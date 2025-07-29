diem_sv = {}
n = int(input("Nhập số sinh viên: " ))

for i in range (n):
    ten = input("Nhập tên sinh viên: ")
    diem = int(input(f"Nhập điểm sinh viên {ten}: "))
    diem_sv[ten] = diem

tong_diem = 0

for diem in diem_sv.values():
    tong_diem = tong_diem + diem

trung_binh = tong_diem/ len(diem_sv) if diem_sv else 0

print (f"Điểm trung bình:  {trung_binh:.2f}")
print ("Sinh viên có điểm trên trung bình:")

for ten, diem in diem_sv.items():
    if diem > trung_binh:
        print (f"{ten}: {diem}")


