try:
    x = 1 / 0
except (ZeroDivisionError, ValueError) as e:
    print("An error occurred:", e)