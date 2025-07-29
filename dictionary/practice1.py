chuoi = input("Nhap moi chuoi ")

char_count = {}
for char in chuoi:
    if char != " ":
        if char in char_count:
            char_count[char] = char_count[char] +1
        else:
            char_count[char] = 1

for char,count in char_count.items():
    print(f"{char}:{count} lần")
        