danh_sach = input("Nhập danh sách từ: ").split()
do_dai = {}

for tu in danh_sach :
    do_dai[tu] = len(tu)

max_len = max(do_dai.values())

print(f"Độ dài lớn nhất: {max_len}")
print("Các từ dài nhất:")

for tu, dai in do_dai.items():
    if dai == max_len:
        
        print (tu)