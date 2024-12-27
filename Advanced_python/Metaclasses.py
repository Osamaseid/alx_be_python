class Meta(type):
    def __new__(cls, name, bases, attrs):
        attrs['greet'] = lambda self: "Hello!"
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=Meta):
    pass

obj = MyClass()
print(obj.greet())