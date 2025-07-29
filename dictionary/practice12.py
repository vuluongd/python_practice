dict1 = {"a":1, "b":5}
dict2 = {"b":8, "c":10}

dict1.update(dict2)
print(dict1)

#common_keys
common_keys = dict1.keys() & dict2.keys()
print(common_keys)

dict4 = {"d":5, "e":7, "a":12}
for key in sorted(dict4.keys()):
    print(key)

dict3 = {"a":1, "b":5}
print(dict1 == dict3)

