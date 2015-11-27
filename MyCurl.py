import pycurl
import re
from StringIO import StringIO


class MyCurl:
    def __init__(self, url, send_headers=[], post_data={}, verbose=False):
        self.headers = {}
        self.url = url
        self.send_headers = send_headers
        self.post_data = post_data
        self.verbose = verbose

    def curl(self):#,url, send_headers=[], post_data={}, verbose=False):
        buffer = StringIO()

        c = pycurl.Curl()
        c.setopt(pycurl.URL, self.url)
        c.setopt(pycurl.HTTPHEADER, self.send_headers)
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.HEADERFUNCTION, self.header_function)
        if self.verbose:
            c.setopt(c.VERBOSE, True)
        c.perform()
        c.close()

        encoding = None
        if 'content-type' in self.headers:
            content_type = self.headers['content-type'].lower()
            match = re.search('charset=(\S+)', content_type)
            if match:
                encoding = match.group(1)
        else:
            encoding = 'iso-8859-1'

        body = buffer.getvalue()
        # Decode using the encoding we figured out.
        return body.decode(encoding)

    def header_function(self, header_line):
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