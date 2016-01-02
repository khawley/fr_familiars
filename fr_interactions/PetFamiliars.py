from bs4 import BeautifulSoup
import re

from .FrBase import FrBase


class PetFamiliars(FrBase):
    """
    Class built to intake, and then pet all your familiars.  Specifically those
    that are still in the process of 'taming' and have not yet been 'awakened',
    but it can pet awakened too.  (as long they are not in the Vault)
    """

    # regex globals, declared here to save on compile time
    bonded_patt = re.compile(r'You have already bonded with this '
                             r'familiar today\.')
    first_bonding_patt = re.compile(r'Please visit your lair first.')
    equipped_patt = re.compile(r'You do not have that familiar equipped\.')
    rewards_patt = re.compile(r"You[\\]?\'ve earned these rewards today:")
    treasure_url_patt = re.compile(r'/treasure_pile\.png')
    chest_url_patt = re.compile(r'/trinket/(?P<chest_id>\d+)\.png')
    loyalty_patt = re.compile(r'Your (?P<beast>.+) is (?P<loyalty>\w+) '
                              r'and wants to learn more about your clan\.')

    # list of dragon_ids that had a familiar with gilded chest that was removed,
    # and are now waiting for a new familiar to be equipped
    dragons_to_equip = []

    bestiary_breakdown = {}  # dict of lists from Bestiary.get_all()
    taming_results = []  # list of dicts, results of each familiar pet
    taming_breakdown = {}  # breakdown of taming_results
    TAMING_SORT_ORDER = ("Loyal", "Companion", "Inquisitive", "Relaxed", "Tolerant",
                   "Wary")

    # todo: rename equip_dragon to default_equip_dragon
    def __init__(self, fr_cookie, equip_dragon=None,
                 bestiary_breakdown=None, dragon_list=None,
                 unequip_awakened=True, equip_next_after_awakening=True,
                 pet_awakened=False, verbosity=False):
        """
        Setup class with initial variables
        :param string fr_cookie: Login Cookie Header for FR
            starts with "Cookie: ..."
        :param int/string equip_dragon: default dragon_id to equip familiars in
            hoard to
        :param dict bestiary_breakdown: dict of lists from Bestiary class
        :param list dragon_list: list from DragonLair class
        :param bool unequip_awakened: whether to unequip familiar if it awakens
        :param bool equip_next_after_awakening: whether to equip the next familiar
            to the recently awakened familiar's dragon
        :param bool pet_awakened: whether to also pet awakened familiars (must
            be in Hoard, not Vault)
        :param int verbosity: How verbose to be:
            0 - do not print echo statements
            1 - print echo statements
        :return:
        """
        FrBase.__init__(self, fr_cookie, verbosity)
        self.equip_dragon = str(equip_dragon)
        self.unequip_awakened = unequip_awakened
        self.equip_next_after_awakening = equip_next_after_awakening
        self.pet_awakened = pet_awakened
        self.bestiary_breakdown = bestiary_breakdown or {}
        self.dragons = dragon_list or []

    def pet_my_familiars(self):
        """
        Cycle through all beasts in besitary_breakdown["taming"] and, if
        pet_awakened is True, all the beasts in bestiary_breakdown["awakened"]
        All results are parsed and appended to taming_results, then passed to
        __breakdown_taming_results()
        :return:
        """
        if not self.bestiary_breakdown:
            self.error("Error: Please set bestiary_breakdown", True)
            return

        self.taming_results = []  # do not want to add the results in twice
        # taming sorted by loyalty, with loyal to wary
        beasts_to_pet = sorted(self.bestiary_breakdown["taming"],
                               key=lambda x: (
                                   self.TAMING_SORT_ORDER.index(x["loyalty"]),
                                   x["name"]))

        if self.pet_awakened:
            beasts_to_pet += self.bestiary_breakdown["awakened"]

        for beast in beasts_to_pet:
            self.echo("-- petting " + beast["name"])
            result = self.pet_one_familiar(beast["id"], beast["name"])

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
            self.error("Error: No taming_results to breakdown")
            return

        gilded_chests = []
        iron_chests = []
        rusted_chests = []
        failures = []
        successes = []
        total_treasure = 0
        for result in self.taming_results:
            if result.get("chest", ""):
                if result["chest"] == "gilded":
                    gilded_chests.append(result)
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
            "gilded_chests": gilded_chests,
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

        for chest in ["gilded_chests", "iron_chests", "rusted_chests"]:
            chests_len = len(self.taming_breakdown[chest])
            msg = "{}: {}".format(chest, chests_len)
            if chests_len:
                msg += " - {}".format(self.taming_breakdown[chest])
            self.echo_n(msg)

        self.echo_n("total_treasure: {}"
                    .format(self.taming_breakdown["total_treasure"]))

        self.echo_n("total successfully pet: {}"
                    .format(self.taming_breakdown["successes"]))

        if self.taming_breakdown["failures"]:
            self.echo_n("failed: {} - {}"
                        .format(len(self.taming_breakdown["failures"]),
                                self.taming_breakdown["failures"]))

    def pet_one_familiar(self, familiar_id, familiar_name="",
                         recursing=False):
        """
        Pet familiar of id passed in and return results
        :param string familiar_id: familiar id to pet
        :param string familiar_name: familiar name, used for error statement
        :param bool recursing: True/False to prevent infinite loop recursion
        :return: results = { "msg": "...",
        :rtype: dict
        """
        url = "http://flightrising.com/includes/ol/fam_bonding.php"
        html = self.curl(url, post_data={"id": familiar_id})

        # confirm user is logged in
        # must exit if not logged in
        if not self.is_logged_in(html):
            exit()

        result = self.__parse_response_familiar_bonding(html)

        # got a gilded chest, so unequip familiar, and add dragon to equip list
        if self.dragons:
            dragon_id = self.__find_dragon_with_familiar(familiar_id)
            result["dragon_id"] = dragon_id

            if result.get("chest") == "gilded" and \
                    dragon_id and self.unequip_awakened:
                self.echo(" * returning familiar to hoard")
                self.dragons_to_equip.append(dragon_id)
                self.__unequip_dragons_familiar(dragon_id)

        # familiar not equipped, try equipping & then petting
        if result["msg"] == "not equipped" and not recursing:
            if self.__equip_familiar(familiar_id):
                result = self.pet_one_familiar(familiar_id,
                                               familiar_name, True)
                if result["msg"] == "not equipped":
                    self.error("Error: Tried to equip familiar '" +
                               str((familiar_id, familiar_name)) +
                               "' but still failed to 'pet'")

        # need to visit the dragon page first for some reason
        # will only be 'caught' and executed, if just equipped the new
        # familiar using the above.  If not, will fail (cause it won't know
        # the dragon_id)
        if result["msg"] == "visit lair first":
            dragon_id = self.__find_dragon_with_familiar(familiar_id)
            if dragon_id:
                self.__visit_dragon(dragon_id)
                result = self.pet_one_familiar(familiar_id,
                                               familiar_name, True)

        # add in id + name here, else results are unknown
        result["id"] = familiar_id
        result["name"] = familiar_name
        return result

    def __visit_dragon(self, dragon_id):
        """
        Curl the dragon page.  Needed for 'first time' petting of a familiar.
        :param dragon_id: id of dragon to 'visit'
        :return: html body of visit dragon curl
        :rtype: string
        """
        url = "http://flightrising.com/main.php?p=lair&tab=dragon&did=" + \
              str(dragon_id)
        return self.curl(url)

    def __equip_familiar(self, familiar_id):
        """
        Equip the f_id to a dragon in dragons_to_equip or the default
        equip_dragon.  If neither, return False.
        :param string familiar_id: familiar id to equip to dragon
        :return: html body of equip familiar
        :rtype: string
        """
        # if list of waiting dragons, pull from them first, then use default
        if self.dragons_to_equip and self.equip_next_after_awakening:
            self.echo(" ~ equipping to dragon from list")
            dragon_id = self.dragons_to_equip.pop()
        elif self.equip_dragon:
            self.echo(" ~ equipping to default")
            dragon_id = self.equip_dragon
        else:
            self.echo(" -- not equipping, no default dragon")
            return False

        for i in xrange(0, len(self.dragons)):
            if self.dragons[i]["dragon_id"] == dragon_id:
                self.dragons[i]["familiar_id"] = familiar_id
        self.echo(" ~ equipping familiar")
        url = 'http://flightrising.com/includes/familiar_active.php?' \
              'id=' + str(dragon_id) + '&itm=' + str(familiar_id)
        return self.curl(url)

    def __unequip_dragons_familiar(self, dragon_id):
        """
        Using the dragon_id, remove the familiar, not replace it.  (Usually
        result of a gilded chest familiar)
        :param string dragon_id: dragon id to remove familiar from
        :return: html body of unequip dragon's familiar
        :rtype: string
        """
        self.echo("~ unequipping dragon:" + str(dragon_id))
        url = "http://flightrising.com/includes/familiar_active.php?id=" + \
              str(dragon_id) + "&itm=0"
        return self.curl(url)

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

            # is first time bonding, need to visit lair page first
            match = re.search(self.first_bonding_patt, div.text)
            if match:
                result = {
                    "msg": "visit lair first"
                }
                break

            # successful?
            match = re.search(self.rewards_patt, div.text)
            if match:
                result = self.__parse_rewards(div)
                break

            # default if not one of the above
            result = {"msg": "error, not able to parse msg"}
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
                    result["chest"] = "gilded"
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

    def __find_dragon_with_familiar(self, familiar_id):
        """
        Find the dragon with familiar_id equipped.
        :param string familiar_id: familiar id to locate in dragon list
        :return: dragon_id
        :rtype: string
        """
        if not self.dragons:
            return ""

        return next((dragon["dragon_id"] for dragon in self.dragons
                    if dragon.get("familiar_id", "") == familiar_id), "")
