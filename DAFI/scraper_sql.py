import requests
import psycopg2
from bs4 import BeautifulSoup


def fetch_database():
    # database gegevens
    connection = psycopg2.connect(
        host='localhost',
        port='5432',
        database='ziekenhuis',
        user='postgres',
        password='postgres'
    )

    # cursor aanmaken
    cursor_var = connection.cursor()

    # de query opstellen
    query = "SELECT wetensch_naam FROM medicijn"

    # de query uitvoeren
    cursor_var.execute(query)

    # resultaten weergeven
    results = cursor_var.fetchall()

    # cursor sluiten
    cursor_var.close()

    # resultaten weergeven
    print(results)
    return results


def write_to_database(medicijn, data):
    # database gegevens
    connection = psycopg2.connect(
        host='localhost',
        port='5432',
        database='ziekenhuis',
        user='postgres',
        password='postgres'
    )

    # cursor aanmaken
    cursor_var = connection.cursor()

    # de query opstellen
    query = f"UPDATE medicijn SET bijwerking = '{data}' WHERE wetensch_naam = '{medicijn}'"
    print(query)

    # de query uitvoeren
    cursor_var.execute(query)

    # resultaten weergeven
    connection.commit()

    # cursor sluiten
    cursor_var.close()


def scrape():

    medicijnen = fetch_database()

    for indx, zoekterm in enumerate(medicijnen):
        url = f"https://www.apotheek.nl/medicijnen/{zoekterm[0].strip().lower().replace(' ','')}#wat-zijn-mogelijke-bijwerkingen"
        print(f"link: {url}")

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        koppen = soup.find_all('span', class_='sideEffectsItem_button__V-L1C')
        # print(f"koppen: {koppen}") # Voor debuggen
        bijwerkingen = []

        for idx, kop in enumerate(koppen):
            try:
                artikel_titel = kop.find('strong').text
                if artikel_titel.split(' ')[0] == 'Bij':
                    pass
                else:
                    bijwerkingen.append(artikel_titel.strip().replace('.', '').replace(',', ''))
            except AttributeError:
                print(f"\tError in bijwerking {idx}. Bijwerking 1 niet toegevoegd aan lijst!")
            # geef voorbeeld van hoe je die informatie kunt omzetten naar een insert into statement.
            # sql = f"INSERT INTO nos (url, titel) VALUES ('{pagina_url}', '{artikel_titel}');"
        # print(f"bijwerkingen: {bijwerkingen}")

        sql_bijwerkingen = ''

        for idx, bijwerking in enumerate(bijwerkingen):
            sql_bijwerkingen += f"{bijwerking}"
            if idx + 1 != len(bijwerkingen):
                sql_bijwerkingen += " | "

        print(f"medicijn {medicijnen[indx][0]} bijwerkingen {sql_bijwerkingen}")
        write_to_database(medicijnen[indx][0], sql_bijwerkingen)


if __name__ == '__main__':
    scrape()