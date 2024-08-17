# file=open("myfile.txt","r") # reading mode is default
# # file.write("I am sumair aziz")

# text=file.read()
# print(text)
# file.close()

# file=open("myfile.txt","a")
# file.write("I am sumair aziz\n")
# file.close()

with open("myfile.txt","a") as file:
    file.write("I am sumair aziz\n")
