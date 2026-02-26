# Der Einstiegspunkt.
# Hier passiert:
#     Spiel starten
#     Spieler erzeugen
#     Hauptspielschleife
#     Räume durchlaufen
#     Events triggern
#     Sieg/Niederlage prüfen

# Wichtig:
# Keine Kampflogik hier implementieren. Nur orchestrieren.
# main.py ist Dirigent, nicht Musiker.

import random

from rpg.player import Player
from rpg.world import Room


def main():
    print("Hello from text-rpg!")
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    hero = Player(name, age)

    print("You wake up to find yourself in an unfamiliar place.")
    first_room = Room(random.choice(["small", "medium", "large"]))
    second_room = Room(random.choice(["small", "medium", "large"]))
    print(first_room.description)

    print("What do you want to do?")
    print("1 - Look around")
    print("2 - Open inventory")
    print("3 - Open the door")  # this should dynamically load the entrances and exits to the room
    print("4 - Have a nap")

    while True:
        player_choice = input("Enter the number of the action you want to do")
        match player_choice:
            case "1":
                print(first_room.description)
            case "2":
                print(hero.show_inventory())
            case "3":
                print("You enter the next room")
                print(second_room.description)
            case "4":
                print("You take a short break")
                break
            case _:
                print("Chose a valid number")

    # goblin = Enemy("Goblin", 8)
    # print(goblin)


if __name__ == "__main__":
    main()
