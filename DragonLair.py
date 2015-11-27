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

    def __init__(self, lair_id, verbose=False):
        """
        :param lair_id:
        :param verbose:
        :return:
        """
        self.lair_id = lair_id
        self.verbose = verbose

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
