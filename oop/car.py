
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

#The self Keyword:
#The self keyword is used within instance methods to refer to the current instance of the class.
#It allows the instance method to access and manipulate the instance's attributes and call other instance methods.
#The self keyword is a convention in Python, and it is the first parameter in the method definition. However, you can use any other name instead of self, as long as you use the same name consistently within the class.
#The self keyword is not used when calling the instance method; it is automatically passed by the Python #interpreter when the method is called.