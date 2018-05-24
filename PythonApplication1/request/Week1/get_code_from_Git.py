import requests
path="C:/Users/Administrator/Desktop/Python/abc.py"
url="https://github.com/WenhongBao/PythonLab/blob/9f53dcce08e9f41bc7adc25f09d47c8ea2a2cfc7/PythonApplication1/Test/tkinterTest.py"

r=requests.get(url)

print(r.status_code)

with open(path,'wb') as f:
    f.write(r.content)

f.close()