"""
2. Kế thừa (Inheritance)

Yêu cầu:

Tạo class Animal với thuộc tính name, sound.

Tạo class Dog kế thừa từ Animal và có thêm phương thức fetch() in "Fetching stick...".

Tạo class Cat kế thừa từ Animal và có thêm phương thức climb() in "Climbing tree...".
"""

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def make_sound(self):
        print(f"{self.name} says: {self.sound}")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")

    def fetch(self):
        print(f"{self.name} is fetching stick...")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")
    
    def climb(self):
        print(f"{self.name} is climbing tree...")

dog = Dog("Buddy")
cat = Cat("Kitty")

dog.make_sound()
dog.fetch()

cat.make_sound()
cat.climb()