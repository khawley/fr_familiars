from bs4 import BeautifulSoup
import re

from .FrBase import FrBase


class DragonLair(FrBase):
    """
    Class to list all dragons in lair, and associated familiars
    """

    # regex globals
    lair_url_patt = re.compile(r'main\.php\?p=lair(?:&|&amp;)id=(?:\d+)'
                               r'(?:&|&amp;)page=(\d+)')
    dragon_url_patt = re.compile(r'main\.php\?p=lair(?:&|&amp;)id=(?:\d+)'
                                 r'(?:&|&amp;)tab=dragon(?:&|&amp;)'
                                 r'did=(?P<dragon_id>\d+)')
    familiar_equipped_patt = re.compile(r'/images/icons/famicon\.png')
    familiar_img_patt = re.compile(r'familiar/(?:\w+)/'
                                   r'(?P<familiar_id>\d+)\.png')

    lair_max_page = 1
    dragons = []

    def __init__(self, lair_id, fr_cookie, verbosity=False):
        """
        :param string lair_id: Id of dragon lair
        :param string fr_cookie: Cookie that has login information
        :param int verbosity: How verbose to be:
            0 - do not print echo statements
            1 - print echo statments
            2 - print echo + curl statements
        :return:
        """
        FrBase.__init__(self, fr_cookie, verbosity)
        self.lair_id = str(lair_id)

        self.lair_url = "http://flightrising.com/main.php?p=lair&id=" + \
                        self.lair_id + "&page="
        self.dragon_url = "http://flightrising.com/main.php?p=lair&id=" + \
                          self.lair_id + "&tab=dragon&did="

    def get_list(self):
        """
        Crawl & parse each page of dragon lair, until reaches an
        empty dragon space.
        :return: list of dragons
        :rtype: list
        """
        self.dragons = []  # do not want to add the results in twice
        i = 1
        while i <= self.lair_max_page:
            self.echo("+ curling lair page: " + str(i))
            html = self.curl(self.lair_url + str(i), self.send_headers)
            self.echo(" - parsing lair page", True)
            if not self.__parse_lair_page(html):
                break
            i += 1

        return self.dragons

    def __parse_lair_page(self, html):
        """
        Parse the lair page for each dragon found.  If it has a familiar
        equipped, then crawl that dragon's page to get info on the familiar.
        Appends all results to self.dragons
        :param string html: html of the lair page
        :return: True/False whether there are more dragons after
            the current page
        :rtype: bool
        """
        soup = BeautifulSoup(html, "html.parser")

        if self.lair_max_page == 1:
            # may not have been set if first call, go find it in the page
            paging_tags = soup.find_all(
                self.__locate_lair_paging_urls)
            self.lair_max_page = max([int(i.text) for i in paging_tags
                                      if i.text])

        dragon_cards = soup.select(".dragoncard")

        if len(dragon_cards) != 15:
            self.error("Error: Something happened, did not find 15"
                       " dragons on page")

        for dragon_card in dragon_cards:
            result = {}

            a_tag = dragon_card.find("a")
            if not a_tag:
                # no more dragons on the page, or the next pages, exit back
                return False
            match = re.search(self.dragon_url_patt, a_tag.attrs["href"])
            if match:
                result["dragon_id"] = match.group("dragon_id")
                self.echo("-- found dragon_id: " +
                          str(result["dragon_id"]), True)

            loginbars = dragon_card.select(".loginbar")
            if result["dragon_id"] and loginbars:
                for tag in loginbars:
                    if not result.get("familiar_id") and \
                            tag.find(self.__locate_familiar_equipped_img):
                        result["familiar_id"] = self.__get_dragon_familiar_id(
                            result["dragon_id"])

            if result:
                self.dragons.append(result)

        return True

    def __get_dragon_familiar_id(self, dragon_id):
        """
        Crawl and parse out the familiar that is attached to the given dragon
        :param string dragon_id: the dragon id to look for familiar
        :return: id of the found familiar
        :rtype: string
        """
        self.echo("---- curling dragon id: " + str(dragon_id))
        dragon_html = self.curl(self.dragon_url + str(dragon_id),
                                self.send_headers)
        self.echo(" -- parsing")
        fam_id = self.__parse_dragon_page(dragon_html)
        self.echo(" -- with familiar: " + str(fam_id), True)
        return fam_id

    def __parse_dragon_page(self, html):
        """
        Find the familiar attached on this page.
        :param string html: html of one dragon's page
        :return: familiar id or an empty string
        :rtype: string
        """
        soup = BeautifulSoup(html, "html.parser")
        for a_tag in soup.select("a.clueitem"):
            img = a_tag.find("img")
            if img:
                match = re.search(self.familiar_img_patt, img.attrs["src"])
                if match:
                    return match.group("familiar_id")

        return ""

    def __locate_lair_paging_urls(self, tag):
        """
        Given a tag from BeautifulSoup, determine if it's a tag with an href,
        and that href is a lair paging url.
        :param Tag tag:
        :return: True/False
        :rtype: bool
        """
        return tag.has_attr("href") and \
            re.search(self.lair_url_patt, tag.attrs["href"])

    def __locate_familiar_equipped_img(self, tag):
        """
        Given a tag from BeautifulSoup, determine if it has a src, and if
        that src matches the familiar equipped pattern.
        :param Tag tag:
        :return: True/False
        :rtype: bool
        """
        return tag.has_attr("src") and \
            re.search(self.familiar_equipped_patt, tag.attrs["src"])
