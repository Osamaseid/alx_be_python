class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")

animal = Animal("Elephant")
animal.eat()  
animal.sleep()  

dog = Dog("Buddy")
dog.eat()  
dog.sleep() 
dog.bark()  