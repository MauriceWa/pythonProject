ns = [{"Location a": "Leiden Centraal", "Location b": "Leiden Lammenschans", "duration": "2 minutes"},
      {"Location a": "Leiden Lammenschans", "Location b": "Alphen aan de Rijn", "duration": "10 minutes"},
      {"Location a": "Alphen aan de Rijn", "Locatie b": "Woerden", "duur": "15 minutes"},
      {"Location a": "Leiden Lammenschans", "Location b": "Alphen aan de Rijn", "duration": "15 minutes"},
      {'Location a': "Woerden", "Location b": "Utrecht", "duration": "20 minutes"}]
route_list = ["Leiden Centraal goes to Leiden Lammenschans and takes 2 minutes",
"Leiden Lammenschans goes to Alphen aan de Rijn and takes 10 minutes",
"Alphen aan de Rijn goes to Woerden and takes 15 minutes",
"Leiden Lammenschans goes to Alphen aan de Rijn and takes 10 minutes",
"Woerden goes to Utrecht and takes 20 minutes"]

def plan_route(Location_a, Location_b):
    Running = True
    choice_menu = input("What would you like to do?" + "\n" + "1. Plan route" + "\n" + "2. Look for possible routes" +
    "\n"+ "3. Close program")
 #   if choice_menu == 1:

def write_route_away():
    print("appel")


def show_routes(route_list):
    for route in route_list:
        print(route)



def main():
    routes = ["Leiden Centraal goes to Leiden Lammenschans and takes 2 minutes",
     "Leiden Lammenschans goes to Alphen aan de Rijn and takes 10 minutes",
     "Alphen aan de Rijn goes to Woerden and takes 15 minutes",
     "Leiden Lammenschans goes to Alphen aan de Rijn and takes 10 minutes",
     "Woerden goes to Utrecht and takes 20 minutes"]
    show_routes(routes)


if __name__ == "__main__":
        main()
