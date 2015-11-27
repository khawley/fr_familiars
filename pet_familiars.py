#! /bin/python
import re
import sys
import pycurl
from bs4 import BeautifulSoup
from bs4.element import NavigableString
try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO
try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode

fr_cookie = 'Cookie: PHPSESSID=askldfjlkanfln; userid=alsdflanf; user_key=1234567890; username=test;'


# regex globals, declared here to save on compile time
bonded_patt = re.compile(r'You have already bonded with this familiar today\.')
equipped_patt = re.compile(r'You do not have that familiar equipped\.')
rewards_patt = re.compile(r"You[\\]?\'ve earned these rewards today:")
treasure_url_patt = re.compile(r'\/treasure_pile\.png')
chest_url_patt = re.compile(r'\/trinket\/(?P<chest_id>\d+)\.png')
loyalty_patt = re.compile(r'Your (?P<beast>.+) is (?P<loyalty>\w+) and wants'
                          r' to learn more about your clan\.')


def main():
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
    taming_results = [pet_beast(beast["id"]) for beast in taming]

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


def pet_beast(b_id):
    # ids = get_ids(beasts)
    url = "http://flightrising.com/includes/ol/fam_bonding.php"
    send_headers = [
        fr_cookie,
        'Origin: http://flightrising.com',
        'Accept-Encoding: gzip, deflate',
        'Accept-Language: en-US,en;q=0.8',
        'Content-Type: application/x-www-form-urlencoded; charset=UTF-8',
        'Accept: */*',
        'X-Requested-With: XMLHttpRequest',
    ]
    # for id in ids:
    result = parse_response(curl(url, send_headers, {"id": b_id}))

    if result["msg"] == "not equipped":
        url = 'http://flightrising.com/includes/familiar_active.php?id=11902870&itm=' + str(b_id)
        result = parse_response(curl(url, send_headers))
        if result["msg"] == "not_equipped":
            sys.stderr.write("Error: Tried to equip familiar id " + str(b_id) +
                             " but still failed to 'pet'")
    return result


def parse_response(html):
    soup = BeautifulSoup(html, "html.parser")
    divs = soup.find_all("div")
    result = {}

    for div in divs:

        # is already bonded?
        match = re.search(bonded_patt, div.text)
        if match:
            result = {
                "msg": "already bonded"
            }
            break

        # is not equipped?
        match = re.search(equipped_patt, div.text)
        if match:
            result = {
                "msg": "not equipped"
            }
            break

        # successful?
        match = re.search(rewards_patt, div.text)
        if match:
            result = parse_rewards(div)
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
        match = re.search(treasure_url_patt, img.attrs["src"])
        if match:
            gold = img.find_parent("span").text.strip()
            continue

        # has a chest?
        match = re.search(chest_url_patt, img.attrs["src"])
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
    match = re.search(loyalty_patt, div.text)
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


def header_function(header_line):
    # HTTP standard specifies that headers are encoded in iso-8859-1.
    # On Python 2, decoding step can be skipped.
    header_line = header_line.decode('utf-8')

    # Header lines include the first status line (HTTP/1.x ...).
    # We are going to ignore all lines that don't have a colon in them.
    # This will botch headers that are split on multiple lines...
    if ':' not in header_line:
        return

    # Break the header line into header name and value.
    name, value = header_line.split(':', 1)

    # Remove whitespace that may be present.
    # Header lines include the trailing newline, and there may be whitespace
    # around the colon.
    name = name.strip()
    value = value.strip()

    # Header names are case insensitive.
    # Lowercase name here.
    name = name.lower()

    # Now we can actually record the header name and value.
    headers[name] = value


def curl(url, send_headers=[], post_data={}):
    global headers
    headers = {}

    buffer = BytesIO()

    c = pycurl.Curl()
    c.setopt(pycurl.URL, url)
    if send_headers:
        c.setopt(pycurl.HTTPHEADER, send_headers)
    if post_data:
        # post_data = {'field': 'value'}
        # Form data must be provided already urlencoded.
        postfields = urlencode(post_data)
        # Sets request method to POST,
        # Content-Type header to application/x-www-form-urlencoded
        # and data to send in request body.
        c.setopt(c.POSTFIELDS, postfields)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.HEADERFUNCTION, header_function)
    # c.setopt(c.VERBOSE, True)
    c.perform()
    c.close()

    # Figure out what encoding was sent with the response, if any.
    # Check against lowercased header name.
    encoding = None
    if 'content-type' in headers:
        content_type = headers['content-type'].lower()
        match = re.search('charset=(\S+)', content_type)
        if match:
            encoding = match.group(1)
            # print('Decoding using %s' % encoding)
    if encoding is None:
        # Default encoding for HTML is iso-8859-1.
        # Other content types may have different default encoding,
        # or in case of binary data, may have no encoding at all.
        encoding = 'iso-8859-1'
        # print('Assuming encoding is %s' % encoding)

    body = buffer.getvalue()
    # Decode using the encoding we figured out.
    return body.decode(encoding)


main()
# pet_beast(413)
# print parse_response(response)