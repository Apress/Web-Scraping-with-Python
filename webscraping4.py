import requests
from bs4 import BeautifulSoup

#make a get request
r = requests.get("http://www.vulnweb.com")

# parse html
soup = BeautifulSoup(r.content, 'html.parser')

#get the title tag
print(soup.title)

#name of the tag
print(soup.title.name)

#get the name of parent tag
print(soup.title.parent.name)