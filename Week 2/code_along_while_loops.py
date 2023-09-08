teller = 0
programma_draait = True
while programma_draait:
  gebruikers_input = input("Wil je nog door gaan? (ja/nee)")

  if gebruikers_input == "ja":
    print("We gaan gewoon door!")
  else:
    print("Dan gaan we stopppen")
    programma_draait = False