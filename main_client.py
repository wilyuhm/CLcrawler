#python 2.7.6
#CLIENT 
#ask user for page adress and `pull HTML webpage for parsing

import sys
import time
from CL_utils import getHTMLblocks
from CL_utils import getVehiclePrice
from CL_utils import getVehicleName
from CL_utils import getLink
from CL_utils import getHTML
from collections import defaultdict

start = time.time()

HTMLfile = open('html.txt', 'r') 
s = HTMLfile.read()
HTMLfile.close()

block_array = []
block_array = getHTMLblocks(s, '<p', '</p>') #contains html for individual postings

list_of_links = []
for block in block_array:
	linkend = getLink(block)
	if linkend != '-1':
		list_of_links.append("http://inlandempire.craigslist.org" + getLink(block))

listings = []
numlinks = 1 
for link in list_of_links:
	print 'Link ' + str(numlinks) + ' of ' + str(len(list_of_links))
	numlinks = numlinks+1
	if link != 'NO LINK':
		html = getHTML(link)
		price = getVehiclePrice(html)
		name = getVehicleName(html).lower()
		listings.append( (name, price, link) )

stats_dict = defaultdict(list) 
for name, price, link in listings:
	stats_dict[name].append(price)

for k, v in stats_dict.items():
	print k
	for i in v:
		print i 

end = time.time()
print 'Total elapsed time for results: ' + str(end-start)
