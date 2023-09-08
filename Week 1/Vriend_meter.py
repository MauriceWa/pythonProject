def main():
    keuze = None
    while keuze not in [1, 0]:
        keuze = int(float(input("Houd je van sport? 1 of 0")))


    keuze2 = None
    while keuze2 not in [1, 0]:
        keuze2 = int(float(input("Houd je van vechten? 1 of 0")))

    keuze3 = None
    while keuze3 not in [1, 0]:
        keuze3 = int(float(input("Houd je van feesten? 1 of 0")))

    keuze4 = None
    while keuze4 not in [1, 0]:
        keuze4 = int(float(input("Houd je van vissen? 1 of 0")))

    keuze5 = None
    while keuze5 not in [1, 0]:
        keuze5 = int(float(input("Houd je van calisthenics? 1 of 0")))

    aantal_punten = keuze + keuze2 + keuze3 + keuze4 + keuze5

    if int(aantal_punten) > 3:
        print("Wij kunnen vrienden zijn.")
    else:
        print("Zoek iemand anders.")




if __name__ == '__main__':
    main()