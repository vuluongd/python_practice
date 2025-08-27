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