import re
from bs4 import BeautifulSoup

from fr_interactions.FrBase import FrBase
from fr_interactions.fr_constants import GILDED_CHEST_ID, IRON_CHEST_ID,\
    RUSTED_CHEST_ID


class Chests(FrBase):
    """
    Class built to open all, some or one treasure chest, as specified by the
    function calls.  Also uses ITEM_MAP to keep track of all items seen thus
    far. Cuts down on querying time to flightrising to get item names.
    """

    # regex patterns
    item_ajax_url_patt = re.compile(r"includes/itemajax\.php\?"
                                    r"id=(?P<item_id>\d+)"
                                    r"&tab=(?P<item_type>\w+)")
    treasure_pile_img_patt = re.compile(r"treasure_pile")
    gem_pile_img_patt = re.compile(r"gem_pile")
    item_ajax_response_patt = re.compile(r'(?P<item_name>.+)\s+'
                                         r'(?P<item_type>.+)\s+'
                                         r'(?P<item_description>[^\n]+)\s+'
                                         r'Sell Value: (?P<sell_value>\d+)')

    all_chest_results = {}
    raw_results = {"gilded": [], "iron": [], "rusted": []}
    item_map = {}
    item_totals = {}

    def __init__(self, fr_cookie, gilded_qty=0, iron_qty=0,
                 rusted_qty=0, item_map=None, verbosity=0):
        """
        :param str fr_cookie: Cookie that has login information
        :param int gilded_qty: number of gilded chests to open
        :param int iron_qty: number of iron chests to open
        :param int rusted_qty: number of rusted chests to open
        :param dict item_map: map from previous run, dict of item_ids as keys,
            and descriptive dicts as values
        :param int verbosity: level of error messages to print
        :return:
        """
        try:
            self.gilded_qty = int(gilded_qty) \
                if type(gilded_qty) is str else gilded_qty
            self.iron_qty = int(iron_qty) \
                if type(iron_qty) is str else iron_qty
            self.rusted_qty = int(rusted_qty)\
                if type(rusted_qty) is str else rusted_qty
        except ValueError:
            self.error("Error: parameters not of type int", True)
            exit()
        self.item_map = item_map or self.item_map
        FrBase.__init__(self, fr_cookie, verbosity)

    def open_all_chests(self):
        """
        Cycle through all 3 types of chests and open them, if any.
        :return:
        """
        self.open_gilded_chests(self.gilded_qty)
        self.open_iron_chests(self.iron_qty)
        self.open_rusted_chests(self.rusted_qty)

    def open_gilded_chests(self, quantity=0):
        """
        Open all gilded chests up to quantity, or until no more if quantity=0.
        Appends results to self.raw_results["gilded"]
        :param int quantity: number of gilded chests to try to open.
        :return:
        """
        # if not quantity, go until there is no more
        i = 0
        while True:
            result = self.open_one_chest(GILDED_CHEST_ID)
            self.raw_results["gilded"].append(tuple(result))
            if result:
                self.echo("-- opened gilded chest: "+str(result), True)
            i += 1
            if i == quantity or not result:
                break

    def open_iron_chests(self, quantity=0):
        """
        Open all gilded chests up to quantity, or until no more if quantity=0.
        Appends results to self.raw_results["iron"]
        :param int quantity: number of iron chests to try to open
        :return:
        """
        # if not quantity, go until there is no more
        i = 0
        while True:
            result = self.open_one_chest(IRON_CHEST_ID)
            self.raw_results["iron"].append(tuple(result))
            if result:
                self.echo("-- opened iron chest: "+str(result), True)
            i += 1
            if i == quantity or not result:
                break

    def open_rusted_chests(self, quantity=0):
        """
        Open all rusted chests up to quantity, or until no more if quantity=0.
        Appends results to self.raw_results["rusted"]
        :param int quantity: number of rusted chests to try to open.
        :return:
        """
        # if not quantity, go until there is no more
        i = 0
        while True:
            result = self.open_one_chest(RUSTED_CHEST_ID)
            self.raw_results["rusted"].append(tuple(result))
            if result:
                self.echo("-- opened rusted chest: "+str(result), True)
            i += 1
            if i == quantity or not result:
                break

    def open_one_chest(self, chest_id):
        """
        Open a single chest with specified id.
        :param chest_id:
        :return: list of result dicts from self.__parse_open_chest_response
            ex: [{"id":...,"type":...,"qty":...,"name":...},...]
        :rtype: list
        """
        # list of results from ONE chest
        results = self.__parse_open_chest_response(
            self.__curl_open_chest(str(chest_id)))

        # add these results to the main dict for tallying
        for r in results:
            self.item_totals[r["id"]] = self.item_totals.get(r["id"], 0) + \
                                        int(r["quantity"])
        return results

    def __curl_open_chest(self, chest_id):
        """
        Curl to open one chest with the specified id.
        :param chest_id:
        :return: html from curl
        :rtype: str
        """
        url = "http://flightrising.com/includes/ol/openchest.php"
        post_data = {
            "id": chest_id,
            "ver": "con"  # this is 'confirming' version
        }
        return self.curl(url, post_data=post_data)

    def __parse_open_chest_response(self, html):
        """
        Given the html result of curling to open a chest, parse out the
        response for the various items retrieved from opening the chest
        :param str html:
        :return: list of result dicts
            ex: [{"id":...,"type":...,"qty":...,"name":...},...]
        :rtype: list
        """
        this_rewards = []
        soup = BeautifulSoup(html, "html.parser")
        for span in soup.find_all("span"):
            # get qty in the <div>
            quantity = span.find("div").text.strip()
            # get a href for id + tab (type), also can use for more info

            a_tag = span.find("a")
            if a_tag:
                match = re.search(self.item_ajax_url_patt,
                                  a_tag.attrs.get("rel", [""])[0])
                if match:
                    result = self.__get_item_name(match.group("item_id"),match.group("item_type"))
                    result["quantity"] = quantity

                    this_rewards.append(result)

            # not an item, likely treasure or gems
            else:
                img_src = span.find("img").attrs.get("src", "")
                found = ""
                # is treasure
                if re.search(self.treasure_pile_img_patt, img_src):
                    found = "treasure"
                elif re.search(self.gem_pile_img_patt, img_src):
                    found = "gem"

                if found:
                    this_rewards.append({
                        "id": found,
                        "type": found,
                        "name": found,
                        "quantity": quantity
                    })

        return this_rewards

    def __get_item_name(self, item_id, item_type):
        """

        :param str item_id: id of the item
        :param str item_type: type as specified in the ajax url
            (may not match actual type, ex: equipment & apparel)
        :return: dict of ajaxed results - id, name, type, ajax_url or {}
        :rtype: dict
        """
        # look up in internal map first.  If there, simply return result
        if self.item_map.get(item_id):
            return self.item_map[item_id]

        # query the itemajax for the name + description
        url = "https://flightrising.com/includes/itemajax.php?id=" + \
              item_id + "&tab=" + item_type

        soup = BeautifulSoup(self.curl(url), "html.parser")
        m = re.search(self.item_ajax_response_patt, soup.text)
        if m:
            result = {
                "id": item_id,
                "name": m.group("item_name"),
                "type": m.group("item_type"),
                "ajax_url": url

            }
            # add to internal dict for quicker querying next time
            self.item_map[item_id] = result
            return result
        return {}

    def print_chest_results(self):
        """
        Based on the internally updated self.item_totals, print out the sorted
        results of all items (and treasure) gained from chests.
        :return:
        """
        # make item_map only from item_totals, sort by type
        sorted_item_map = sorted([self.item_map[item_id]
                                  for item_id in self.item_totals.keys()
                                  if item_id in self.item_map],
                                 key=lambda x: x["type"])
        print "Chest Results"
        # print treasure + gems separately, since they aren't in the item_map
        print "- Treasure:", self.item_totals["treasure"]
        print "- Gems:", self.item_totals.get("gem", "0")
        print

        this_type = None
        for item_dict in sorted_item_map:
            if item_dict["type"] != this_type:
                this_type = item_dict["type"]
                print "===", item_dict["type"], "==="
            print "-", item_dict["name"], self.item_totals[item_dict["id"]],
            print "(id:" + item_dict["id"] + ")"
