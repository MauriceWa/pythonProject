import requests
import random

def haal_alle_spacex_launches_op(boolean):
    query = {"launch_success": boolean}
    data = requests.get("https://api.spacexdata.com/v3/launches", params=query)
    info = data.json()
    flight_nr = random.randint(0, len(info))
    mission_name = info[flight_nr].get("mission_name")
    launch_year = info[flight_nr].get("launch_year")
    flight_number = info[flight_nr].get("flight_number")
    launch_site = info[flight_nr].get("launch_site").get("site_name_long")
    launch_link = info[flight_nr].get("links").get("video_link")
    video_date_utc = info[flight_nr].get("launch_date_utc")
    mission_info_output = (f'{mission_name} in {launch_year} with flight number {flight_number}\n'
                           f'{launch_site}\n'
                           f'{launch_link}\n'
                           f'{video_date_utc}')
    print(mission_info_output)

def geef_lanceringen_weer():
    print("appel")


true_or_false = input("").lower()
haal_alle_spacex_launches_op(true_or_false)
