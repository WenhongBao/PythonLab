import requests

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()#if 200 mean success 404 mean fail. use r.raise_for.status() to make sure is 200 or not.
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "Error!!"


url="https://item.jd.com/2967929.html"
print(getHTMLText(url))


