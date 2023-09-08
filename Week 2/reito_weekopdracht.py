def main():
  life = True
  programmeer_termen = {
    "Functie": "Een functie is een blok code in een programma dat een specifieke taak uitvoert wanneer het wordt aangeroepen. Functies worden gebruikt om herbruikbare stukken code te creëren.",
    "Algoritme": "Een algoritme is een reeks stappen of instructies die worden gevolgd om een specifieke taak uit te voeren of een probleem op te lossen. Algoritmen zijn de basis van programmeerlogica.",
    "IDE": "Een IDE is een softwaretoepassing die programmeurs helpt bij het ontwikkelen van software. Het bevat doorgaans code-editorfuncties, een debugger en tools voor het bouwen en uitvoeren van programma's.",
    "Loop": "Een lus is een programmeerconstructie die wordt gebruikt om een bepaald blok code herhaaldelijk uit te voeren zolang een bepaalde voorwaarde waar is. Er zijn verschillende soorten lussen, zoals de for-lus en de while-lus.",
    "Dictionary": "Een dictionary (of woordenboek) is een gegevensstructuur in Python die bestaat uit een verzameling sleutel-waardeparen. Het maakt het mogelijk om waarden op te slaan en op te halen op basis van een unieke sleutel.",
    "Lijst": "Een lijst is een gegevensstructuur in Python die een geordende verzameling van elementen kan bevatten. Lijsten kunnen elementen van verschillende datatypes bevatten en worden vaak gebruikt om meerdere waarden in één variabele op te slaan.",
    "Conditie": "Een conditie is een expressie of waarde die wordt geëvalueerd om te bepalen of bepaalde acties moeten worden uitgevoerd. In programmeercontexten wordt vaak gebruikgemaakt van condities in beslissingsstructuren, zoals if-statements.",
    "Recursie": "Recursie is een programmeertechniek waarbij een functie zichzelf aanroept om een bepaalde taak uit te voeren. Dit kan nuttig zijn voor problemen die van nature recursief van aard zijn, zoals het berekenen van de faculteit van een getal of het doorzoeken van complexe gegevensstructuren zoals bomen.",
  }

  while life:
    keuze_menu = int(input(
      "Kies 1 als je een programmeerterm wilt opzoeken, kies 2 als je nog een term wilt toevoegen, kies 3 als je wilt stoppen"))
    if keuze_menu == 1:
      gebruiker = input("Welke term wil je weten?")
      if gebruiker in programmeer_termen.keys():
        print(programmeer_termen[gebruiker]+'\n')
      else:
        print("Helaas, deze term staat niet in het woordenboek.")

    elif keuze_menu == 2:
      nieuwe_term = input("Voeg een nieuwe term toe.")
      nieuwe_term_betekenis = input("Geef de betekenis van de nieuwe term")
      programmeer_termen.update({nieuwe_term: nieuwe_term_betekenis})
      print('"' + nieuwe_term + ': ' + nieuwe_term_betekenis + '" was added to the dictionary.''\n')

    elif keuze_menu == 3:
      print("The program will close.")
      life = False

if __name__ == '__main__':
  main()