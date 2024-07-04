import random

# Generate a set of 10 random numbers between 1 and 10
random_numbers = set(random.randint(1, 10) for _ in range(10))

# Print the unique numbers
print("Unique numbers:", random_numbers)