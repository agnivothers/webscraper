from bs4 import BeautifulSoup

with open("ecologicalpyramid.html","r") as ecological_pyramid:
  soup = BeautifulSoup(ecological_pyramid,"lxml")
"""
producer_entries = soup.find("ul")
print(producer_entries.attrs)
print(producer_entries)
print(producer_entries.string)
list_entry = soup.find("li")
print(type(list_entry))
print(list_entry)
print(list_entry.attrs)
#print(list_entry.attrs['class']['producerlist'])
print(list_entry.name)
#print(list_entry.name.string)
#print(list_entry['producerlist'])

div_entries = soup.find("div")
print(div_entries.attrs)
print(div_entries.string)
"""
some_text = soup.find(text="plants")
print(type(some_text))
print(some_text)
#producer = soup.find(id="producers")
#print(producer)
primaryconsumer = soup.find(id="primaryconsumers")
print(primaryconsumer)
