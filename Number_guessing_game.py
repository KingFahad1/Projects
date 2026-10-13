from random import randint

print("Welcome to the Number Guessing Game")
secret_number = randint(1,100)
while True:
    try:
        guess = int(input("Please enter a number between 1 and 100: "))
        if guess == secret_number:
            print("Congratulations! You guessed the number!")
            break
        elif guess > secret_number:
            print("You guessed too high!")
        elif guess < secret_number:
            print("You guessed too low!")
    except ValueError as e:
        print("That's not a valid guess! Please try a numerical value.")

