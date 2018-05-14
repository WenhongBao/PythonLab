import hashlib
db={}

def get_md5(password):
    md5=hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

def register(username,password):
    db[username]=get_md5(password+username+'the Salt')
    
def login(username,password):
    if db[username]==get_md5(password+username+'the Salt'):
        pass
    else:
        return 'password incorrect'
       
print('Please register first')
get_username=input('Please enter your username to register: ')
get_password=input('Please enter your password to register: ')

register(get_username,get_password)

print('Please login now')
username=input('Please enter your username to login: ')
password=input('Please enter your password to login: ')

login(username,password)

print('Finish')