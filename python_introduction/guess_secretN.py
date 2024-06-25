import random

# Generate a secret number
secret_number = random.randint(1, 10)

# Get user's guess
guess = int(input("Guess the number (1-10): "))

# Match the guess
match guess:
   
    case number if number > secret_number:
        print("Oops, your guess is a bit high. Try again!")
        
    case _:
        print("Nope, your guess is a bit low. Give it another shot!")
    case secret_number:
        print("Congratulations, you guessed it!")

# Offer to play again
play_again = input("Do you want to play again? (y/n): ")
if play_again.lower() == "y":
    print("Let's play again!")
else:
    print("Thanks for playing! Goodbye.")