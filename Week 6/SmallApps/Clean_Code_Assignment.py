def bereken_som():
    nummer1 = float(input("Voer alstublieft alleen positieve getallen in: "))
    nummer2 = float(input("Voer nu alstublieft het tweede positieve getal in: "))
    if nummer1 < 0 or nummer2 < 0:
        print("Negatieve getallen worden niet ondersteund.")
    else:
        print(f"""Het resultaat van de berekening is: {float(nummer1 + nummer2)}""")


bereken_som()
