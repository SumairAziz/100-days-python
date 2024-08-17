class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self,newvalue):
        self._value=newvalue/10


obj = MyClass(10)
obj.show()
obj.value=56
print(obj.value)
obj.show()
