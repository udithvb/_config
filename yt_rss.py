from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import xml.dom.minidom as md

with open("cmp.html",'r') as ytf:
    html_doc = ytf.read() 

sp = BeautifulSoup(html_doc,'lxml')
mydivs = sp.find_all("a",id="video-title")



# dom = md.parse("sample.txt")
# prettyxml = dom.toprettyxml()
# with open("sample_pretty.xml",'x') as xml_file:
#     xml_file.write(prettyxml)

root = ET.parse("sample.xml").getroot()

# for child in root:
#     print(child.tag)


# print(mydivs[0])
#print("root 0 2: ",root[0][2]) #item
item_ls = root[0]
# print("item_ls:",item_ls)
#root = ET.Element("channel")
#item = ET.SubElement(item_ls,"item")

for count,i in enumerate(mydivs,1):
    item = ET.SubElement(item_ls,"item")
    ET.SubElement(item,"title").text = i.get_text()
    ET.SubElement(item,"link").text = f"http://www.youtube.com{i['href']}"
    ET.SubElement(item,"description").text = str(count)

    
    # print(count,f"http://www.youtube.com{i['href']}")
    # print(i.get_text())
    #break

tree =  ET.ElementTree(root)
tree.write("filename.xml")

# print(ET.tostring(root))
# with open("test_xml",'x') as f:
#     f.write(root.tostring())
