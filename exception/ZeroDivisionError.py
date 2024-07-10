num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

def div_num():
    try:
        div = num1 / num2
        print(div)
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("The division was successful.")
    finally:
        print("The div_num function has completed.")

print(div_num())