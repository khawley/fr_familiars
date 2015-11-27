#! /bin/python
from MyCurl import MyCurl
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import re
import sys
from HTMLParser import HTMLParser

my_fr_cookie = 'Cookie: PHPSESSID=askldfjlkanfln; userid=alsdflanf; ' \
               'user_key=1234567890; username=test;'


class Bestiary:
    """
    Class to curl bestiary pages and return results of beasts
    """
    img_patt = re.compile(r'\/(?P<beast_id>[\d]+)(?:_gray)?\.png')
    name_patt = re.compile(r'^\n(?P<name>[\w\s\-\'\*]+)\n'
                           r'(?P<description>(?:\n|.)*)\n$', re.UNICODE)
    loyalty_patt = re.compile(r'^(?P<loyalty>[\w]+)$')
    beasts = []
    base_url = "http://flightrising.com/main.php?" \
               "p=bestiary&tab=familiars&page="

    def __init__(self, pages=None, fr_cookie=None):
        """
        :param int pages: Number of pages from 1 to 'pages' to parse
        :param fr_cookie: Cookie that has login information
        :return:
        """
        self.pages = pages or 43
        self.fr_cookie = fr_cookie or my_fr_cookie

    def get_list(self):
        """Curl and then parse all bestiary pages, returning results.

        :return: list of dicts, of all beasts
        :rtype: list
        """
        # must have User-Agent set
        send_headers = [
            'Accept-Language: en-US,en;q=0.8',
            'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
            'Upgrade-Insecure-Requests: 1',
            'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            self.fr_cookie,
        ]
        for i in range(1, self.pages + 1):
            url = self.base_url + str(i)
            print "curling " + url,
            html = MyCurl.curl(url, send_headers)
            # html = open("bestiary_response.html")
            print " -- parsing"
            self.__parse_html(html)
        return self.beasts

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
            src= ""

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
