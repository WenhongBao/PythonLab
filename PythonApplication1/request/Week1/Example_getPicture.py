import requests
path="C:/Users/Administrator/Desktop/Python/abc.mp3"
url="https://www.xiami.com/song/1796378666"

r=requests.get(url)

print(r.status_code)

with open(path,'wb') as f:
    f.write(r.content)

f.close()

