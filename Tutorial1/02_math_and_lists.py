ship_name = input("What is your space ship's name? ")
captain = input("Welcome aboard {}, Captain. What is your name? ".format(ship_name))
planets = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter",
           "Saturn", "Uranus", "Neptune", "Pluto"]
location = 3
print("--------Captain's Log for {}--------".format(ship_name))
print("LOCATION: {}".format(planets[location]))
print("PLANETS: {}".format(planets))
destination = int(input("Where would you like to go, {}? ".format(captain)))
eta = abs(destination - location) ** 2 / 2
print("Traveling from {} to {}. It will take {:.1f} years.".format(
      planets[location], planets[destination], eta))