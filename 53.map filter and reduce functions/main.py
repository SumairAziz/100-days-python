# cube=lambda x:x**3

def cube(x):
    return x*x*x

# print(cube(3))

lists=[1,2,3,4,5,6,7]

lists=list(map(cube,lists))

# print(nlist)

def f(a):
    return a>4

new= list(filter(lambda x:x>12,lists))

print(new)

from functools import reduce

sum=reduce(lambda x,y:x+y,lists)

print(sum)