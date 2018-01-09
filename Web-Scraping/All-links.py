#Download all links present from a HTML website.

import urllib2
import re

#connect to the destination 
website = urllib2.urlopen(url)

#read the code that is present
html = website.read()

#use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)

print links
