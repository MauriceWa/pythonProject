
def print_main_menu():
  print("Thanks for the information, choose one of the following options:")

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



def main():


  #gewicht, lengte in m, leeftijd,
  weight = input("What is your weight?")
  age = int(input("What is your age?"))
  length_in_m = int(float(input("What is your length in meter?")))
  app_running = True


  while app_running:
  if choice == 1:

  # hartslag alleen vragen in voor de formule van karvonen
  if __name__ == "__main__":
    main()
