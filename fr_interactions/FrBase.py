import sys
import pycurl
import re
from StringIO import StringIO
from urllib import urlencode


class FrBase(object):
    response_headers = {}

    def __init__(self, fr_cookie, verbose=False):
        self.fr_cookie = fr_cookie
        self.verbose = verbose

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
        if self.verbose or verbose:
            sys.stdout.write(msg)

    def error(self, msg, newline=False, verbose=False):
        """
        If verbose, print the msg to stderr.
        :param string msg: String to be printed
        :param bool newline: Whether to add a newline after msg
        :param bool verbose: whether to actually print
        :return:
        """
        if newline:
            msg += "\n"
        if self.verbose or verbose:
            sys.stderr.write(msg)

    def curl(self, url, send_headers=None, post_data=None, verbose=False):
        response_buffer = StringIO()
        self.response_headers = {}

        c = pycurl.Curl()
        c.setopt(pycurl.URL, url)
        if send_headers:
            c.setopt(pycurl.HTTPHEADER, send_headers)
        if post_data and type(post_data) is dict:
            # post_data = {'field': 'value'}
            # Form data must be provided already urlencoded.
            postfields = urlencode(post_data)
            # Sets request method to POST,
            # Content-Type header to application/x-www-form-urlencoded
            # and data to send in request body.
            c.setopt(c.POSTFIELDS, postfields)
        c.setopt(c.WRITEDATA, response_buffer)
        c.setopt(c.HEADERFUNCTION, self.__header_function)
        if verbose:
            c.setopt(c.VERBOSE, True)
        c.perform()
        c.close()

        encoding = None
        if 'content-type' in self.response_headers:
            content_type = self.response_headers['content-type'].lower()
            match = re.search('charset=(\S+)', content_type)
            if match:
                encoding = match.group(1)
        else:
            encoding = 'iso-8859-1'

        body = response_buffer.getvalue()
        # Decode using the encoding we figured out.
        return body.decode(encoding)

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