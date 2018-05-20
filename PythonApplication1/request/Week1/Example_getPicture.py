import requests
path="C:/Users/Administrator/Desktop/Python/abc.jpg"
url="http://singerimg.kugou.com/uploadpic/softhead/400/20171222/20171222165824304.jpg"

r=requests.get(url)

print(r.status_code)

with open(path,'wb') as f:
    f.write(r.content)

f.close()

