import os

for i in range(47,101):
    os.mkdir(f"{i}.")
    file=open(f"{i}./main.py","w")
    file.close()