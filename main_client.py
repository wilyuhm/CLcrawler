#python 2.7.6
#CLIENT 
#ask user for page adress and `pull HTML webpage for parsing

import sys
import requests
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from CL_utils import getHTMLblocks
from CL_utils import findVehiclePrice
from CL_utils import getLink
from CL_utils import getHTML

block_array = []
HTMLfile = open('html.txt', 'r') #contains the html requests by FILENAME in request_html.txt
s = HTMLfile.read()
HTMLfile.close()
block_array = getHTMLblocks(s, '<p', '</p>') #contains html for individual postings

list_of_links = []
for block in block_array:
	linkend = getLink(block)
	if linkend != 'NO LINK':
		list_of_links.append("http://inlandempire.craigslist.org" + getLink(block))

listings = []
numlinks = 0
nolinks = 0
for link in list_of_links:
	print 'Link ' + str(numlinks) + ' of ' + str(len(list_of_links))
	numlinks = numlinks+1
	if link != 'NO LINK':
		html = getHTML(link)
		price = findVehiclePrice(html)
		listings.append( (link, price) )
	else:
		nolinks = nolinks + 1
for listing in listings:
	print listing
