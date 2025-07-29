#setdefault() và get()
my_dict = {
    "name": "luong",
    "age": 22
}

#dùng get() để truy xuất
print(my_dict.get("name"))

#dùng setdefault để thêm với mặc định

#nếu sex chưa tồn tại thì là male
my_dict.setdefault("sex", "male")
#nếu name đã tồn tại thì không thay đổi
my_dict.setdefault("name", "bob")

print(my_dict)