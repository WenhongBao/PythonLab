import requests
url="http://www.ip138.com/ips138.asp?ip="

r=requests.get(url+'55.55.55.55'+'&action=2')
print(r.status_code)
r.encoding=r.apparent_encoding
print(r.text)