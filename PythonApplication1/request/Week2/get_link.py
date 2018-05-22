import requests
r=requests.get("https://www.bilibili.com/video/av9784617/?p=30")
#r.encoding=r.apparent_encoding
demo=r.text

from bs4 import BeautifulSoup
soup=BeautifulSoup(demo,"html.parser")
for link in soup.find_all('a'): #soup('a')==soup.find_all('a')
    print(link.get('href'))


