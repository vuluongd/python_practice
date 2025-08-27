'''
Lệnh zip() trong Python được dùng để “ghép cặp” các phần tử từ nhiều iterable (list, tuple, string, …) lại với nhau theo từng chỉ số.

zip(iterable1, iterable2, ..)
Trả về một iterator các tuple, mỗi tuple chứa các phần tử từ các iterable tương ứng.
'''
names = ["An", "Binh", "Luong"]
ages = [23, 22, 21]

result =zip(names, ages)
print(list(result))
# Kết quả: [('An', 23), ('Binh', 22), ('Luong', 21)]
# Nếu các iterable có độ dài khác nhau, zip sẽ dừng lại ở iterable ngắn nhất
names = ["An", "Binh"]
ages = [23, 22, 21]
result =zip(names, ages)
print(list(result))
# Kết quả: [('An', 23), ('Binh', 22)]
# Sử dụng * để giải nén các tuple
pairs = [('An', 23),('Binh', 22, ('Luong',21))]
names, ages = zip(*pairs)
print(names)
print(ages)
# Kết quả: ('An', 'Binh', 'Luong')
# Kết quả: (23, 22, 21)
# Chuyển đổi kết quả của zip thành list hoặc dict
names = ["An", "Binh", "Luong"]
ages = [23, 22, 21]
result_list = list(zip(names, ages))
result_dict = dict(zip(names, ages))
print(result_list)
print(result_dict)
# Kết quả: [('An', 23), ('Binh', 22), ('Luong', 21)]
# Kết quả: {'An': 23, 'Binh': 22, 'Luong': 21}
# Sử dụng zip trong vòng lặp for
names = ["An", "Binh", "Luong"]
ages = [23, 22, 21]
for name, age in zip(names, ages):
    print (f"{name} is {age} years old")

# Kết quả:
# An is 23 years old
# Binh is 22 years old
# Luong is 21 years old
