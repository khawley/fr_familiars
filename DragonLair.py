from MyCurl import MyCurl
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import re
import sys
from HTMLParser import HTMLParser


class DragonLair:
    """
    Class to list all dragons in lair, and associated familiars
    """

    #regex globals
    dragon_url_patt = re.compile(r'main\.php\?p=lair(?:&|&amp;)id=95470'
                                 r'(?:&|&amp;)tab=dragon(?:&|&amp;)'
                                 r'did=(?P<dragon_id>\d+)')
    familiar_equipped_patt = re.comiple(r'/images/icons/famicon.png')

    lair_max_page = 1

    def __init__(self, lair_id, fr_cookie, verbose=False):
        """
        :param string lair_id: Id of dragon lair
        :param string fr_cookie: Cookie that has login information
        :param bool verbose: Whether to print progress
        :return:
        """
        self.lair_id = str(lair_id)
        self.fr_cookie = fr_cookie
        self.verbose = verbose
        self.send_headers = [
            'Accept-Language: en-US,en;q=0.8',
            'User-Agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
            'Upgrade-Insecure-Requests: 1',
            'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            self.fr_cookie,
        ]
        self.lair_url = "http://flightrising.com/main.php?p=lair&id=" +\
                        self.lair_id + "&page="
        self.dragon_url = "http://flightrising.com/main.php?p=lair&id=" + \
                          self.lair_id + "&tab=dragon&did="

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

    def get_list(self):
        i = 1
        while i <= self.lair_max_page:
            html = MyCurl.curl(self.lair_url, self.send_headers)
            self.__parse_lair_page(html)
            i += 1
        pass

    def __parse_lair_page(self, html):

        soup = BeautifulSoup(html, "html.parser").select("#super-container")[0]

        if self.lair_max_page == 1:
            # may not have been set, go find it in the page
            self.lair_max_page = max([int(i) for i in
                                      re.findall(r'(\d+)',
                                                 soup.find_all("div")[4].text)])

        dragon_cards = soup.select(".dragoncard")

        if len(dragon_cards) != 15:
            sys.stderr.write("Error: Something happened, did not find 15 dragons on page")

        for dragon_card in dragon_cards:
            a_tag = dragon_card.find("a")
            match = re.search(self.dragon_url_patt, a_tag.attrs["href"])
            if match:
                dragon_id = match.group("dragon_id")

            if dragon_card.selector(".loginbar")[0]\
                .find(self.__locate_familiar_equipped_img()):
                has_familiar = True



        pass

    def __locate_familiar_equipped_img(self, tag):
        return tag.has_attr("src") and \
               re.search(self.familiar_equipped_patt, tag.attrs["src"])
