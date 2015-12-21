import sys
import re
import requests
from StringIO import StringIO
from urllib import urlencode
from bs4 import BeautifulSoup


class FrBase(object):
    response_headers = {}
    __is_logged_in = None

    def __init__(self, fr_cookie, verbosity=0):
        """

        :param string fr_cookie: Cookie that has login information
        :param int verbosity: How verbose to be:
            0 - do not print echo statements
            1 - print echo statements
            2 - print echo + curl statements
        :return:
        """
        self.fr_cookie = fr_cookie
        self.verbosity = verbosity

        # must have User-Agent set
        self.send_headers = [
            'Origin: http://flightrising.com',
            'Accept-Language: en-US,en;q=0.8',
            'User-Agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
            'Content-Type: application/x-www-form-urlencoded; charset=UTF-8',
            'Upgrade-Insecure-Requests: 1',
            'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            self.fr_cookie,
        ]

    def echo(self, msg, newline=False, verbose=False):
        """
        If verbose, print the msg to stdout.
        :param string msg: String to be printed
        :param bool newline: Whether to add a newline after msg
        :param bool verbose: whether to actually print
        :return:
        """
        if newline:
            msg += "\n"
        if self.verbosity or verbose:
            sys.stdout.write(msg)

    @staticmethod
    def error(msg, newline=False):
        """
        If verbose, print the msg to stderr.
        :param string msg: String to be printed
        :param bool newline: Whether to add a newline after msg
        :return:
        """
        if newline:
            msg += "\n"
        sys.stderr.write(msg)

    def curl(self, url, send_headers=None, post_data=None, verbose=False):
        """
        Originally a function using pycurl, it has been repurposed to use the
        requests library.
        :param str url:
        :param dict send_headers: dict of headers, {"name": "value"} to send
        :param dict post_data: dict of post data, {"name": "value"} to send
        :param bool verbose: deprecated variable
        :return: html response
        :rtype: str
        """

        # if passing in deprecated list, convert to dict
        if type(send_headers) is list:
            # parse out the type by the colon
            send_headers = {item.split(":")[0]: item.split(":")[1].strip()
                            for item in send_headers}

        if post_data:
            response = requests.post(url, headers=send_headers, data=post_data)
        else:
            response = requests.get(url, headers=send_headers)

        if not response.ok:
            self.error("Failed to make request to " + url, True)
            exit()

        return response.text

    def __header_function(self, header_line):
        # Header lines include the first status line (HTTP/1.x ...).
        # We are going to ignore all lines that don't have a colon in them.
        # This will botch headers that are split on multiple lines...
        if ':' not in header_line:
            return

        # Break the header line into header name and value.
        name, value = header_line.split(':', 1)

        # Remove whitespace that may be present.
        # Header lines include the trailing newline,
        # and there may be whitespace around the colon.
        name = name.strip()
        value = value.strip()

        # Header names are case insensitive.
        # Lowercase name here.
        name = name.lower()

        # Now we can actually record the header name and value.
        self.response_headers[name] = value

    def is_logged_in(self, html):
        """
        If not confirmed previously, check the html for the lack of #loginbar
        in the #usertab.  If found, the cookie is not valid.  Check that cookie
        like expected for the 'www.flightrising.com' domain.
        Sets self.__is_logged_in when no #loginform is found.
        :param str html: html from a query to request to flightrising
        :return: True/False if logged
        :rtype: bool
        """

        # have already established that the cookie is valid & user is logged in
        if self.__is_logged_in is not None:
            return self.__is_logged_in

        # start with True, switch to False when proven wrong
        self.__is_logged_in = True

        soup = BeautifulSoup(html, "html.parser")
        # html is actually a bit broken, so can't just search for #usertab :(
        usertabs = [div for div in soup.find_all("div")
                    if div.attrs.get("id", "") == "usertab"]
        usertab = usertabs.pop() if usertabs else None

        if not usertab:
            # maybe it was renamed?
            self.error("Cannot locate #usertab, may not be logged in.")
            self.__is_logged_in = False

        form = usertab.find("form") if usertab else None
        if form and form.attrs.get("id", "") == "loginform":
            # loginform was found, cookie is bad...
            self.error("You are not logged in.  Please check your cookie.",
                       True)
            # check cookie for PHPSESSID
            if "PHPSESSID" not in self.fr_cookie \
                    and "fr_session" in self.fr_cookie:
                self.error("Please confirm that you are using a cookie from "
                           "flightrising.com, and not www1.flightrising.com",
                           True)
            self.__is_logged_in = False

        # else
        # found usertab, did not find loginbar.  You're logged in
        return self.__is_logged_in
