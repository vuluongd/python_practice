sinh_vien = {}

sinh_vien["name"] = input("name:",)
sinh_vien["age"] = input("age:",)
sinh_vien["score"]=input("score:",)
sinh_vien["class"]=input("class:",)

key = input("needle: ")

info = sinh_vien.get(key)

if info is not None:
    print(f"{key} : {info}")
else:
    print(f"info is none")
