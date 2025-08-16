"""
1. Class cơ bản

Yêu cầu:
Tạo class Student với các thuộc tính:

name

age

grade (điểm trung bình)

Viết phương thức:

display_info() → in thông tin học sinh.

is_passed() → trả về True nếu điểm ≥ 5, ngược lại False.
"""
class Student:
    def __init__(self, name, age, grade):
        self.name = name 
        self.age = age
        self .grade = grade
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    def is_passed(self):
        return self.grade >= 5

luong = Student("luong", 20, 4)

luong.display_info()

print ("Passed: ", luong.is_passed())