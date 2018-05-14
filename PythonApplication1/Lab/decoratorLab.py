

import functools
def log1(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('begin call')
        return func(*args,**kw)
    return wrapper

@log1
def print_name():
    print('Parker')

print_name()