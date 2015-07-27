#python 2.7.6
#CLIENT 
#UDP socket
#ask user for page adress and `pull HTML webpage for parsing

import sys
sys.dont_write_bytecode=True
from collections import defaultdict
from CL_utils import getHTMLblocks
from CL_utils import getLink
from CL_utils import findVehicleandPrice


HTMLfile = open('html.txt', 'r') #contains the html requests by FILENAME in request_html.txt
s = HTMLfile.read()
HTMLfile.close()

block_array = []
block_array = getHTMLblocks(s, '<p', '</p>') #contains html for individual postings

listings = []
for block in block_array:
	vehicle, price, link = findVehicleandPrice(block)
	if price > 0: #people suck and list at $0
		listings.append( (vehicle, price, link) )

stats_dict = defaultdict(list)
for listing in listings: #listing contains (year+make+model, price, link)
	if listing[0] != ' ':
		stats_dict[listing[0]].append( (listing[1], listing[2]) )

#calculate average
filtered_dict = defaultdict(list)
for make, tups in stats_dict.items(): #tups contains list of tuples of (price, link) for particular type
	low_price=(tups[0][0], tups[0][1]) #lowest price for particular year, make, model
	avg_price=0
	index=0
	for price, link in tups:
		avg_price += price
		if price < low_price[0]:
			low_price = (price, link)
		index+=1
	else:
		avg_price /= (index)

	savings=(100.0-((100.0*low_price[0])/avg_price))
	if savings > 0.0:
		filtered_dict[make]=[make, avg_price,low_price[0],"%.2f" % savings]
		
filtered_dict = sorted(filtered_dict.iteritems(), key=lambda(k, v): v[0], reverse=False)
#filtered_dict = sorted(filtered_dict.iteritems(), key=lambda(k, v): v[3], reverse=True) #sort by savings
for item in filtered_dict:
	print item

