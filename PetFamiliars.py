import re
import sys
from bs4 import BeautifulSoup

from MyCurl import MyCurl
from Bestiary import Bestiary


class PetFamiliars:
    """
    Class built to intake, and then pet all your familiars.  Specifically those
    that are still in the process of 'taming' and have not yet been 'awakened',
    but it can pet awakened too.  (as long they are not in the Vault)
    """

    # regex globals, declared here to save on compile time
    bonded_patt = re.compile(r'You have already bonded with this '
                             r'familiar today\.')
    equipped_patt = re.compile(r'You do not have that familiar equipped\.')
    rewards_patt = re.compile(r"You[\\]?\'ve earned these rewards today:")
    treasure_url_patt = re.compile(r'\/treasure_pile\.png')
    chest_url_patt = re.compile(r'\/trinket\/(?P<chest_id>\d+)\.png')
    loyalty_patt = re.compile(r'Your (?P<beast>.+) is (?P<loyalty>\w+) '
                              r'and wants to learn more about your clan\.')

    # list of dragon_ids that had a familiar with gold chest that was removed,
    # and are now waiting for a new familiar to be equipped
    dragons_to_equip = []

    bestiary_breakdown = {}  # dict of lists from Bestiary.get_all()
    taming_results = []  # list of dicts, results of each familiar pet
    taming_breakdown = {}  # breakdown of taming_results

    def __init__(self, fr_cookie, equip_dragon=None,
                 bestiary_breakdown=None, dragon_list=None,
                 pet_awakened=False, verbose=False):
        """
        Setup class with initial variables
        :param string fr_cookie: Login Cookie Header for FR
            starts with "Cookie: ..."
        :param int/string equip_dragon: default dragon_id to equip familiars in
            hoard to
        :param dict bestiary_breakdown: dict of lists from Bestiary class
        :param list dragon_list: list from DragonLair class
        :param bool pet_awakened: whether to also pet awakened familiars (must
            be in Hoard, not Vault)
        :param bool verbose: whether to print verbose progress statements
        :return:
        """
        self.fr_cookie = fr_cookie
        self.verbose = verbose
        self.equip_dragon = str(equip_dragon)
        self.pet_awakened = pet_awakened
        self.bestiary_breakdown = bestiary_breakdown or {}
        self.dragons = dragon_list or []

        # must have User-Agent set
        self.send_headers = [
            self.fr_cookie,
            'Origin: http://flightrising.com',
            'Accept-Language: en-US,en;q=0.8',
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
            'Content-Type: application/x-www-form-urlencoded; charset=UTF-8',
            'Accept: */*',
            'X-Requested-With: XMLHttpRequest',
        ]

    def echo(self, msg, newline=False):
        """
        If verbose, print the msg.
        :param string msg: String to be printed
        :param bool newline: Whether to add a newline after msg
        :return:
        """
        if newline:
            msg += "\n"
        if self.verbose:
            sys.stdout.write(msg)

    def pet_my_familiars(self):
        """
        Cycle through all beasts in besitary_breakdown["taming"] and, if
        pet_awakened is True, all the beasts in bestiary_breakdown["awakened"]
        All results are parsed and appended to taming_results, then passed to
        __breakdown_taming_results()
        :return:
        """
        if not self.bestiary_breakdown:
            sys.stderr.write("Error: Please set bestiary_breakdown\n")
            return

        beasts_to_pet = self.bestiary_breakdown["taming"]

        if self.pet_awakened:
            beasts_to_pet += self.bestiary_breakdown["awakened"]

        for beast in beasts_to_pet:
            self.echo("-- petting " + beast["name"])
            result = self.pet_one_familiar(beast["id"])
            if result["msg"] == "not equipped":
                if self.__equip_familiar(beast["id"]):
                    result = self.pet_one_familiar(beast["id"])
                    if result["msg"] == "not equipped":
                        sys.stderr.write("Error: Tried to equip familiar '" +
                                         str(beast["name"]) +
                                         "' but still failed to 'pet'")

            # add in id + name here, else results are unknown
            result["id"] = beast["id"]
            result["name"] = beast["name"]

            self.taming_results.append(result)
            chest = ""
            if result.get("chest"):
                chest = " -- chest: " + result["chest"]
            self.echo(" -- message: " + result["msg"] + chest, True)
        self.__breakdown_taming_results()

    def __breakdown_taming_results(self):
        """
        Parse the results in taming_results for readability and consolidation.
        This is then stored in taming_breakdown
        :return:
        """
        if not self.taming_results:
            sys.stderr.write("Error: No taming_results to breakdown")
            return

        gold_chests = []
        iron_chests = []
        rusted_chests = []
        failures = []
        successes = []
        total_treasure = 0
        for result in self.taming_results:
            if result.get("chest", ""):
                if result["chest"] == "gold":
                    gold_chests.append(result)
                elif result["chest"] == "iron":
                    iron_chests.append(result)
                elif result["chest"] == "rusted":
                    rusted_chests.append(result)

            total_treasure += int(result.get("treasure", 0))

            if result["msg"] != "rewards":
                failures.append(result)
            else:
                successes.append(result)

        self.taming_breakdown = {
            "gold_chests": gold_chests,
            "iron_chests": iron_chests,
            "rusted_chests": rusted_chests,
            "failures": failures,
            "total_treasure": total_treasure,
            "successes": successes
        }

    def print_taming_breakdown(self):
        """
        Pretty Print taming_breakdown
        :return:
        """
        if not self.taming_breakdown:
            self.__breakdown_taming_results()

        if self.taming_breakdown["gold_chests"]:
            print "gold_chests:", len(self.taming_breakdown["gold_chests"]),
            print "-", self.taming_breakdown["gold_chests"]
        else:
            print "gold_chests: 0"
        print "iron_chests:", len(self.taming_breakdown["iron_chests"])
        print "rusted_chests:", len(self.taming_breakdown["rusted_chests"])
        print "total_treasure:", self.taming_breakdown["total_treasure"]
        print "total successfully pet:", \
            len(self.taming_breakdown["successes"])

        if self.taming_breakdown["failures"]:
            print "failed:", len(self.taming_breakdown["failures"]),
            print "-", self.taming_breakdown["failures"]

    def pet_one_familiar(self, familiar_id):
        """
        Pet familiar of id passed in and return results
        :param string familiar_id: familiar id to pet
        :return: results = { "msg": "...",
        :rtype: dict
        """
        url = "http://flightrising.com/includes/ol/fam_bonding.php"
        result = self.__parse_response_familiar_bonding(
            MyCurl.curl(url, self.send_headers, {"id": familiar_id}))
        if self.dragons and result.get("chest") == "gold":
            self.echo(" * returning familiar to hoard")
            dragon_id = self.__locate_dragon(familiar_id)
            if dragon_id:
                self.dragons_to_equip.append(dragon_id)
                self.__unequip_dragons_familiar(dragon_id)
        return result

    def __equip_familiar(self, familiar_id):
        """
        Equip the f_id to a dragon in dragons_to_equip or the default
        equip_dragon.  If neither, return False.
        :param string familiar_id: familiar id to equip to dragon
        :return:
        """
        # if list of waiting dragons, pull from them first, then use default
        if self.dragons_to_equip:
            self.echo(" ~ equipping to dragon from list")
            dragon_id = self.dragons_to_equip.pop()
        elif self.equip_dragon:
            self.echo(" ~ equipping to default")
            dragon_id = self.equip_dragon
        else:
            self.echo(" -- not equipping, no default dragon")
            return False

        self.echo(" ~ equipping familiar")
        url = 'http://flightrising.com/includes/familiar_active.php?' \
              'id=' + str(dragon_id) + '&itm=' + str(familiar_id)
        return MyCurl.curl(url, self.send_headers)

    def __unequip_dragons_familiar(self, dragon_id):
        """
        Using the dragon_id, remove the familiar, not replace it.  (Usually
        result of a gold chest familiar)
        :param string dragon_id: dragon id to remove familiar from
        :return:
        """
        self.echo("~ unequipping dragon:" + str(dragon_id))
        url = "http://flightrising.com/includes/familiar_active.php?id=" + \
              str(dragon_id) + "&itm=0"
        MyCurl.curl(url, self.send_headers)

    def __parse_response_familiar_bonding(self, html):
        """
        Given html from 'pet familiar' curl, determine success/failure.
        If succes, parse out rewards.
        :param string html: body html from a curl response
        :return: result = {"msg": "....", }
        :rtype: dict
        """
        result = {}

        for div in BeautifulSoup(html, "html.parser").find_all("div"):

            # is already bonded?
            match = re.search(self.bonded_patt, div.text)
            if match:
                result = {
                    "msg": "already bonded"
                }
                break

            # is not equipped?
            match = re.search(self.equipped_patt, div.text)
            if match:
                result = {
                    "msg": "not equipped"
                }
                break

            # successful?
            match = re.search(self.rewards_patt, div.text)
            if match:
                result = self.__parse_rewards(div)
                break
        return result

    def __parse_rewards(self, div):
        """
        Given a div from BeautifulSoup and the familiar bonding response, parse
        out the treasue, possible chests, and loyalty.
        :param Tag div:
        :return: result = { "msg": "rewards", "treasure": "...",
            "loyalty": "...", ["chest": "..."]}
        :rtype: dict
        """
        result = {
            "msg": "rewards"
        }
        # find all imgs, then find parents, get text, and have number
        imgs = div.find_all("img")
        for img in imgs:
            # is treasure pile?
            match = re.search(self.treasure_url_patt, img.attrs["src"])
            if match:
                result["treasure"] = img.find_parent("span").text.strip()
                continue

            # has a chest?
            match = re.search(self.chest_url_patt, img.attrs["src"])
            if match:
                chest_id = match.group("chest_id")
                if chest_id == "576":
                    result["chest"] = "gold"
                elif chest_id == "575":
                    result["chest"] = "iron"
                elif chest_id == "574":
                    result["chest"] = "rusted"
                else:
                    result["chest"] = "??"

        match = re.search(self.loyalty_patt, div.text)
        if match:
            # added through parent function
            # result["beast"] = match.group("beast")
            result["loyalty"] = match.group("loyalty")

        return result

    def __locate_dragon(self, familiar_id):
        """
        Find the dragon with familiar_id equipped.
        :param string familiar_id: familiar id to locate in dragon list
        :return: dragon_id
        :rtype: string
        """
        if not self.dragons:
            return ""
        for d in self.dragons:
            if d["familiar_id"] == familiar_id:
                return d["dragon_id"]
        return ""
