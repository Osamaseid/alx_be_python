def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
  
@do_twice
def greet(name):
    print(f"Hello{name}") 

