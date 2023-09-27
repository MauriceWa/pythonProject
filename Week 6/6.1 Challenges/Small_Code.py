import random

number = random.randint(1,10)

guess = input("Silly game! Guess number between 1 and 10")
guess = int(guess)

if guess == number:
    print("You won!")

else:
    print("You lost!")