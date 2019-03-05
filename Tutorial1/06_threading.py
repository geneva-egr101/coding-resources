import time
import threading
def systems_check(eta, captain):
    if eta >= 8:
        time.sleep(eta / 2)
        print("All systems are nominal, {}.".format(captain))
ship_name = input("What is your space ship's name? ")
captain = input("Welcome aboard {}, Captain. What is your name? ".format(ship_name))
planets = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter",
           "Saturn", "Uranus", "Neptune", "Pluto"]
def travel(ship_name, captain, location):
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
            threading.Thread(target=systems_check, args=[eta, captain]).start()
            time.sleep(eta)
            location = destination
            print("You have arrived at {}!".format(planets[location]))
travel(ship_name, captain, 3)