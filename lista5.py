# 1
l = [3, 'alfa', 2.71, 'kot']
print(l[3])
print(l[-4])
l[0] = 4
l[3] = 'pies'
print(l)
l2 = l
print(l, l2)
l2[0] = 'cyfra'
print(l, l2)
l3 = l.copy()
l3[0] = 27
print(l, l3)

print('\n')
# 2
l = []
for i in range(0, 10):
    l += [(i+1)**2]
print(l)
for i in range(0, 10):
    if l[i] % 2 == 0:
        l[i] *= -1
print(l)

print('\n')
# 3
import random
n = int(input('Ile liczb w liście: '))
l = []
for i in range(0, n):
    l += [random.randint(0, 100)]
maks = 0
min = 100
for i in range(0, n):
    if l[i] > maks:
        maks = l[i]
    if l[i] < min:
        min = l[i]
print('Największa liczba:', maks)
print('Najmniejsza liczba:', min)

print('\n')
# 4
from math import sin
l = []
n = int(input('Ile liczb w liście: '))
for i in range(0, n):
    l += [sin(i+1)]
    maks = 0
    min = 100
for i in range(0, n):
    if l[i] > maks:
        maks = l[i]
    if l[i] < min:
        min = l[i]
print('Największa liczba:', maks)
print('Najmniejsza liczba:', min)

print('\n')
# 5
l = []
for i in range(0, 51):
    l += [100+i]
for i in range(1, 38):
    if l[i] % 5 == 0:
        del l[i]
print(l)

print('\n')
# 6
l = [5, 24, 65, 23, 45, 67, 34, 89, 123, 456]
l2 = l.copy()
element = l2[0]
del l2[0]
l2 += [element]
l3 = l.copy()
element = [l3[9]]
del l3[9]
element += l3
l3 = element.copy()
l4 = []
for i in range(-1, -11, -1):
    l4 += [l[i]]
l5 = []
for i in range(0, 10):
    if l[i] % 2 == 0:
        l5 += [l[i]]
l6 = []
for i in range(0, 10):
    if l[i] % 2 != 0 and i % 2 == 0:
        l6 += [l[i]]
print('l=', l)
print('l2=', l2)
print('l3=', l3)
print('l4=', l4)
print('l5=', l5)
print('l6=', l6)

print('\n')
# 7
from math import pi
mypi = pi
l = []
for i in range(0, 50):
    l += [int(mypi % 10)]
    mypi *= 10
print(l)
