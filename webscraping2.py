from bs4 import BeautifulSoup
import requests
url="http://vulnweb.com"
r=requests.get(url)
Soup=BeautifulSoup(r.content, 'html5lib')
print(Soup.prettify())