#python 2.7.6
#CLIENT 
#ask user for page adress and `pull HTML webpage for parsing

import sys
import requests
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from CL_utils import getHTMLblocks
from CL_utils import findVehicleandPrice
from CL_utils import getLink
from CL_utils import getHTML

block_array = []
HTMLfile = open('html.txt', 'r') #contains the html requests by FILENAME in request_html.txt
s = HTMLfile.read()
HTMLfile.close()
block_array = getHTMLblocks(s, '<p', '</p>') #contains html for individual postings

list_of_links = []
for block in block_array:
	list_of_links.append("inlandempire.craigslist.org" + getLink(block))

html = getHTML(list_of_links)


