from MyCurl import MyCurl
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import re
import sys
from HTMLParser import HTMLParser


class Bestiary:
    """
    Class to curl bestiary pages and return results of beasts
    """
    img_patt = re.compile(r'\/(?P<beast_id>[\d]+)(?:_gray)?\.png')
    name_patt = re.compile(r'^\n(?P<name>[\w\s\-\'\*]+)\n'
                           r'(?P<description>(?:\n|.)*)\n$', re.UNICODE)
    loyalty_patt = re.compile(r'^(?P<loyalty>[\w]+)$')
    beasts = []
    beasts_breakdown = {}
    base_url = "http://flightrising.com/main.php?" \
               "p=bestiary&tab=familiars&page="

    def __init__(self, fr_cookie, pages=None, verbose=False):
        """
        :param string fr_cookie: Cookie that has login information
        :param int pages: Number of pages from 1 to 'pages' to parse
        :param bool verbose: Print status statements
        :return:
        """
        self.fr_cookie = fr_cookie
        self.pages = pages or 43
        self.verbose = verbose
        # must have User-Agent set
        self.send_headers = [
            'Accept-Language: en-US,en;q=0.8',
            'User-Agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
            'Upgrade-Insecure-Requests: 1',
            'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            self.fr_cookie,
        ]

    def echo(self, msg, newline=False):
        """If verbose, print the msg.

        :param string msg: String to be printed
        :param bool newline: Whether to add a newline after msg
        :return:
        """
        if newline:
            msg += "\n"
        if self.verbose:
            sys.stdout.write(msg)

    def get_all(self):
        """Curl and then parse all bestiary pages, returning results.

        :return: list of dicts, of all beasts
        :rtype: list
        """

        for i in range(1, self.pages + 1):
            self.__get_page(i)
        self.__breakdown_beasts()
        return self.beasts_breakdown

    def __get_page(self, page):
        """
        Internal function to get & parse the html from one page of the Bestiary
        :param int/string page:
        :return:
        """
        url = self.base_url + str(page)
        self.echo("curling " + url)
        html = MyCurl.curl(url, self.send_headers)
        # html = open("bestiary_response.html")
        self.echo(" -- parsing", True)
        self.__parse_html(html)

    def get_one_page(self, page):
        """
        Externally callable function to get one page of Bestiary and return
        the beasts_breakdown of that page (and any previously crawled pages)
        :param int/string page:
        :return: beasts_breakdown
        :rtype: dict of lists
        """
        self.__get_page(page)
        self.__breakdown_beasts()
        return self.beasts_breakdown

    def __breakdown_beasts(self):
        """Using self.beasts, determine awakened, locked, & taming.
        Write to self.beasts_breakdown.

        :return:
        """
        if not self.beasts:
            sys.stderr.write("Error: No bestiary to breakdown")
            return

        awakened = []
        locked = []
        taming = []

        for beast in self.beasts:
            loyalty = beast["loyalty"].lower()
            if loyalty == "awakened":
                awakened.append(beast)
            elif loyalty == "locked":
                locked.append(beast)
            else:
                taming.append(beast)

        if len(self.beasts) != \
                (len(locked) + len(awakened) + len(taming)):
            sys.stderr.write("Error!  Not adding up correctly!")

        self.beasts_breakdown = {
            "bestiary": self.beasts,
            "awakened": awakened,
            "locked": locked,
            "taming": taming
        }

    def print_beasts_breakdown(self):
        """Print the breakdown of awakened, locked, taming & total.

        :return:
        """
        if not self.beasts:
            self.get_all()

        # print stats
        print "locked: ", len(self.beasts_breakdown["locked"]),
        print " -", self.beasts_breakdown["locked"]
        print "awakened: ", len(self.beasts_breakdown["awakened"])
        print "taming: ", len(self.beasts_breakdown["taming"])
        print "total =", len(self.beasts)
        print

    def __parse_html(self, html):
        """
        Given html, find an parse out all familiar.  Store in self.bestiary.
        Store id, img_src, name, and loyalty of each beast found.

        :param string html:
        :return: None
        """
        soup = BeautifulSoup(html, "html.parser")
        main_div = soup.select("#super-container")[0]
        this_div = list(main_div.children)[-2].find("div")

        # loop through each span, which contains 1 beast each
        for span in this_div.find_all("span"):

            beast_id = None
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

            if beast_id and name:
                self.beasts.append({
                    "id": beast_id,
                    "src": src,
                    "name": name,
                    "loyalty": loyalty
                })
            elif beast_id and not name:
                sys.stderr.write("Error: Parsed out id, but not name - " +
                                 HTMLParser().unescape(span.text))

    @staticmethod
    def __locate_beast_image(tag):
        """ Given a tag, see if it matches the specifications

        :param Tag tag:
        :return: True/False
        :rtype: bool
        """
        return tag.has_attr("width") and tag.has_attr("height")
