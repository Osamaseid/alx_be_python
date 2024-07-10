class ValueTooHighError(Exception):
    
    pass

def check_value(num):
    if num > 100:
        raise ValueTooHighError(f"The value {num} is too high. The maximum allowed value is 100.")
    else:
        print(f"The value {num} is valid.")

try:
    user_input = int(input("Enter a number: "))
    check_value(user_input)
except ValueTooHighError as e:
    print(e)
except ValueError:
    print("Invalid input. Please enter a number.")

# alternative way    
 #   x = 10
#limit = 100
 
#if x > limit:
 ##  raise NumberTooLargeError(message)