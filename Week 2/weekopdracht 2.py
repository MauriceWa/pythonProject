def main():
    # variabele, functie, algoritme, ide, loop, dictionary, lijst, conditie, recursie
  woordjes = {
    "variabele": "een naam waarde combinatie die de computer kan gebruiken.",
    "functie": "stukjes code die buiten de rest van de script worden geschreven",
    "algoritme": "een instructie, een stukje code, om een probleem om te lossen",
    "ide": "een softwaretoepassing waarmee ontwikkelaars code binnen één programma kunnen maken, bewerken en compileren",
    "loop": "delen in de programmacode die keer naar keer herhaald worden",
    "dictionary": "een datatype waarin je meerdere datapunten op kunt slaan met key-value paren",
    "lijst": "een functie om data op te slaan in python",
    "conditie": "maakt gebruik van termen om een progamma te vorderen of te stoppen",
    "recursie": "een methode waar de oplossing van een probleem afhangt van oplossingen van kleinere identieke problemen, in tegenstelling tot iteratie",
  }
  user_input = input("Voer een progammeerterm in:").lower()
  if user_input in woordjes.keys():
    print (woordjes[user_input])

if __name__ == "__main__":
  main()
