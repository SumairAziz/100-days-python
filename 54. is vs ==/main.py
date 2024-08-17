a=4
b="4"

print(a is a) #exact location of object in memory
print(a== b) #value

a = None
b = None

print(a is b) # exact location of object in memory
print(a is None) # exact location of object in memory
print(a == b) # value