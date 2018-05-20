import requests
r=requests.get("https://baike.baidu.com/item/%E7%BD%91%E7%AB%99%E6%B5%8B%E8%AF%95/2688344?fr=aladdin")
r.encoding=r.apparent_encoding
demo=r.text

from bs4 import BeautifulSoup
#html.parser为html解释器
soup=BeautifulSoup(demo,"html.parser")
print(soup.title)
