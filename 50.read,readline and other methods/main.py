# file=open("file.txt","r")
# i=0
# while True:
#     i+=1
#     line=file.readline()
#     if not line:
#         print("line",type(line))
#         break
#     s1=int(line.split(",")[0])
#     s2=int(line.split(",")[1])
#     s3=int(line.split(",")[2])
#     print(f"student number = {i} = {s1}")
#     print(f"student number = {i} = {s2}")
#     print(f"student number = {i} = {s3}")
#     print(line)
#     i+=1

file=open("file.txt","a")
lists=["\n","line1\n","line2\n","line3\n"]
file.writelines(lists)
file.close()