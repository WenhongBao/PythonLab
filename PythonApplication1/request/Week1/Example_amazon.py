import requests

url="https://www.amazon.cn/gp/product/B01M8L5Z3Y"

r=requests.get(url)
#because not error (it should be error here) occur please go to Note.txt 
print(r.status_code)
print(r.encoding)
print(r.request.headers)