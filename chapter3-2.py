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
  print(tertiaryconsumer.find_previous())
