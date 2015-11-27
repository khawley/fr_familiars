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
        pass
