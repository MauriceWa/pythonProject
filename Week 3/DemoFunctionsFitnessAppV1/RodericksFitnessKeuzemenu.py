def menu():
    running = True
    while running:
        print("What do you want to calculate?" + '\n' + "1. BMI" + '\n' + "2. BMR" + '\n' + "3. Energy usage" + '\n'
            + "4. Karvanonen"+'\n' + "5. Exit")
        menu = int(input())
        if menu == 1:
            w = int(input("Weight:"))
            l = int(input("Length:"))
            print('bmi: %.2f' % calculate_bmi(w, l) + '\n')

        elif menu == 2:
            gender = input("Gender: ")
            a = int(input("Age: "))
            w = int(input("Weight:"))
            l = int(input("Length:"))
            print('bmr: %.2f' % calculate_bmr(gender, w, l, a) + '\n')

        elif menu == 3:
            intensity = int(input("Intensity"))
            duration = int(input("What was the duration in seconds?"))
            print('Energy Usage: %.2f' % calculate_energy_usage(intensity, duration) + '\n')

        elif menu == 4:
            hf_work = int(input("What is your heart frequency during work?"))
            hf_rest = int(input("What is your heart frequency in rest?"))
            age = int(input("Age: "))
            intensity = int(float(input("Intensity in percentage?")))
            intensity_percentage = intensity / 100
            print('Energy Usage: %.2f' % calculate_karvanonen(hf_work, hf_rest, age, intensity_percentage) + '\n')

        elif menu == 5:
          print("The program will now close."+ '\n')
          running = False
    return
'''hello this is text'''

def calculate_bmi(weight, length_cm):
    length_m = length_cm / 100
    return weight / pow(length_m, 2)


def calculate_bmr(gender, weight, length, age):
    gender = gender.lower().replace(" ", "")
    if gender == "man":
        return 10 * weight + 6.25 * length - 5 * age + 5
    elif gender == "woman":
        return 10 * weight + 6.25 * length - 5 * age - 16
    else:
        raise Exception("Error: Gender " + gender + " does not exist")


def calculate_energy_usage(intensity, duration):
    return 0.0215 * intensity * duration


def calculate_karvanonen(hf_work, hf_rest, age, intensity_percentage):
    return (hf_work - hf_rest) / ((220 - age) - hf_rest) * intensity_percentage


menu()


