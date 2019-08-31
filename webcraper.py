from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
  #html = urlopen('http://pythonscraping.com/pages/page1.html')
  html = urlopen('http://localhost')

except HTTPError as e:
  print(e)
except URLError as e:
  print(e)
else:
  bs = BeautifulSoup(html.read(),'html.parser')
try:
  print(bs.nonExistantTag123.sometag)
except AttributeError as e:
  print(e)
  print(bs.h1)
