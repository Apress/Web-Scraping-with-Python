from bs4 import BeautifulSoup
import requests

url="https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"

result=requests.get(url)

doc = BeautifulSoup(result.content, 'html.parser')

result1 = doc.find_all(string = 'California')

print(result1)