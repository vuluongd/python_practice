# duyệt, đếm số lượng
my_dict = {
    "name": "luong",
    "age" : 25,
    "major": "Aerospace Engineering"

 }
for key in my_dict.keys():
    print(key)
for value in my_dict.values():
    print(value)
for v,k in my_dict.items():
    print(f"{v}: {k}")
print(len(my_dict))