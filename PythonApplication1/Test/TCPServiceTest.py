import socket

#create a socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#listen
s.bind(('127.0.0.1',9999))
s.listen(5)
print('Waiting for connection....')

while True:
    #accept a new connection
    sock,addr=s.accept()
    #create a new thread to slove TCP connection
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()
    
def tcplink(sock,addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(('Hello,%s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

#create conection
s.connect(('127.0.0.1',9999))
#get welcome message
print(s.recv(1024).decode('utf-8')) 
for data in [b'Michael',b'Tracy',b'Sarah']:
    #send data
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s,close()