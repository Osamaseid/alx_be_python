# -------------------------------
# 1) Comma Code
# -------------------------------

def comma_code(items):
    if len(items) == 0:
        return ''
    elif len(items) == 1:
        return items[0]
    else:
        return ', '.join(items[:-1]) + ', and ' + items[-1]


# Test Comma Code
spam = ['apples', 'bananas', 'tofu', 'cats']
result = comma_code(spam)
print("Comma Code Result:")
print(result)
print()


# -------------------------------
# 2) Character Picture Grid
# -------------------------------

grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]

print("Character Picture Grid:")

for y in range(len(grid[0])):        # loop through rows
    for x in range(len(grid)):      # loop through columns
        print(grid[x][y], end='')
    print()                         # new line after each row
