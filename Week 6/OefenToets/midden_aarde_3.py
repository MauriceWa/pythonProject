vijanden = []


def lees_helden_uit_bestand():
    with open("helden.txt") as bestand:
        helden_lijst = []
        data = bestand.readlines()
        for held in bestand:
            held.strip().split(";")
            dict = {
                "naam":held[0],
                "kracht":held[1],
                "verdediging":held[2],
                "aanvallen":held[3],
                "beschrijving":held[4]
            }
            helden_lijst.append(dict)
    return helden_lijst

def lees_vijanden_uit_bestand():
    with open("helden.txt") as bestand:
        vijanden_lijst = []
        data = bestand.readlines()
        for vijand in bestand:
            vijand.strip().split(";")
            dict = {
                "naam":vijand[0],
                "kracht":vijand[1],
                "verdediging":vijand[2],
                "aanvallen":vijand[3],
                "beschrijving":vijand[4]
            }
            vijanden_lijst.append(dict)
    return vijanden_lijst
def toon_held_informatie(held):

def strijd(held, vijanden):


def main():
    program = True
    helden = lees_helden_uit_bestand()
    vijanden = lees_vijanden_uit_bestand()

    print("Welkom bij het gevecht in Middel Aarde, kies je strijder:"+ "\n" "1. Legolas" + "\n" + "2. Gimli"
           + "\n" + "3. Aragorn" + "\n")
    keuze = int(input())
    if keuze == 1:
        held1 = helden[0]
        print("Wil je meer informatie over jouw gekozen held? Type ja of nee" + "\n")
        tweede_keuze = input()
        if tweede_keuze == "ja":
            print(toon_held_informatie(held1))
        else:
            print("Het gevecht van goed gaat beginnen...")
    if keuze == 2:
        print("Wil je meer informatie over jouw gekozen held? Type ja of nee" + "\n")
        tweede_keuze = input()
        if tweede_keuze == "ja":
            print(toon_held_informatie(1))
        else:
            print("Het gevecht van goed gaat beginnen...")
    if keuze == 3:
        print("Wil je meer informatie over jouw gekozen held? Type ja of nee" + "\n")
        tweede_keuze = input()
        if tweede_keuze == "ja":
            print(toon_held_informatie(1))
        else:
            print("Het gevecht van goed gaat beginnen...")


if __name__ == "__main__":
    main()