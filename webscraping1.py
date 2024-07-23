import requests
URL = "http://vulnweb.com"
r = requests.get(URL)
print(r.content)