
def greet(fx):
    def mfx(*args,**kwargs):
        print("Welcome")
        fx(*args,**kwargs)
        print("Farewell\n\n")
    return mfx
@greet
def hello():
    print("Hello world")
hello()
# greet(hello())


# @greet
def hello2(a,b):
    print("Hello world2")
    print(a+b)
greet(hello2)(1,2)
greet(hello2(1,2)) #wont greet


print(" \t\t-------------------------\t\t".center(80))

import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    print( a + b)