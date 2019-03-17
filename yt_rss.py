from bs4 import BeautifulSoup
with open("pamp.html",'r') as ytf:
    html_doc = ytf.read() 
sp = BeautifulSoup(html_doc,'lxml')
mydivs = sp.find_all("a",id="video-title")
print("*"*10)
#print(mydivs)
for count,i in enumerate(mydivs,1):
    print(count,i['href'])
    print(i.get_text())

#print(len(mydivs))
