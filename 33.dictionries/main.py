info = {"name": "Karan", "age": 19, "eligible": True}
# print(info)
# print(info.keys())
# print(info.values())

# for key in info.keys():
#     print(f"The value corresponding to the {key.center(11)} is {info[key]}")

print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key.center(11)} is {value}")
