import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com/"
html = urlopen(url)
soup = BeautifulSoup(html,"lxml")
print(soup)
