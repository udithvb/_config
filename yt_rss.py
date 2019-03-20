from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import xml.dom.minidom as md

#read rendered html
with open("gav_sen.html",'r') as ytf:
    html_doc = ytf.read() 

sp = BeautifulSoup(html_doc,'lxml')
mydivs = sp.find_all("a",id="video-title")
#mydivs contains all anchor tags with video title and url

root = ET.parse("sample.xml").getroot()
item_ls = root[0]
#sample.xml contains boiler plate

for count,i in enumerate(mydivs,1):
    item = ET.SubElement(item_ls,"item")
    ET.SubElement(item,"title").text = i.get_text()
    ET.SubElement(item,"link").text = f"http://www.youtube.com{i['href']}"
    ET.SubElement(item,"description").text = str(count)

tree =  ET.ElementTree(root)
tree.write("filename.xml")

#for readable , pretty xml
# dom = md.parse("sample.txt")
# prettyxml = dom.toprettyxml()
# with open("sample_pretty.xml",'x') as xml_file:
#     xml_file.write(prettyxml)
