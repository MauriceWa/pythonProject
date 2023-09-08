def main():
  huurders = ["Joep", "Toby", "Bas"]

  for huurder in huurders:
    print(huurder)
  huurder_1 = {
    "naam": "Youp van leeuwen",
    "Hoeveelheid_huur": 1200,
    "locatie": "Leiden",
    "telefoon_nummers":["06346810486", "0629350163"]
  }

  huurder_2 = {
    "naam": "Toby van Berkum",
    "Hoeveelheid_huur": 800,
    "locatie": "Leiden",
    "telefoon_nummers":["06346810486", "0629350163"]
  }

  huurder_3 = {
    "naam": "Bas vaan der Veen",
    "Hoeveelheid_huur": 2100,
    "locatie": "Leiden",
    "telefoon_nummers":["06346810486", "0629350163"]
  }

  huurders_lijst = [huurder_1, huurder_2, huurder_3]

  for huurder in huurders_lijst:
    telefoon_nummers = huurder["telefoon_nummers"]
    print(huurder["naam"], huurder["Hoeveelheid_huur"],huurder["telefoon_nummers"][0])




if __name__ == '__main__':
  main()