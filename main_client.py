#python 2.7.6
#CLIENT 
#UDP socket
#ask user for page adress and `pull HTML webpage for parsing

import sys
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#return all text between tags, including tags
def getHTMLblocks(text, starttag, endtag):
	index = text.find(starttag)
	end_index = text.rfind(endtag)
	text = text[index:end_index+len(endtag)]
	block_array = []
	index = text.find(starttag)
	while index != -1 and end_index != -1:	
		end_index = text.find(endtag)
		block_array.append(text[index:end_index+len(endtag)])
		text = text[end_index+len(endtag):]
		index = text.find(starttag)
	return block_array

block_array = []
HTMLfile = open('html.txt', 'r') #contains the html requests by FILENAME in request_html.txt
s = HTMLfile.read()
HTMLfile.close()
block_array = getHTMLblocks(s, '<p', '</p>') #contains html for individual postings

#pass in HTML object code, find and match vehicle to a manufacturer and find the price
#returns a tuple (vehicle, price)

def findVehicleandPrice(text):
	manu_list = []
	manufacturers = open('manufacturers.txt')	
	manu_list = [line.rstrip('\n') for line in manufacturers]
	manufacturers.close()

	foundmake = 0
	year = ''
	make = ''
	model = ''
	price ='' 
	prevword = text.split(' ')
	for word in text.split(' '): #get make and model
		if foundmake:
			model = word.replace('</a>','')
			break
		for manu in manu_list:
			if fuzz.ratio(word.lower(), manu) > 90:
				foundmake = 1
				make = manu
				break
		if foundmake==0:
			prevword = word
	if foundmake:
		year = prevword.replace('class="hdrlnk">', '')

	vehicle = year + ' ' + make.lower() + " " + model.lower()
	priceindex = text.rfind('<span class="price">&#x0024;') + 28
	if priceindex:
		price = text[priceindex:text.find('<', priceindex, priceindex+7)]
	if len(price) > 6:
		price = '0'
	return (vehicle, int(price))

listings = []
for block in block_array:
	listings.append(findVehicleandPrice(block))
for l in listings:
	print l

