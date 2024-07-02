rows = 5

i = 1
while i <= rows:
    space = 1
    while space <= rows - i:
        print(" ", end="")
        space += 1
    
    asterisk = 1
    while asterisk <= (2 * i - 1):
        print("*", end="")
        asterisk += 1
    
    print()
    i += 1