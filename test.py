"""This is a test function
Source code:
http://stackoverflow.com/questions/2081586/web-scraping-with-python
"""

import urllib2
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen(\
        'http://www.timeanddate.com/worldclock/astronomy.html?n=78').read())

# Get Data and Sunrise data
for row in soup('table',{'class':'spad'})[0].tbody('tr'):
    tds = row('td')
    print tds[0].string, tds[1].string

