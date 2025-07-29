student = {}
n = int(input("nhập số sinh viên: "))
for i in range(n):

    mssv = input(f"nhap ma so sinh vien cua sv thu {i+1}: ")

    name = input("ten: ")

    age = input("tuoi: ")

    score = input("diem: ")

    student[mssv]= {"ten":name, "tuoi":age, "diem":score}

for mssv, info in student.items():
    print(f"{mssv}:{info}")
