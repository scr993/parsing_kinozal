from bs4 import BeautifulSoup
import requests
url = 'https://kinozal-tv.appspot.com'

request = requests.get(url)
soup = BeautifulSoup(request.text. "html.parser")
print(soup)