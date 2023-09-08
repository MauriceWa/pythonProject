def main():
  # variabele, functie, algoritme, ide, loop, dictionary, lijst, conditie, recursie

  woordje_1 = {
    "woordje": "variabele",
    "definitie": "een naam waarde combinatie die de computer kan gebruiken."
  }

  woordje_2 = {
    "woordje": "functie",
    "definitie": "stukjes code die buiten de rest van de script worden geschreven"
  }
  woordje_3 = {
    "woordje": "algoritme",
    "definitie": "een instructie, een stukje code, om een probleem om te lossen"
  }
  woordje_4 = {
    "woordje": "ide",
    "definitie": "een softwaretoepassing waarmee ontwikkelaars code binnen één programma kunnen maken, bewerken en compileren"
  }
  woordje_5 = {
    "woordje": "loop",
    "definitie": "delen in de programmacode die keer naar keer herhaald worden"
  }
  woordje_6 = {
    "woordje": "dictionary",
    "definitie": "een datatype waarin je meerdere datapunten op kunt slaan met key-value paren"
  }
  woordje_7 = {
    "woordje": "lijst",
    "definitie": "een functie om data op te slaan in python"
  }
  woordje_8 = {
    "woordje": "conditie",
    "definitie": "maakt gebruik van termen om een progamma te vorderen of te stoppen"
  }
  woordje_9 = {
    "recursie": "een methode waar de oplossing van een probleem afhangt van oplossingen van kleinere identieke problemen, in tegenstelling tot iteratie"
  }
  for woordje in progammeer_woorden:
    user_input = input("Voer een progammeerterm in:").lower()
    print(user_input)
    print(woordje)
    if user_input in woordje:
      print (woordje[user_input])
  # variabele, functie, algoritme, ide, loop, dictionary, lijst, conditie, recursie
if __name__ == "__main__":
  main()
