def appl(fx,value):
    return value + fx(value)

double = lambda x:x**2
avg = lambda x,y:(x+y)/2

# print(double(5))
# print(avg(5,5))
print(appl(double,5))
print(appl(lambda x:x**2,5))