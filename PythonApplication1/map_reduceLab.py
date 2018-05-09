def normalize(name):
    return name.capitalize()

L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
print(L2)

print('Another lab start here..........')

from functools import reduce;

L3=[3,5,7,9]
def call(x,y):
    return x*y;
def prod(L):
    reduce(call,L);
print('3*5*7*9',prod(L3));