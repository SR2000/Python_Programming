# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
ls = list()

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('Enter count: ')
pos = input('Enter position: ')
pos = int(pos)
count = int(count)
#html = urllib.request.urlopen(url, context=ctx).read()
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
print('Retrieving:',url)

# Retrieve all of the anchor tags
temp = 0
while temp != count:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    temp = temp + 1
    for tag in tags:
        ls.append(tag.get('href', None))
    url= (ls[pos - 1])
    ls = list()
    print('Retrieving:',url)
