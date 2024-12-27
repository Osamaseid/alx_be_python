class MyClass:
    def method(self):
        print("Method called")

obj = MyClass()
method_name = 'method'
getattr(obj, method_name)()  # Calls obj.method()