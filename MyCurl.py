import pycurl
import re
from StringIO import StringIO
from urllib import urlencode


class MyCurl:
    headers = {}
    def __init__(self):
        pass
        # self.url = url
        # self.send_headers = send_headers
        # self.post_data = post_data or {}
        # self.verbose = verbose

    @classmethod
    def curl(cls, url, send_headers=None, post_data=None, verbose=False):
        response_buffer = StringIO()

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
        # c.setopt(c.HEADERFUNCTION, cls.__header_function)
        if verbose:
            c.setopt(c.VERBOSE, True)
        c.perform()
        c.close()

        encoding = None
        if 'content-type' in cls.headers:
            content_type = cls.headers['content-type'].lower()
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
        # Header lines include the trailing newline, and there may be whitespace
        # around the colon.
        name = name.strip()
        value = value.strip()

        # Header names are case insensitive.
        # Lowercase name here.
        name = name.lower()

        # Now we can actually record the header name and value.
        self.headers[name] = value