class Employee:
    def __init__(self,name):
        self.name=name

class Dancer:
    def __init__(self,role):
        self.role=role

class dancer_employee(Employee,Dancer):
    def __init__(self,name,role,grade):
        self.grade=grade
        Employee.__init__(self,name)
        Dancer.__init__(self,role)

d=dancer_employee("Harry","main","18")
print(d.name," ",d.role," ",d.grade)
print(dancer_employee.mro())

# class Employee:
#   def __init__(self, name):
#     self.name = name
#   def show(self):
#     print(f"The name is {self.name}")

# class Dancer:
#   def __init__(self, dance):
#     self.dance = dance

#   def show(self):
#     print(f"The dance is {self.dance}")

# class DancerEmployee(Employee, Dancer):
#   def __init__(self, dance, name):
#     self.dance = dance
#     self.name = name

# o  = DancerEmployee("Kathak", "Shivani")
# print(o.name)
# print(o.dance)
# o.show() 
# print(DancerEmployee.mro())