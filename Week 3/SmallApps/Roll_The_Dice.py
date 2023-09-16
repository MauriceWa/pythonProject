import random


def roll_dice():
    return random.randint(1, 6)


def main():
    running = True
    while running:
        result = roll_dice()
        print("The result of rolling the dice is:"+'\n', result)

        choice = input("Do you want to roll again? (Yes/No): ")

        if choice.lower() != "yes":
            print("Program will now close.")
            running = False


if __name__ == "__main__":
    main()
