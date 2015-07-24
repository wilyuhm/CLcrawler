#Grab HTML from given URL and send output to FILENAME

import requests
import time

start = time.clock()

URL = 'http://inlandempire.craigslist.org/search/cto?s='
FILENAME = 'html.txt'
NUMRESULTS = 100

r = requests.get(URL+str(NUMRESULTS-100))

f = open(FILENAME, 'w')
f.write(r.text.encode('utf-8'))
f.close()

end = time.clock()
print 'Total elapsed time to get page: ' + str(end-start)
