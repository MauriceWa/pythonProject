def lees_helden_uit_bestand():
    helden_lijst = []
    with open("helden.txt", "r") as bestand:
        for info in bestand:
            held = info.strip().split(";")
            helden_dict = {
                'naam': held[0],
                'kracht': int(held[1]),
                'verdediging': int(held[2]),
                'aanvallen': int(held[3]),
                'beschrijving': held[4]
            }
            helden_lijst.append(helden_dict)
        return helden_lijst


def lees_vijanden_uit_bestand():
    vijanden_lijst = []
    with open("vijanden.txt", "r") as bestand:
        for info in bestand:
            vijand = info.strip().split(";")
            vijand_dict = {
                'naam': vijand[0],
                'kracht': int(vijand[1]),
                'verdediging': int(vijand[2]),
                'aanvallen': int(vijand[3]),
                'verliest_tegen': vijand[4]
            }
            vijanden_lijst.append(vijand_dict)
        return vijanden_lijst


def strijd(held, vijanden_opties):
    for vijand in vijanden_opties:
        helden_score = held['kracht'] * held['aanvallen'] - vijand['verdediging']
        vijand_score = vijand['kracht'] * vijand['aanvallen'] - held['verdediging']

        print(f"{held['naam']} vecht tegen {vijand['naam']}")
        print(f"{helden_score} vs {vijand_score}")

        if vijand['verliest_tegen'] == held['naam']:
            print("deze held is te machtig voor deze vijand, en wint automatisch")

        elif helden_score > vijand_score:
            print("De held verslaat heldhaftig de vijand")

        elif helden_score == vijand_score:
            print("Vijand vernietigt de held")

        elif helden_score < vijand_score:
            print("Vijand vernietigd de held")


def toon_held_informatie(held):
    print(f"Naam: {held['naam']}\nBeschrijving: {held['beschrijving']}\nKracht: {held['kracht']}\n"
          f"Verdediging: {held['verdediging']}\nAanvallen: {held['aanvallen']}")


def main():
    helden = lees_helden_uit_bestand()
    vijanden = lees_vijanden_uit_bestand()
    keuze_menu = int(input("Welkom bij het gevecht in Middel Aarde, kies je strijder:\n1. Legolas\n2. Gimli\n"
                           "3. Aragorn\n"))
    app_draait = True

    while app_draait:
        if keuze_menu == 1:
            held1 = helden[0]
            held_informatie_input = input("Wil je informatie weten over jouw gekozen held? Type Ja of Nee\n").lower()
            if held_informatie_input == 'ja':
                toon_held_informatie(held1)
            print("Het gevecht van goed gaat beginnen...")
            strijd(held1, vijanden)
            app_draait = False

        elif keuze_menu == 2:
            held2 = helden[1]
            held_informatie_input = input("Wil je informatie weten over jouw gekozen held? Type Ja of Nee\n").lower()
            if held_informatie_input == 'ja':
                toon_held_informatie(held2)
            print("Het gevecht van goed gaat beginnen...")
            strijd(held2, vijanden)
            app_draait = False

        elif keuze_menu == 3:
            held3 = helden[2]
            held_informatie_input = input("Wil je informatie weten over jouw gekozen held? Type Ja of Nee\n").lower()
            if held_informatie_input == 'ja':
                toon_held_informatie(held3)
            print("Het gevecht van goed gaat beginnen...")
            strijd(held3, vijanden)
            app_draait = False


if __name__ == '__main__':
    main()