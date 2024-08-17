class Person:
    def __init__(self, n="Unknown", o="Unknown"):
        self.name = n
        self.occupation = o
        print(f"Hey, my name is {self.name} and I am a {self.occupation}")

# Using the constructor with both arguments
p = Person("Sumair", "Student")

# Using the constructor with default arguments
p1 = Person()


class Person2:
    def __init__(self, *args):
        if len(args) == 2:
            self.name = args[0]
            self.occupation = args[1]
            print(f"Hey, my name is {self.name} and I am a {self.occupation}")
        elif len(args) == 1:
            self.name = args[0]
            self.occupation = "Unknown"
            print(f"Hey, my name is {self.name} and my occupation is unknown")
        else:
            print("Hey, I am a mystery person!")

# With two arguments
p2 = Person2("Sumair", "Student")

# With one argument
p3 = Person2("Sumair")

# With no arguments
p4 = Person2()
