import re

#正则表达式中group（）用来提出分组截获的字符串，（）用来分组
#import re
#a = "123abc456"
#print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0)   #123abc456,返回整体
#print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1)   #123
#print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2)   #abc
#print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3)   #456

#编译正则表达式，编译成正则表达式对象
print('re.compile=>')
p=re.compile(r'[1-9]\d{5}')
print(p)

#在字符串中搜索匹配正则表达式的第一个位置，返回match对象
print('re.search=>')
match=re.search(r'[1-9]\d{5}','BIT 100081')
if match:
    print(match.group(0))

#从字符串的开始位置起匹配正则表达式，返回match对象
print('re.match=>')
match=re.match(r'[1-9]\d{5}','100081 BIT')
if match:
    print(match.group(0))

#搜索字符串，以列表类型返回全部能匹配的子串
print('re.findall=>')
ls =re.findall(r'[1-9]\d{5}','BIT100081 TSU100084')
print(ls)

#将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
print('re.split=>')
ls1=re.split(r'[1-9]\d{5}','BIT100081 TSU100084')
print(ls1)

#搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
print('re.finditer=>')
for m in re.finditer(r'[1-9]\d{5}','BIT100081 TSU100084'):
    if m:
        print(m.group(0))

#在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
print('re.sub=>')
p1=re.sub(r'[1-9]\d{5}',':zipcode','BIT100081 TSU100084')
print(p1)
