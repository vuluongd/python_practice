class Student:
    def __init__(self, name, age, grade):
        self.name = name 
        self.age = age
        self .grade = grade
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    def is_passed(self):
        return self.grade >= 5

luong = Student("luong", 20, 6)

luong.display_info()

print ("Passed: ", luong.is_passed())