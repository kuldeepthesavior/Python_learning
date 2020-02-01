# variable and simple function
print('hey i love you pagli!!')
a=2
b=3
c=a+b
print(c)
def name(n):
    print('i love paretin \t :',n)


name('kuldeep')

print(a,b)

# tuple can not be modified


t=(1,2,'a','b','kuldeep',[11,10,2019])
print(t)
print(t[5][2])

# list can be modified

l=['i','created',1,'list']
print(l)
l[1]='have modified'
print(l)

# dictionary can be modified

d={'age':23,'name':'priti','address':'jaunpur'}
print(d)

if 'age' in d:
    print(d['age'])

# set duplicate is not allowed , print element in random order

s={1,2,2,3,'a','a','b'}
print(s)
if 1 in s:
    print('\nelement is present in set\n')


class Name():
    '''
    documenation string

    '''


print("dict",Name.__dict__)
print("doc",Name.__doc__)
print("name",Name.__name__)
print("module",Name.__module__)
print("bases",Name.__bases__)

print(input.__doc__,end='\n end of input doc\n\n\n')


import math

print(dir(math))
import sys
import os

print(os.getcwd())
print(dir(sys))

print('\n\n\n\n\n')

print(os.name)
print(os.environ)
# print(os.getlogin())
print(os.getppid())

import datetime

print(datetime.datetime.today())
now=datetime.datetime.today()
other=datetime.datetime(1997,2,13)
print(now-other)

print(datetime.time)
print(datetime.timezone)