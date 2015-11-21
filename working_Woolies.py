##1 ---import modules
import urllib.request
from bs4 import BeautifulSoup
page=urllib.request.urlopen("http://www.woolworths.com.au/storelocator/service/storefinder/supermarkets/postcode/2005")
soup=BeautifulSoup(page)

##2 ---- find all items with tag javascript and count the number of items
javas=soup.findAll(attrs={"type":"text/javascript"})
lrange=len(javas)

##3 ----- define a function that finds the javascript item that contains "var stores"
def listf(i):
     try:
       return(
         "var stores" in javas[i].string)
     except:
     	 pass

##4 --- create a list to store true and false from 3
x=0
javalist=[]
for x in range(0,lrange):
	javalist.append(listf(x))
	x=x+1

##5 ---- get the javas.string item the contains the wanted store locations
number = javalist.index(True)

#6 ----- extract the chunk of text into a txt file
longStores = javas[number].string
f = open('woolies.txt','w')
shortStores=longStores[longStores.index("var stores"):longStores.index("var markers")]
f.write (shortStores)
f.close()

