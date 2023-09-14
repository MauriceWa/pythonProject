
def menu():
  running = True
  while running:
    menu = int(input(
      "What do you want to calculate?" + '\n' + "1. BMI" + '\n' + "2. BMR" + '\n' + "3. Energy usage" + '\n' + "4. Karvanonen"))
    if menu == 1:
      w = int(input("Weight:"))
      l = int(input("Length:"))
      print('bmi: %.2f' % calculate_bmi(w, l)+'\n')

    elif menu == 2:
      gender = input("Gender: ")
      a = int(input("Age: "))
      w = int(input("Weight:"))
      l = int(input("Length:"))
      print('bmr: %.2f' % calculate_bmr(gender, w, l, a)+'\n')

    elif menu == 3:
      intensity = int(input("Intensity"))
      duration = int(input())
      print('bmr: %.2f' % calculate_energy_usage(intensity, duration)+'\n')
  return



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

# while life:
#   keuze_menu = int(input(
#     "Kies 1 als je een programmeerterm wilt opzoeken, kies 2 als je nog een term wilt toevoegen, kies 3 als je wilt stoppen"))
#   if keuze_menu == 1:
#     gebruiker = input("Welke term wil je weten?")
#     if gebruiker in programmeer_termen.keys():
#       print(programmeer_termen[gebruiker] + '\n')
#     else:
#       print("Helaas, deze term staat niet in het woordenboek.")
#
#   elif keuze_menu == 2:
#     nieuwe_term = input("Voeg een nieuwe term toe.")
#     nieuwe_term_betekenis = input("Geef de betekenis van de nieuwe term")
#     programmeer_termen.update({nieuwe_term: nieuwe_term_betekenis})
#     print('"' + nieuwe_term + ': ' + nieuwe_term_betekenis + '" was added to the dictionary.''\n')
#
#   elif keuze_menu == 3:
#     print("The program will close.")
#     life = False
#
# return
