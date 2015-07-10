import requests

r = requests.get('http://inlandempire.craigslist.org/search/cta')

string = r.text
tag = '</p>'
index = string.find('<p')
index1 = string.rfind(tag)
print index
print index1
string = string[index:index1+len(tag)]
block =[]
block.append(string)
print block[0]
