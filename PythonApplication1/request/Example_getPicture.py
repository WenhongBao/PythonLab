import requests
path="D:/abcd.jpg"
url="http://v.youku.com/v_show/id_XMzYxMzE2MTE0NA==.html?spm=a2hww.20027244.m_250036.5~5!2~5~5~5~5~A&f=51733384"

r=requests.get(url)

print(r.status_code)

with open(path,'wb') as f:
    f.write(r.content)

f.close()

