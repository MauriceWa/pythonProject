import requests
from bs4 import BeautifulSoup


def scrape_nos():
    """
    Deze functie haalt de titels van NOS artikelen op, samen met de URL naar de artikel paginas.
    """
    # maak een variabele met daarin de website url.
    url = "https://nos.nl/"

    # maak een variabele waarmee een GET-request naar de site wordt gedaan d.m.v. de requests library
    response = requests.get(url)

    # parseer de response van de GET-request en sla op in een variabele d.m.v. BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # sla de class-code van de elementen die je wilt hebben op als string variabele. Let op, deze verandert vaak!
    HTML_class_van_koppen = "sc-6c728684-1 eDtwUh"

    # Pak alle koppen van de NOS pagina
    koppen = soup.findAll("a", {"class": HTML_class_van_koppen})
    print(koppen)

    for kop in koppen:
        # haal de url uit de kop en print die uit
        pagina_url = url + kop.get("href")
        print(pagina_url)

        # haal de titel van de kop op en print die uit
        artikel_titel = kop.find("h2").text
        print(artikel_titel)

        # geef voorbeeld van hoe je die informatie kunt omzetten naar een insert into statement.
        sql = f"INSERT INTO NOS (url, titel) VALUES ('{pagina_url}', '{artikel_titel}');"
        print("")
        print(sql)


if __name__ == '__main__':
    scrape_nos()