from math import sin, pi
#4.1
a = int(input())
b = int(input())
if a>b:
    print(a)
elif a<b:
    print(b)
else:
    print('Equal')
#4.2
x = int(input())
if x > 0:
    y = (sin(x))**2
else:
    y = 1+ 2*sin(x**2)
#4.3
x = int(input())
if x > 0:
    y = (sin(x**2))
else:
    y = 1+ 2*sin(x)**2
#4.4
x = int(input())
if x > 4:
    print('2')
else:
    print('1')
#4.5
y = int(input())
if y > 3:
    print(1)
else:
    print(2)
#4.6
x = int(input())
if x < 2:
    y = x
else:
    y = 2
#4.7
k = int(input())
x = int(input())
if k<x: f = k*x
else: f = k+x
print(f)
#4.8
k = int(input())
x = int(input())
if x<k: f = abs(x)
else: f = k*x
print(f)
#4.9
a = int(input())
b = int(input())
if a>b: print('min = {b}, max = {a}')
else: print('min = {a}, max = {b}')
#4.10
km = int(input())
foot = int(input())
foot *= 0.3048
km *= 0.001
if foot > km:
    print(km)
else:
    print(foot)
#4.11
kmh = int(input())
mps = int(input())
kmh = kmh*10/36
if kmh>mps:
    print(mps())
else:
    print(kmh)
#4.12
circle = int(input())
kvadrat = int(input())
circle = pi*circle**2
kvadrat **= 2
if circle > kvadrat:
    print('Kruq')
else:
    print('Kvadrat')
#4.13
m1 = int(input())
m2 = int(input())
v1 = int(input())
v2 = int(input())
ro1 = m1/v1
ro2 = m2/v2
if ro1 > ro2: print(ro1)
else: print(ro2)
#4.14
r1 = int(input())
r2 = int(input())
u1 = int(input())
u2 = int(input())
i1 = u1/r1
i2 = u2/r2
if i1 > i2: print(i2)
else: print(i1)
#4.15
a = int(input())
b = int(input())
c = int(input())
if b**2 - 4*a*c >= 0:
    print('Имеет')
else:
    prit('HeT')
#4.16
a = int(input())
b = int(input())
c = int(input())
if b**2 - 4*a*c >= 0:
    x1 = (-b + (b**2 - 4*a*c))/2*a
    x2 = (-b - (b**2 - 4*a*c))/2*a
    print(x1,x2)
else:
    prit('HeT')
#4.17
monthcalendar = int(input())
monthhuman = int(input())
yearcalendar = int(input())
yearhuman = int(input())
if monthhuman <= monthcalendar:
    print(yearcalendar-yearhuman)
else:
    print(yearcalendar - yearhuman - 1)
#4.18
radius = int(input())
a = int(input())
radius = (radius**2)*pi
a **= 2
if radius > a:
    print('No')
else:
    print('Yes')
#4.99 b
a = int(input())
b = int(input())
if a > b:
    b=a
print(b)
#4.101
a = int(input())
b = int(input())
c = int(input())
d = int(input())
min = a
max = a
if min>b:
    min = b
if b>max:
    max = b
if min>c:
    min = c
if max<c:
    max = c
if min>d:
    min = d
if max<d:
    max = d
print(min,max)
#4.105
a = int(input())
b = int(input())
if a>abs(b):
    a/=2
print(a)
#4.109
def inter(x):
    if 1.6<=x and x<=3.8:
        return x
a = int(input())
b = int(input())
c = int(input())
print(inter(a), inter(b), inter(c))
#4.116
x = int(input())
if x <-1:
    y = -1
elif x > -1:
    y = x
else:
    y = 1
print(y)