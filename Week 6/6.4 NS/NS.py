Running = True


def plan_route(location_a, location_b, route_list):
    found_route = False

    for route in route_list:
        if route["Location a"] == location_a and route["Location b"] == location_b:
            found_route = True
            print(f"Found a route between{location_a} and {location_b}:")
            print(f"The duration is {route['duration']}")

        if not found_route:
            print(f"No route found from {location_a} towards {location_b} ")

    return found_route


def write_route_away(route_data):
    print("appel")


def show_routes(route_list):
    for route in route_list:
        print(route)


def main():
    route_list = ["Leiden Centraal goes to Leiden Lammenschans and takes 2 minutes",
                  "Leiden Lammenschans goes to Alphen aan de Rijn and takes 10 minutes",
                  "Alphen aan de Rijn goes to Woerden and takes 15 minutes",
                  "Leiden Lammenschans goes to Alphen aan de Rijn and takes 10 minutes",
                  "Woerden goes to Utrecht and takes 20 minutes"]
    routes_dict = [
        {"Location a": "Leiden Centraal", "Location b": "Leiden Lammenschans", "duration": "2 minutes"},
        {"Location a": "Leiden Lammenschans", "Location b": "Alphen aan de Rijn", "duration": "10 minutes"},
        {"Location a": "Alphen aan de Rijn", "Location b": "Woerden", "duration": "15 minutes"},
        {"Location a": "Leiden Lammenschans", "Location b": "Alphen aan de Rijn", "duration": "15 minutes"},
        {'Location a': "Woerden", 'Location b': "Utrecht", "duration": "20 minutes"}]
    running = True
    while running:
        choice_menu = int(
            input("What would you like to do?" + "\n" + "1. Plan route" + "\n" + "2. Look for possible routes" +
                  "\n" + "3. Close program "))
        if choice_menu == 1:
            location_a = input("Where are you starting from?")
            location_b = input("Where will you depart?")
            plan_route(location_a, location_b, routes_dict)

        elif choice_menu == 2:
            show_routes(route_list)

        elif choice_menu == 3:
            running = False


if __name__ == "__main__":
    main()
