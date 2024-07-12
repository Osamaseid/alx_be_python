class Animal :
    def __init__(self, name, age ):
        self.name = name
        self.age = age

    def speak(self):
        print("the animal makes a sound.")
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def speak(self):
        print("the dog bark")
dog1 = Dog("bobi", 2, "mixed")
dog1.speak()
print(dog1.name)
print(dog1.age)