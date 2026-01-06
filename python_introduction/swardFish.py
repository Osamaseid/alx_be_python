while True:
    print("who are you:")
    name = input()
    if name != "os":
        continue
    print(" hello tell me your password")
    password = input()
    if password == "swardFish":
        break
print("Access granted!")