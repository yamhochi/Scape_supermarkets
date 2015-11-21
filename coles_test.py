import urllib.request
from bs4 import BeautifulSoup


page=urllib.request.urlopen("file:///Users/hoecheeyam/Desktop/Scrape/data_supermarket/Coles_Store_Locator.html")
soup = BeautifulSoup(page)
f=open('opendata.txt','w')
addresses = soup.findAll(attrs={"class":"address"})
joints = soup.findAll('h4')
x=0
for x in range (0,764):
	address = addresses[x].string
	joint = joints[x].string
	f.write (joint+","+address+"\n")
	x=x+1

f.close()