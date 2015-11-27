#! /bin/python
import pycurl
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import re
import sys
from HTMLParser import HTMLParser

try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

hparser = HTMLParser()
img_patt = re.compile(r'\/(?P<beast_id>[\d]+)(?:_gray)?\.png')
name_patt = re.compile(r'^\n(?P<name>[\w\s\-\'\*]+)\n(?P<description>(?:\n|.)*)\n$', re.UNICODE)
loyalty_patt = re.compile(r'^(?P<loyalty>[\w]+)$')
def main():
    global beasts
    beasts = []
    for i in range(1, 44):
        url = "http://flightrising.com/main.php?p=bestiary&tab=familiars&page="+str(i)
        print "curling " + url,
        html = curl(url)
        # html = open("bestiary_response.html")
        print " -- parsing"
        parse_html(html)

    print beasts


def parse_html(html):
    global beasts, hparser
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
        # img w/ id
        # name
        # description
        # status images (caught, etc)
        # loyalty text
        for div in span.children:
            if type(div) == NavigableString:
                continue

            img = div.find(locate_beast_image)
            if img:
                src = img.attrs["src"]
                match = re.search(img_patt, src)
                beast_id = match.group("beast_id") if match else beast_id
                continue
            
            # name
            txt = hparser.unescape(div.text)
            match = re.search(name_patt, txt)
            if match:
                name = match.group("name")
                continue

            # loyalty
            match = re.search(loyalty_patt, txt)
            if match:
                loyalty = match.group("loyalty")

        if beast_id and name:
            beasts.append({
                "id": beast_id,
                "src": src,
                "name": name,
                "loyalty": loyalty
            })
        elif beast_id and not name:
            sys.stderr.write("Error: Parsed out id, but not name - " + hparser.unescape(span.text))


def locate_beast_image(tag):
    return tag.has_attr("width") and tag.has_attr("height")


def header_function(header_line):
    # HTTP standard specifies that headers are encoded in iso-8859-1.
    # On Python 2, decoding step can be skipped.
    header_line = header_line.decode('utf-8')

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
    headers[name] = value


def curl(url):
    global headers
    headers = {}

    buffer = BytesIO()
    send_headers = [
        # 'Accept-Encoding: gzip, deflate, sdch',
        'Accept-Language: en-US,en;q=0.8',
        'Upgrade-Insecure-Requests: 1',
        'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
        'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Cookie: PHPSESSID=askldfjlkanfln; userid=alsdflanf; user_key=1234567890; username=test;',
        # 'Connection: keep-alive'
    ]

    c = pycurl.Curl()
    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.HTTPHEADER, send_headers)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.HEADERFUNCTION, header_function)
    # c.setopt(c.VERBOSE, True)
    c.perform()
    c.close()

    # Figure out what encoding was sent with the response, if any.
    # Check against lowercased header name.
    encoding = None
    if 'content-type' in headers:
        content_type = headers['content-type'].lower()
        match = re.search('charset=(\S+)', content_type)
        if match:
            encoding = match.group(1)
            # print('Decoding using %s' % encoding)
    if encoding is None:
        # Default encoding for HTML is iso-8859-1.
        # Other content types may have different default encoding,
        # or in case of binary data, may have no encoding at all.
        encoding = 'iso-8859-1'
        # print('Assuming encoding is %s' % encoding)

    body = buffer.getvalue()
    # Decode using the encoding we figured out.
    return body.decode(encoding)

main()

