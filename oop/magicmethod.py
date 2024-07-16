class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"Name: {self.name}, Age: {self.age}"

person = Person("Alice", 30)
print(person)