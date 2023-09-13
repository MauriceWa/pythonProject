def calculate_bmi(weight, length):
  return (weight/pow(length, 2))


def calculate_bmr(gender, weight, length, age):
  gender = gender.lower().replace("", " ")
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
print(calculate_karvanonen(180, 60,18,100 ))




print(calculate_bmr("Tan", 80, 182, 20))


def main():


  if __name__ == "__main__":
    main()