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

html_atag = """<html><body><p>Test html a tag example</p>
<a href="http://www.packtpub.com">Home</a>
<a href="http;//www.packtpub.com/books">Books</a>
</body>
</html>"""
soup = BeautifulSoup(html_atag,'lxml')
atag = soup.a
print(atag['href'])
print(atag.attrs)
print(atag)
print(type(atag))
print(atag.name)
atag.name='agniv'
print(soup)
print("----------------")
first_a_string = atag.string
print(type(first_a_string))
print(first_a_string)
