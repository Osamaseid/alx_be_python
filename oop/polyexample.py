class Dog:
    def make_sound(self):
        return "woof"

class Cat:
    def make_sound(self):
        return "meeaw"

class Bird:
    def make_sound(self):
        return "pip"

def let_them_speak(obj):
    return obj.make_sound()

cat_obj = Cat()
dog_obj = Dog()
bird_obj = Bird()

print(let_them_speak(cat_obj))
print(let_them_speak(dog_obj))
print(let_them_speak(bird_obj))
    