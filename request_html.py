#Grab HTML from given URL and send output to FILENAME

import requests
import time

start = time.time()
URL = 'http://inlandempire.craigslist.org/search/cto?s='
FILENAME = 'html.txt'
NUMRESULTS = 2400 #Max 2400
NUMPAGES = NUMRESULTS/100 + 1
#Craigslist allows a max of 2500 search results with 100 results per page

currpage=1
print 'Getting page ' + str(currpage) + ' of ' + str(NUMPAGES) + '...'
listingnumber = 0
curr_URL = URL + str(listingnumber)
r = requests.get(curr_URL)
currpage+=1
f = open(FILENAME, 'w')
f.write(r.text.encode('utf-8'))
f.close()

f = open(FILENAME, 'a')
listingnumber = 100
if NUMRESULTS>2400:
	NUMRESULTS=2400
while(listingnumber <= NUMRESULTS):
	curr_URL = URL + str(listingnumber)
	print 'Getting page ' + str(currpage) + ' of ' + str(NUMPAGES) + '...'
	currpage+=1
	r = requests.get(curr_URL)
	f.write(r.text.encode('utf-8'))
	listingnumber = listingnumber + 100
f.close()
end = time.time()
print 'Total elapsed time to get page(s): ' + str(end-start) 
