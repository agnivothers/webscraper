from bs4 import BeautifulSoup

with open("ecologicalpyramid.html","r") as ecological_pyramid:
  soup = BeautifulSoup(ecological_pyramid,"lxml")
producer_entries = soup.find("ul")
print(producer_entries)
print(type(producer_entries))
print(len(producer_entries))
for producer in producer_entries:
  print('Printing producer')
  print(type(producer))
  print(len(producer))
  print(producer)
"""
print(producer_entries.li.div.string)
primary = soup.find(id="primaryconsumers")
print(primary.text)

css_class = soup.find(attrs={'class':'primaryconsumerlist'})
print(css_class)
all_tertiaryconsumers = soup.find_all(class_="tertiaryconsumerlist")
for tertiaryconsumer in all_tertiaryconsumers:
  print(tertiaryconsumer.div.string)
print("------------")
all_li = soup.findAll("div",class_="name")
for li in all_li:
  print(li.string)
print('-----------')

producers = soup.find_all(id="producerlist")
for producer in producers:
  print('Printing producers')
  print(producer)
"""
