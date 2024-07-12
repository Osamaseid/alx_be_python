
class car :

    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price

car1 = car("toyota", "red", 12300)
car2 = car("nissan", "green", 123333)
print(car1);

class mobile :
    def __init__(self, number, model, color, size):
        self.model = model
        self.color = color
        self.number = number
        self.size = size
    def __str__(self):
        return f"{self.model} {self.color} {self.number} {self.size}"
        
    
mobile1 = mobile(23, "dd", "green", "34px") 

print(mobile1)  