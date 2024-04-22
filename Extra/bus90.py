import requests
from bs4 import BeautifulSoup


def scrape_nos():
    """
    Deze functie haalt de titels van NOS artikelen op, samen met de URL naar de artikel paginas.
    """
    # maak een variabele met daarin de website url.
    url = "https://www.bing.com/search?q="
    url_input = input()
    url_input_change = url_input.strip().replace(" ", "+")
    full_url = f"{url}{url_input_change}"
    print(full_url)

    response = requests.get(full_url)

    # parseer de response van de GET-request en sla op in een variabele d.m.v. BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    # Pak alle koppen van de NOS pagina
    koppen = soup.findAll("h2")
    print(f"koppen: {koppen}")

    for kop in koppen:
        # haal de url uit de kop en print die uit
        pagina_url = full_url + kop.find("a").get('href')
        print(pagina_url)

        # haal de titel van de kop op en print die uit
        artikel_titel = kop.find('a').text
        print(artikel_titel)

        # geef voorbeeld van hoe je die informatie kunt omzetten naar een insert into statement.
        # sql = f"INSERT INTO nos (url, titel) VALUES ('{pagina_url}', '{artikel_titel}');"


if __name__ == '__main__':
    scrape_nos()