import requests
from bs4 import BeautifulSoup 

#r = requests.get('http://ufcstats.com/statistics/fighters?char=a')
#print(r.status_code)
#print(r.headers['content-type'])
#print(r.encoding)
#print(r.text)

#Trying to get every page now; payload provides dictionary of key value pairs to be passed for request

#creates list of Response objects, each object corresponds to first character of last name of fighters
alphabet  = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
pages = []
urls = []
content = []
URL_ROOT = 'http://ufcstats.com/statistics/fighters?char='
for c in alphabet:
	page = requests.get(URL_ROOT + c)
	pages.append(page)
	urls.append(URL_ROOT + c)
	content.append(page.content)
	
print(pages[0].headers)
#print('\n\n'+ str(content[0]))
soup = BeautifulSoup(content[0], 'html.parser')

print(soup.prettify())
print()
lister = soup.find_all('td')
for item in lister :
	aTag = item.find_all('a')
	if not aTag:
		print(item.contents)
	else:
		print (aTag)

#lister
#print (lister[0] + "\n\n" + lister[1] + "\n\n" + lister[2] + "\n\n" + lister[1])
#print(soup.td)
#print(soup.td.attrs)

 