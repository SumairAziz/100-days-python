x=4

def change():
    global x
    x=5
    y=5
    print(x)
    print(y)

change()
print(f"global value of x is {x}")
# print(f"global value of y is {y}")