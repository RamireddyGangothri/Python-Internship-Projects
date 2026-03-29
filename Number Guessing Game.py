import random

print("Number Guessing Game")
print("Guess a number between 1 and 50")

number = random.randint(1, 50)
guess = None

while guess != number:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")
