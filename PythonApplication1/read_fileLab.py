#'r' => read 'rb' => read byte 'r', encoding='gbk' => read UTF-8 'w'/'wb' => write/write byte
f=open('decoratorLab.py','r')
print(f.read())
f.close()

with open('decoratorLab.py','r')as f:
    print(f.read())