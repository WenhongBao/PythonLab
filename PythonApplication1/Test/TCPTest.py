import socket

#create a socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#make a connect
s.connect(('www.sina.com.cn',80))
#send data
s.send(b'GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n')
#get data
buffer=[]
while True:
    #1k everytime
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)
s.close()

header,html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))

#put data into doc
with open('sina.html','wb') as f:
    f.write(html)