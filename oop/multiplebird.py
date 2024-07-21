class Bird:
    def fly():
        return "i can fly"
class Mammals:
    def run():
        return "i ca run"
class Bat(Bird, Mammals):
    def fly():
        return " i can do both"
    def run():
        return "i can do both"
bat = Bat()
print(Bat.fly())