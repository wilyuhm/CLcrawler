#Grab HTML from given URL and send output to FILENAME

import requests
import time

start = time.time()
URL = 'http://inlandempire.craigslist.org/search/cto?s='
FILENAME = 'html.txt'

#Craigslist allows a max of 2500 search results with 100 results per page
listingnumber = 0
curr_URL = URL + str(listingnumber)
r = requests.get(curr_URL)

f = open(FILENAME, 'w')
f.write(r.text.encode('utf-8'))
f.close()

f = open(FILENAME, 'a')
listingnumber = 100
while(listingnumber < 2500):
	r = requests.get(curr_URL)
	f.write(r.text.encode('utf-8'))
	listingnumber = listingnumber + 100
f.close()
end = time.time()
print 'Total elapsed time to get page: ' + str(end-start) 

