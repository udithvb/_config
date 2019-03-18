import xml.dom.minidom as md

dom = md.parse("sample.txt")
prettyxml = dom.toprettyxml()

with open("sample_pretty.xml",'x') as xml_file:
    xml_file.write(prettyxml)
    
