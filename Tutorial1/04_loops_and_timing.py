import time
ship_name = input("What is your space ship's name? ")
captain = input("Welcome aboard {}, Captain. What is your name? ".format(ship_name))
planets = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter",
           "Saturn", "Uranus", "Neptune", "Pluto"]
location = 3
while location != 0:
    print("--------Captain's Log for {}--------".format(ship_name))
    print("LOCATION: {}".format(planets[location]))
    print("PLANETS:")
    for i in range(len(planets)):
        print("{}: {}".format(i, planets[i]))
    destination = int(input("Where would you like to go, {}? ".format(captain)))
    if destination == location:
        print("We are already on {}, so we can't travel there.".format(planets[location]))
    else:
        eta = abs(destination - location) ** 2 / 2
        print("Traveling from {} to {}. It will take {:.1f} years.".format(
            planets[location], planets[destination], eta))
        time.sleep(eta)
        location = destination
        print("You have arrived at {}!".format(planets[location]))