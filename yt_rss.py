from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

with open("cmp.html",'r') as ytf:
    html_doc = ytf.read() 

sp = BeautifulSoup(html_doc,'lxml')
mydivs = sp.find_all("a",id="video-title")









# for count,i in enumerate(mydivs,1):
#     print(count,f"http://www.youtube.com{i['href']}")
#     print(i.get_text())

