number_input = input("Input a number between 0 and 10:")
with open("Numbers.txt", "w") as file:
    file.write(number_input)

# Need to make a loremipsum file and somehow add numbers infront of each sentence in there through inputs