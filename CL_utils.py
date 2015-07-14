#given a block of HTML text
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


#pass in HTML object code, find the price
#returns price
def getVehiclePrice(text):
	identifyer = '<span class="price">$'
	price =''
	priceindex = text.find(identifyer) + len(identifyer)
	if priceindex:
		price = text[priceindex:text.find('<', priceindex)]
	else:
		price = -1
	try: 
		price = int(price)
	except:
		price = -1
	return int(price)

def getVehicleName(text):
	identifier = 'class="attrgroup"><span><b>'
	name = ''
	nameindex = text.find(identifier) + len(identifier)
	if nameindex:
		name = text[nameindex:text.find('<', nameindex)]
	else:
		name = 'Unrecognized name'
	return str(name)
 
#given block of html
#return link for that page
def getLink(HTML_block):
	indentifyer = 'href="'
	startindex = HTML_block.rfind(indentifyer)
	if startindex == -1:
		return '-1'
	endindex = HTML_block.find('"', startindex+22)
	return HTML_block[startindex+len(indentifyer):endindex]

import requests
#use requests to get HTML at URL
def getHTML(url):
	html = requests.get(url)
	return html.text
