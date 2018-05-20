import requests

kv={'wd':'Python'}
url="http://www.baidu.com/s"
#params mean add text after url
r=requests.get(url,params=kv)
print(r.request.url)
print(len(r.text))
