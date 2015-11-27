#! /bin/python
import re
import sys
from bs4 import BeautifulSoup

from MyCurl import MyCurl
from Bestiary import Bestiary

my_fr_cookie = 'Cookie: PHPSESSID=askldfjlkanfln; userid=alsdflanf; user_key=1234567890; username=test;'
dragon_id = '11902870'


class PetFamiliars:

    # regex globals, declared here to save on compile time
    bonded_patt = re.compile(r'You have already bonded with this familiar today\.')
    equipped_patt = re.compile(r'You do not have that familiar equipped\.')
    rewards_patt = re.compile(r"You[\\]?\'ve earned these rewards today:")
    treasure_url_patt = re.compile(r'\/treasure_pile\.png')
    chest_url_patt = re.compile(r'\/trinket\/(?P<chest_id>\d+)\.png')
    loyalty_patt = re.compile(r'Your (?P<beast>.+) is (?P<loyalty>\w+) and wants'
                              r' to learn more about your clan\.')

    def __init__(self, fr_cookie=None):
        self.fr_cookie = fr_cookie or my_fr_cookie
        pass

    def get_besiary(self, pages=None):
        get_pages = pages or 1
        self.bestiary_dict = Bestiary(pages=get_pages, fr_cookie=my_fr_cookie).get_all()
        return self.bestiary_dict

    def main(self):
        # read in bestiary file, sort dict by non-awakened, and non-locked
        with open('bestiary_dict.py') as bestiary_file:
            bestiary = eval(bestiary_file.read())
        print bestiary
        if type(bestiary) is dict:
            awakened = [bestiary[b_id] for b_id in bestiary
                        if bestiary[b_id]["loyalty"].lower() == "awakened"]
            locked = [bestiary[b_id]["name"] for b_id in bestiary
                      if bestiary[b_id]["loyalty"].lower() == "locked"]
            taming = [bestiary[b_id] for b_id in bestiary
                      if bestiary[b_id]["loyalty"].lower()
                      not in ("locked", "awakened")]
        else:  # is of newer type list :)
            awakened = [b for b in bestiary if b["loyalty"].lower() == "awakened"]
            locked = [b for b in bestiary if b["loyalty"].lower() == "locked"]
            taming = [b for b in bestiary if b["loyalty"].lower()
                      not in ("locked", "awakened")]

        # print stats
        print "locked: ", len(locked), " -", locked
        print "awakened: ", len(awakened)
        print "taming: ", len(taming)
        print "total =", len(bestiary)
        if len(bestiary) != (len(locked) + len(awakened) + len(taming)):
            print "Error!  Not adding up correctly!"
        print

        # try to pet everyone
        taming_results = [self.pet_beast(beast["id"]) for beast in taming]

        # prep the results
        gold_chests = [result for result in taming_results
                       if result["chest"] == "gold"]

        print "gold_chests:", len(gold_chests), gold_chests
        print "iron_chests:", len([result for result in taming_results
                                   if result["chest"] == "iron"])
        print "rusted_chests:", len([result for result in taming_results
                                     if result["chest"] == "rusted"])
        failures = [result for result in taming_results
                    if result["msg"] != "rewards"]
        if failures:
            print "failed:", len(failures), failures

    def pet_beast(self, b_id):
        url = "http://flightrising.com/includes/ol/fam_bonding.php"

        # must have User-Agent set
        send_headers = [
            fr_cookie,
            'Origin: http://flightrising.com',
            'Accept-Encoding: gzip, deflate',
            'Accept-Language: en-US,en;q=0.8',
            'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
            'Content-Type: application/x-www-form-urlencoded; charset=UTF-8',
            'Accept: */*',
            'X-Requested-With: XMLHttpRequest',
        ]

        # for id in ids:
        result = self.parse_response(MyCurl.curl(url, send_headers, {"id": b_id}))

        if result["msg"] == "not equipped":
            url = 'http://flightrising.com/includes/familiar_active.php?id=' + str(dragon_id) + '&itm=' + str(b_id)
            result = self.parse_response(MyCurl.curl(url, send_headers))
            if result["msg"] == "not_equipped":
                sys.stderr.write("Error: Tried to equip familiar id " + str(b_id) +
                                 " but still failed to 'pet'")
        return result

    def parse_response(self, html):
        soup = BeautifulSoup(html, "html.parser")
        divs = soup.find_all("div")
        result = {}

        for div in divs:

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
                result = self.parse_rewards(div)
                break
        return result

    def parse_rewards(div):
        # match out loyalty level.
        # match out the gold
        # match out chests

        beast = ""
        gold = ""
        chest = ""
        loyalty = ""

        # find all imgs, then find parents, get text, and have number
        imgs = div.find_all("img")
        for img in imgs:
            # is treasure pile?
            match = re.search(self.treasure_url_patt, img.attrs["src"])
            if match:
                gold = img.find_parent("span").text.strip()
                continue

            # has a chest?
            match = re.search(self.chest_url_patt, img.attrs["src"])
            if match:
                chest_id = match.group("chest_id")
                if chest_id == "576":
                    chest = "gold"
                elif chest_id == "575":
                    chest = "iron"
                elif chest_id == "574":
                    chest = "rusted"
                else:
                    chest = "??"
        match = re.search(self.loyalty_patt, div.text)
        if match:
            beast = match.group("beast")
            loyalty = match.group("loyalty")

        return {
            "msg": "rewards",
            "beast": beast,
            "gold": gold,
            "chest": chest,
            "loyalty": loyalty
        }


# main()
# pet_beast(413)
print PetFamiliars().get_besiary(pages=1)
# print parse_response(response)