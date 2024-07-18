class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"name: {self.name} age: {self.age}")

    def __del__(self):
        print(f"Deleting the object for {self.name}")

person = Person("Alice", 30)
person.display() 


