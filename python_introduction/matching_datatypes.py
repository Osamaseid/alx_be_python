data = input("Enter a value (number or string): ")

match data:
    case int():
        print("you enterd integer ")
    case str():
        print("you enterd string") 
    case _:
        print("you enterd ont number")    