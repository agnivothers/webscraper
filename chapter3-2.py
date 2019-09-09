import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

with open("ecologicalpyramid.html","r") as ecological_pyramid:
  soup = BeautifulSoup(ecological_pyramid,"lxml")
tertiaryconsumers = soup.find_all(class_="tertiaryconsumerlist")
for tertiaryconsumer in tertiaryconsumers:
  parent_ul = tertiaryconsumer.find_parent("ul")
  #print(parent_ul)
  #print(tertiaryconsumer)
  #print(tertiaryconsumer.find_parent())
  #print(tertiaryconsumer.find_next_sibling())
  #print(tertiaryconsumer.find_previous_sibling())
  #print(tertiaryconsumer.find_next())
  #print(tertiaryconsumer.find_previous())

#html = urlopen("https://www.packtpub.com/all-products/all-books/")
#packtsoup = BeautifulSoup(html,"lxml")

# The stackoverflow method url is: https://stackoverflow.com/questions/3336549/pythons-urllib2-why-do-i-get-error-403-when-i-urlopen-a-wikipedia-page
url = "https://www.packtpub.com/all-products/all-books/"
req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
html = urllib.request.urlopen( req )
soup_packtpub = BeautifulSoup(html,"lxml")
#print (soup_packtpub)


print("Printing booktitles ...")
#booktitles = soup_packtpub.find("h5",class_="card-title mt-0")
#booktitles = soup_packtpub.find_all(class_="product-meta")
#booktitles = soup_packtpub.find("a",class_="card-body")
#booktitles = soup_packtpub.find("div",class_="card h-100")
#booktitles = soup_packtpub.find("div",class_="col-md-12")
#booktitles = soup_packtpub.find("div",id="instant-search-results-container")
booktitles = soup_packtpub.find_all("a",class_="product-item-link")
#print(booktitles)
for booktitle in booktitles:
  print("Printing booktitle ...")
  print(booktitle)
