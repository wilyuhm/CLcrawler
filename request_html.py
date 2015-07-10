#Grab HTML from given URL and send output to FILENAME

import requests

URL = 'http://inlandempire.craigslist.org/search/cta'
FILENAME = 'html.txt'

r = requests.get(URL)
f = open(FILENAME, 'w')
f.write(r.text.encode('utf-8'))
f.close()
