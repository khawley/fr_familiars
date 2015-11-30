import re
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from HTMLParser import HTMLParser

from .FrBase import FrBase


class Bestiary(FrBase):
    """
    Class to curl bestiary pages and return results of beasts
    """

    # regex patterns, compiled on init for time/memory saving
    img_patt = re.compile(r'/(?P<beast_id>[\d]+)(?:_gray)?\.png')
    name_patt = re.compile(r'^\n(?P<name>[\w\s\-\'\*]+)\n'
                           r'(?P<description>(?:\n|.)*)\n$', re.UNICODE)
    loyalty_patt = re.compile(r'^(?P<loyalty>[\w]+)$')

    base_bestiary_url = "http://flightrising.com/main.php?" \
                        "p=bestiary&tab=familiars&page="

    beasts = []  # list of all beasts in the bestiary
    beasts_breakdown = {}  # dict based on 'taming', 'awakened', &  'locked'

    def __init__(self, fr_cookie, pages=None, bestiary_breakdown=None,
                 verbose=False):
        """
        :param string fr_cookie: Cookie that has login information
        :param int pages: Number of pages from 1 to 'pages' to parse
        :param bool verbose: Print status statements
        :return:
        """
        FrBase.__init__(self, fr_cookie, verbose)
        self.pages = pages or 43
        self.beasts_breakdown = bestiary_breakdown
        if bestiary_breakdown:
            self.beasts = [v for k in bestiary_breakdown
                           for v in bestiary_breakdown[k]]

    def get_all(self):
        """
        Curl and then parse all bestiary pages, returning results.
        :return: dict of lists, of all beasts
        :rtype: dict
        """
        for i in range(1, self.pages + 1):
            self.beasts += self.__get_page(i)
        self.beasts_breakdown = self.__breakdown_beasts()
        return self.beasts_breakdown

    def __get_page(self, page):
        """
        Internal function to get & parse the html from one page of the Bestiary
        :param int/string page:
        :return: results of __parse_bestiary_page, the list of beasts on
            that page
        :rtype: list
        """
        url = self.base_bestiary_url + str(page)
        self.echo("curling " + url)
        html = self.curl(url, self.send_headers)
        self.echo(" -- parsing", True)
        return self.__parse_bestiary_page(html)

    def get_one_page(self, page):
        """
        Externally callable function to get one page of Bestiary and return
        the beasts_breakdown of that page (and any previously crawled pages)
        :param int/string page:
        :return: beasts_breakdown
        :rtype: dict of lists
        """
        this_page_beasts = self.__get_page(page)
        this_page_breakdown = self.__breakdown_beasts(this_page_beasts)
        return this_page_breakdown

    def __breakdown_beasts(self, these_beasts=None):
        """Using self.beasts (or these_beasts), determine awakened, locked, & taming.
        :param list these_beasts: a specific list to breakdown
        :return: dict of lists, sorted by "bestiary", "awakened", "locked",
            and "taming"
        :rtype: dict
        """
        if these_beasts:
            beasts_to_breakdown = these_beasts
        elif self.beasts:
            beasts_to_breakdown = self.beasts
        else:
            self.error("Error: No lists of beasts to breakdown")
            return

        awakened = []
        locked = []
        taming = []

        for beast in beasts_to_breakdown:
            loyalty = beast["loyalty"].lower()
            if loyalty == "awakened":
                awakened.append(beast)
            elif loyalty == "locked":
                locked.append(beast)
            else:
                taming.append(beast)

        if len(beasts_to_breakdown) != \
                (len(locked) + len(awakened) + len(taming)):
            self.error("Error!  Not adding up correctly!")

        return {
            "bestiary": beasts_to_breakdown,
            "awakened": awakened,
            "locked": locked,
            "taming": taming
        }

    def print_beasts_breakdown(self, this_breakdown=None):
        """Print the breakdown of awakened, locked, taming & total.

        :param dict this_breakdown: dict of lists of a particular breakdown
            to print out
        :return:
        """
        if this_breakdown:
            breakdown = this_breakdown
        else:
            if not self.beasts:
                self.get_all()
            breakdown = self.beasts_breakdown

        # breakdown further, for better user inspection
        wary = []
        tolerant = []
        relaxed = []
        inquisitive = []
        companion = []
        loyal = []
        for beast in breakdown["taming"]:
            loyalty = beast.get("loyalty", "").lower()
            if loyalty == "wary":
                wary.append(beast)
            elif loyalty == "tolerant":
                tolerant.append(beast)
            elif loyalty == "relaxed":
                relaxed.append(beast)
            elif loyalty == "inquisitive":
                inquisitive.append(beast)
            elif loyalty == "companion":
                companion.append(beast)
            elif loyalty == "loyal":
                loyal.append(beast)

        # print stats
        print "locked: ", len(breakdown["locked"]),
        print " -", breakdown["locked"]
        print "awakened: ", len(breakdown["awakened"])
        print "taming: ", len(breakdown["taming"])
        print " -- wary: ", len(wary), "-", wary
        print " -- tolerant: ", len(tolerant), "-", tolerant
        print " -- relaxed: ", len(relaxed), "-", relaxed
        print " -- inquisitive: ", len(inquisitive), "-", inquisitive
        print " -- companion: ", len(companion), "-", companion
        print " -- loyal: ", len(loyal), "-", loyal
        print "total =", len(breakdown["bestiary"])
        print

    def __parse_bestiary_page(self, html):
        """
        Given html, find an parse out all familiar.  Store in self.bestiary.
        Store id, img_src, name, and loyalty of each beast found.

        :param string html:
        :return: None
        """
        this_page_beasts = []
        soup = BeautifulSoup(html, "html.parser")
        main_div = soup.select("#super-container")[0]
        this_div = list(main_div.children)[-2].find("div")

        # loop through each span, which contains 1 beast each
        for span in this_div.find_all("span"):
            kids = list(span.children)
            if len(kids) == 1 and type(kids[0]) is NavigableString:
                continue

            result = self.__parse_beast_span(span)

            if result["id"] and result["name"]:
                this_page_beasts.append(result)
            elif result["id"] and not result["name"]:
                self.error("Error: Parsed out id, but not name - " +
                           HTMLParser().unescape(span.text))

        return this_page_beasts

    def __parse_beast_span(self, span):
        """
        Examine the span & its children to get relevant information about beast
        (Split out from self.__parse_bestiary_page()
        because breaking out of an inner for-loop,
         inside a for-loop, is a pain.)
        :param Tag span:
        :return: parsed results of beast_id, name, loyalty, & src
        :rtype: dict
        """
        beast_id = ""
        name = ""
        loyalty = ""
        src = ""

        # loop through the divs of the span, which could have:
        # img w/ id, name, description, status images, loyalty text
        for div in span.children:
            if type(div) == NavigableString:
                continue

            img = div.find(self.__locate_beast_image)
            if img:
                src = img.attrs["src"]
                match = re.search(self.img_patt, src)
                beast_id = match.group("beast_id") if match else beast_id
                continue

            # name
            txt = HTMLParser().unescape(div.text)
            match = re.search(self.name_patt, txt)
            if match:
                name = match.group("name")
                continue

            # loyalty
            match = re.search(self.loyalty_patt, txt)
            if match:
                loyalty = match.group("loyalty")

        return {
            "id": beast_id,
            "name": name,
            "loyalty": loyalty,
            "src": src
        }

    def get_beast_by_id(self, beast_id, key=None):
        """
        Searches all beasts and returns the dict of the beast_id
        :param string beast_id: id of familiar to find
        :param string key: key used to limit how much to search, will accept
            "taming", "awakened", "locked" - the keys of
            self.bestiary_breakdown
        :return: dict of the familiar
        :rtype: dict
        """
        if key and key in self.beasts_breakdown:
            to_search = self.beasts_breakdown[key]
        else:
            to_search = self.beasts
        return next((beast for beast in to_search
                     if beast["id"] == beast_id), {})

    def get_beast_name_by_id(self, beast_id, key=None):
        """
        Uses self.get_beast_by_id and returns just the name of beast
        :param string beast_id: id of familiar to find
        :param string key: key used to limit how much to search, will accept
            "taming", "awakened", "locked" - the keys of
            self.bestiary_breakdown
        :return: name of the familiar
        :rtype: string
        """
        return self.get_beast_by_id(beast_id, key).get("name", "")

    @staticmethod
    def __locate_beast_image(tag):
        """ Given a tag, see if it matches the specifications

        :param Tag tag:
        :return: True/False
        :rtype: bool
        """
        return tag.has_attr("width") and tag.has_attr("height")
