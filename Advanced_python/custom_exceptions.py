class MyError(Exception):
    pass

def check_value(x):
    if x < 0:
        raise MyError("Negative value error")

try:
    check_value(-1)
except MyError as e:
    print(e)