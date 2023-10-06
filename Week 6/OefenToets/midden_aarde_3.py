vijanden = []


def lees_helden_uit_bestand():
    with open("helden.txt").read().splitlines() as bestand:
        


def lees_vijanden_uit_bestand():
    bestand = open("vijanden.txt", "r")

    lurtz = {"Naam":"Lurtz"}, \
                  {"kracht":"5"},\
                  {"verdediging":"5"},\
                  {"aanvallen":"2"},\
                  {"verlist tegen":"Aragorn"}

    witch_king = {"Naam":"Witch King"}, \
                  {"kracht":"7"},\
                  {"verdediging":"5"},\
                  {"aanvallen":"2"},\
                  {"verlist tegen":"Legolas"}

    cave_troll = {"Naam":"Cave Troll"}, \
                  {"kracht":"10"},\
                  {"verdediging":"8"},\
                  {"aanvallen":"3"},\
                  {"verlist tegen":"Gimli"}
    vijanden =[lurtz,witch_king,cave_troll]
    print(vijanden)
    bestand.close()
def toon_held_informatie(Aragorn):
    Aragorn = {"Naam":"Aragorn"}, \
                  {"kracht":"8"},\
                  {"verdediging":"6"},\
                  {"aanvallen":"3"},\
                  {"beschrijving":"Aragorn zoon van Arathorn, dwaler uit het noorden"}
    print(Aragorn)

def strijd():
    Aragorn = {"Naam": "Aragorn"}, \
              {"kracht": "8"}, \
              {"verdediging": "6"}, \
              {"aanvallen": "3"}, \
              {"beschrijving": "Aragorn zoon van Arathorn, dwaler uit het noorden"}

    lurtz = {"Naam":"Lurtz"}, \
                  {"kracht":"5"},\
                  {"verdediging":"5"},\
                  {"aanvallen":"2"},\
                  {"verlist tegen":"Aragorn"}

    witch_king = {"Naam":"Witch King"}, \
                  {"kracht":"7"},\
                  {"verdediging":"5"},\
                  {"aanvallen":"2"},\
                  {"verlist tegen":"Legolas"}

    cave_troll = {"Naam":"Cave Troll"}, \
                  {"kracht":"10"},\
                  {"verdediging":"8"},\
                  {"aanvallen":"3"},\
                  {"verlist tegen":"Gimli"}
    vijanden =[lurtz, witch_king, cave_troll]
    for held in Aragorn:
        held_score = print(Aragorn["kracht"])

def main():
    program = True
    print("Welkom bij het gevecht in Middel Aarde, kies je strijder:"+ "\n" "1. Legolas" + "\n" + "2. Gimli"
           + "\n" + "3. Aragorn" + "\n")
    keuze = int(input())
    if keuze == 1:
        print("Wil je meer informatie over jouw gekozen held? Type ja of nee" + "\n")
        tweede_keuze = input()
        if tweede_keuze == "ja":
            print(toon_held_informatie(1))
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