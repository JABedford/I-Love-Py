# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
quote_page = 'destination url'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)


# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

#######Start to extract the data!#######

# Take out the <div> of name and get its value
name_box = soup.find('h1', attrs={'class': 'name'})

name = name_box.text.strip() # strip() is used to remove starting and trailing
print name

# get the index price
price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print price

import csv
from datetime import datetime

# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow([name, price, datetime.now()])

  
  
