import json

keys = ["name","sex","major","career"]
values = ["luong", "male", "Aerospace Engineering", "university student"]

my_dict = dict(zip(keys,values))
print(my_dict)

my_json = json.dumps(my_dict, indent = 10, ensure_ascii=False)
print(my_json)