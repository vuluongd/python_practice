#python classes
class Person:
    def __init__(self,name):
        self.name = name
    def say_hello(self):
        print(f"Hello {self.name}!")
luong = Person('Luong')
luong.say_hello()