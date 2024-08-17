class Parent:
    def __init__(self):
        print("hello, parent")

    def show1(self):
        print("I am public parent")

    def _show2(self):
        print("I am protected parent")

    def __show3(self):
        print("I am private parent")

p=Parent()
p.show1()
p._show2()
p._Parent__show3()
print(p.__dir__())
