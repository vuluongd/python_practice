#Tạo một dictionary từ hai list: keys và values.
keys = ["names","age","major","career","sex"]
values = ["luong","22", "Aerospace Engineering", "university student", "male"]
my_dict = dict(zip(keys,values))
print (my_dict)
#Tạo một dictionary với các giá trị mặc định.
her_keys = ["names","age","phone"]
her_value = ["unknown"]
her_dict = dict.fromkeys(her_keys, her_value)
print(her_dict)