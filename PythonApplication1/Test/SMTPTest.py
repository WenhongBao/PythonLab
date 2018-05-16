from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr

import smtplib

 
def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

from_addr=input('From: ')
password=input('Password: ')
to_addr=input('To: ')
smtp_server=input('SMTP server: ')#check smtp_server.txt (GMail: smtp.gmail.com, port:587)

#if html mail: change first item to html coding, change second item to 'html'
msg =MIMEText('hello, send by Python...','plain','utf-8')
msg['From']=_format_addr('PythonLover<%s>' % from_addr)
msg['To']=_format_addr('admit<%s>' % from_addr)
msg['Subject']=Header('from SMTP....','utf-8').encode()

server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
#please make sure your email open pop3 and smtp server before testing
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

