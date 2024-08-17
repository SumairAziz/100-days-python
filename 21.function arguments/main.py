

def avg(a,b):
    print((a+b)/2)

avg(3,7)
def avg(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum+=i
    print("Average is ",sum/len(numbers))

avg(3,7)


def name(**name):
  print(type(name))
  print("Hello,", name["fname"], name["mname"], name["lname"])


name(mname="Buchanan", lname="Barnes", fname="James")