class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Student name: {self.name}")
        print(f"Student age: {self.age}")

student = Student("Muhammad", 21)
student.display_info()