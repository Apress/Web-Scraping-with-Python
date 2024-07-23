import requests

# Make a GET request

r = requests.get("http://www.vulnweb.com")

# print request object

print(r.url)

# print status code
# status code 200 means success

print(r.status_code)
