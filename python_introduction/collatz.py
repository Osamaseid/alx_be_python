def collatz(number):
    if number % 2 == 0:          # if number is even
        result = number // 2
        print(result)
        return result
    else:                       # if number is odd
        result = 3 * number + 1
        print(result)
        return result

num = int(input("Enter an integer: "))

while num != 1:
    num = collatz(num)
