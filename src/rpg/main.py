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
# noch eine Zeile Kommentar
# Und hier noch einer :)
# yo was geht ab

import random

from rpg.enemy import Enemy
from rpg.player import Player
from rpg.world import Room


def main():
    print("Hello from text-rpg!")
    print(
        "You wake up to find yourself in an unfamiliar place. You stand up and have a look around."
    )
    first_room = Room(random.choice(["small", "medium", "large"]))
    print(first_room.description)

    name = input("Enter your name: ")
    age = input("Enter your age: ")

    hero = Player(name, age)
    print(hero)

    print(hero.show_inventory())

    goblin = Enemy("Goblin", 8)
    print(goblin)


if __name__ == "__main__":
    main()
