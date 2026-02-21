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

from rpg.enemy import Enemy
from rpg.player import Player


def main():
    print("Hello from text-rpg!")

    name = input("Enter your name: ")
    age = input("Enter your age: ")

    hero = Player(name, age)
    print(hero)

    goblin = Enemy("Goblin", 8)
    print(goblin)


if __name__ == "__main__":
    main()
