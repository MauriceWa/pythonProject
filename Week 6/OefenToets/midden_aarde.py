def lees_helden_uit_bestand():
    helden_lijst = []
    with open("helden.txt") as bestand:
        data = bestand.readlines()
        for resources in data:
                held = resources.strip().split(";")
                dictionary = {
                    "naam": held[0],
                    "kracht": int(held[1]),
                    "verdediging": int(held[2]),
                    "aanvallen": int(held[3]),
                    "beschrijving": held[4]
                }
                helden_lijst.append(dictionary)
    return helden_lijst


def lees_vijanden_uit_bestand():
    vijanden_lijst = []
    with open("vijanden.txt") as bestand:
        data = bestand.readlines()
        for resources in data:
            vijand = resources.strip().split(";")
            dictionary = {
                    "naam": vijand[0],
                    "kracht": int(vijand[1]),
                    "verdediging": int(vijand[2]),
                    "aanvallen": int(vijand[3]),
                    "verliest_tegen": vijand[4]
            }
            vijanden_lijst.append(dictionary)
    return vijanden_lijst


def strijd(held, vijanden):
    for vijand in vijanden:
        helden_score = held['kracht'] * held['aanvallen'] - vijand['verdediging']
        vijanden_score = vijand['kracht'] * vijand['aanvallen'] - held['verdediging']

        print(f'{held["naam"]} vecht tegen {vijand["naam"]}')
        print(f'{helden_score} vs {vijanden_score}')

        if vijand['verliest_tegen'] == held["naam"]:
            print("Deze held is te machtig voor deze vijand, en wint automatisch")

        elif helden_score > vijanden_score:
            print("De held verslaat heldhaftig de vijand")

        elif helden_score == vijanden_score:
            print("Vijand vernietigd de held")

        elif vijanden_score > helden_score:
            print("Vijand vernietigd de held")


def toon_held_informatie(held):
    print(f'Naam: {held["naam"]} \nBeschrijving: {held["beschrijving"]}\nKracht: {held["kracht"]}'
          f'\nVerdediging: {held["verdediging"]}\nAanvallen: {held["aanvallen"]}')


def main():
    applicatie_draait = True
    helden = (lees_helden_uit_bestand())
    vijanden = (lees_vijanden_uit_bestand())

    while applicatie_draait:
        print("Welkom bij het gevecht in Middel Aarde, kies je strijder:\n1. Legolas\n2. Gimli\n"
              "3. Aragorn")
        keuzes = int(input())
        if keuzes == 1:
            held1 = helden[0]
            meer_weten = input("Wil je informatie weten over jouw gekozen held? Type ja of nee")
            if meer_weten == "ja":
                toon_held_informatie(held1)
                print("Het gevecht van goed gaat beginnen...")
                strijd(held1, vijanden)
                applicatie_draait = False
            if meer_weten == "nee":
                print("Het gevecht van goed gaat beginnen...")
                strijd(held1, vijanden)
                applicatie_draait = False

        if keuzes == 2:
            held2 = helden[1]
            meer_weten = input("Wil je informatie weten over jouw gekozen held? Type ja of nee")
            if meer_weten == "ja":
                toon_held_informatie(held2)
                print("Het gevecht van goed gaat beginnen...")
                strijd(held2, vijanden)
                applicatie_draait = False
            if meer_weten == "nee":
                print("Het gevecht van goed gaat beginnen...")
                strijd(held2, vijanden)
                applicatie_draait = False

        if keuzes == 3:
            held3 = helden[2]
            meer_weten = input("Wil je informatie weten over jouw gekozen held? Type ja of nee")
            if meer_weten == "ja":
                toon_held_informatie(held3)
                print("Het gevecht van goed gaat beginnen...")
                strijd(held3, vijanden)
                applicatie_draait = False
            if meer_weten == "nee":
                print("Het gevecht van goed gaat beginnen...")
                strijd(held3, vijanden)
                applicatie_draait = False


if __name__ == "__main__":
    main()
