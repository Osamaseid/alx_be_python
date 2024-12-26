def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        fun(*args, **kwargs)
        fun(*args, **kwargs)
    return wrappers_do_twice
@do_twice
def greet(name):
    print(f"Hello{name}") 
