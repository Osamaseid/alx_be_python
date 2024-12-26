def decorator(fun):
    def wrapper():
        print (" before function call")
        fun()
        print("after function call")
    return wrapper
@decorator
def say_hello():
    print("hello!")