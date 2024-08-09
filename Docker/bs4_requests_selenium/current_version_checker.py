import bs4
import requests
import selenium
import sys

print('Python version:', sys.version.split(' ')[0])
print('Selenium version:', selenium.__version__)
print('Requests version:', requests.__version__)
print('BeautifulSoup version:', bs4.__version__)

from bs4 import BeautifulSoup

# Access a web page
# https://mygamatoto.com/
page_url = 'https://mygamatoto.com/allcats'

page = requests.get(page_url)
soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())
print('Bs4 and Req okiee. That was the html for https://mygamatoto.com/allcats.')