import bs4
import request
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
my_url= 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
#open up connetction, grab the page
uclient= ureq(my_url)
page_html=uclient.read()
uclient.close()
#html parsing
page_soup = soup(page_html,"html.parser")
#header of the page
page_soup.h1
page_soup.p
page_soup.body.span
container= page_soup.findAll('div',{"class":"item_container"})
len(container)








