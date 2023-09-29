PIZZA_NAME = 0
FLOWER_IN_GRAM = 600
WATER_PERCENTAGE = 52
SALT_PERCENTAGE = 2.5
YEAST_PERCENTAGE = 1


def calculate_ingredients_in_grams():
    water_in_gram = FLOWER_IN_GRAM * WATER_PERCENTAGE / 100
    salt_in_gram = FLOWER_IN_GRAM * SALT_PERCENTAGE / 100
    yeast_in_gram = FLOWER_IN_GRAM * YEAST_PERCENTAGE / 100
    print(f"Flower in grams: {FLOWER_IN_GRAM}")
    print(f"Water in grams: {water_in_gram}")
    print(f"Salt in grams: {salt_in_gram}")
    print(f"Yeast in grams: {yeast_in_gram}")


def write_pizza_to_text_file():
    with open("Ingredients_Pizza.txt", "a") as file:
        int(file.write("water" + "\n"))


def main():
    calculate_ingredients_in_grams()
    write_pizza_to_text_file()


if __name__ == "__main__":
    main()
