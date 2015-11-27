#! /bin/python
import re
import sys
from bs4 import BeautifulSoup

from MyCurl import MyCurl
from Bestiary import Bestiary


class PetFamiliars:

    # regex globals, declared here to save on compile time
    bonded_patt = re.compile(r'You have already bonded with this '
                             r'familiar today\.')
    equipped_patt = re.compile(r'You do not have that familiar equipped\.')
    rewards_patt = re.compile(r"You[\\]?\'ve earned these rewards today:")
    treasure_url_patt = re.compile(r'\/treasure_pile\.png')
    chest_url_patt = re.compile(r'\/trinket\/(?P<chest_id>\d+)\.png')
    loyalty_patt = re.compile(r'Your (?P<beast>.+) is (?P<loyalty>\w+) '
                              r'and wants to learn more about your clan\.')

    send_headers = []
    bestiary_breakdown = {}
    to_tame = []
    taming_results = []
    taming_breakdown = {}

    def __init__(self, fr_cookie, equip_dragon=None,
                 bestiary_list=None, get_pages=None, verbose=False):
        self.fr_cookie = fr_cookie
        self.verbose = verbose
        self.equip_dragon = equip_dragon
        self.__get_pages = get_pages
        self.bestiary_breakdown = bestiary_list or []  # self.get_bestiary()

        # must have User-Agent set
        self.send_headers = [
            self.fr_cookie,
            'Origin: http://flightrising.com',
            'Accept-Encoding: gzip, deflate',
            'Accept-Language: en-US,en;q=0.8',
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
            'Content-Type: application/x-www-form-urlencoded; charset=UTF-8',
            'Accept: */*',
            'X-Requested-With: XMLHttpRequest',
        ]

    def echo(self, msg, newline=False):
        if newline:
            msg += "\n"
        if self.verbose:
            sys.stdout.write(msg)

    def get_bestiary(self, pages=None):
        get_pages = pages or self.__get_pages
        if not self.bestiary_breakdown:
            self.bestiary_breakdown = Bestiary(
                pages=get_pages, fr_cookie=self.fr_cookie, verbose=self.verbose).get_list()
        return self.bestiary_breakdown

    def pet_my_familiars(self):
        if not self.bestiary_breakdown:
            self.get_bestiary()
        for beast in self.bestiary_breakdown["taming"]:
            self.echo("-- petting " + beast["name"])
            result = self.pet_one_familiar(beast["id"])
            if result["msg"] == "not equipped":
                self.__equip_familiar(beast["id"])
                result = self.pet_one_familiar(beast["id"])
                if result["msg"] == "not equipped":
                    sys.stderr.write("Error: Tried to equip familiar '"
                                     + str(beast["name"]) +
                                     "' but still failed to 'pet'")
            self.taming_results.append(result)
            self.echo(" -- message: " + result["msg"], True)
        self.__breakdown_taming_results()

    def __breakdown_taming_results(self):
        if not self.taming_results:
            sys.stderr.write("Error: No taming_results to breakdown")
            return

        gold_chests = []
        iron_chests = []
        rusted_chests = []
        failures = []
        total_gold = 0
        total_successes = 0
        for result in self.taming_results:
            if result.get("chest", ""):
                if result["chest"] == "gold":
                    gold_chests.append(result)
                elif result["chest"] == "iron":
                    iron_chests.append(result)
                elif result["chest"] == "rusted":
                    rusted_chests.append(result)

            total_gold += result.get("gold", 0)

            if result["msg"] != "rewards":
                failures.append(result)
            else:
                total_successes += 1

        self.taming_breakdown = {
            "gold_chests": gold_chests,
            "iron_chests": iron_chests,
            "rusted_chests": rusted_chests,
            "failures": failures,
            "total_gold": total_gold
        }

    def print_taming_breakdown(self):
        if not self.taming_breakdown:
            self.__breakdown_taming_results()

        if self.taming_breakdown["gold_chests"]:
            print "gold_chests:", len(self.taming_breakdown["gold_chests"]),
            print "-", self.taming_breakdown["gold_chests"]
        else:
            print "gold_chests: 0"
        print "iron_chests:", len(self.taming_breakdown["iron_chests"])
        print "rusted_chests:", len(self.taming_breakdown["rusted_chests"])
        print "total_gold:", self.taming_breakdown["total_gold"]
        print "total successfully pet:", \
            self.taming_breakdown["total_successes"]

        if self.taming_breakdown["failures"]:
            print "failed:", len(self.taming_breakdown["failures"]),
            print "-", self.taming_breakdown["failures"]

    def pet_one_familiar(self, b_id):
        url = "http://flightrising.com/includes/ol/fam_bonding.php"
        result = self.__parse_response(
            MyCurl.curl(url, self.send_headers, {"id": b_id}))
        return result

    def __equip_familiar(self, b_id):
        if not self.equip_dragon:
            self.echo(" -- not equipping, not default dragon")
            return {
                "msg": "not equipped",
                "beast": b_id
            }
        self.echo(" -- equipping familiar")
        url = 'http://flightrising.com/includes/familiar_active.php?' \
              'id=' + str(self.equip_dragon) + '&itm=' + str(b_id)
        return MyCurl.curl(url, self.send_headers)

    def __parse_response(self, html):
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
        result = {
            "msg": "rewards"
        }
        # find all imgs, then find parents, get text, and have number
        imgs = div.find_all("img")
        for img in imgs:
            # is treasure pile?
            match = re.search(self.treasure_url_patt, img.attrs["src"])
            if match:
                result["gold"] = img.find_parent("span").text.strip()
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
            result["beast"] = match.group("beast")
            result["loyalty"] = match.group("loyalty")

        return result
