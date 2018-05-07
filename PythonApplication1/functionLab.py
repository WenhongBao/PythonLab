import math

n1 = 255
n2 = 1000

print(hex(n1))
print(hex(n2))

print('Another lab start here..........')

def quadratic(a,b,c):
    judgement = b ** 2 - 4 * a * c

    if judgement < 0:
        result = "No result"
        return result
    elif judgement == 0:
        result = -b / (2 * a)
        return result
    else:
        result1 = ((-b) + math.sqrt(judgement)) / (2 * a)
        result2 = ((-b) - math.sqrt(judgement)) / (2 * a)
        return result1,result2

print(quadratic(2,3,1))
print(quadratic(1,3,-4))

print('Another lab start here..........')

L = [m + '=>' + n for m in "ABC" for n in "ABC" if m != n]
print(L)

print('Another lab start here..........')

L1 = ['Hello','World',18,'Apple']
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)