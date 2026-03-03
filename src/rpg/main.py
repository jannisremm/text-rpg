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


from rpg.player import Player
from rpg.world import generate_level


def main():
    print("Hello from text-rpg!")
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    hero = Player(name, age)

    print("You wake up to find yourself in an unfamiliar place.")
    level = generate_level(5)
    current_room = 0
    number_of_rooms = len(level)

    print("What do you want to do?")
    print("1 - Look around")
    print("2 - Open inventory")
    print("3 - Open the door in front of you")
    print("4 - Go back to the previous room")
    print("5 - Have a nap")

    while True:
        player_choice = input("Enter the number of the action you want to do")
        match player_choice:
            case "1":
                print(level[current_room].get_ai_description())
            case "2":
                print(hero.show_inventory())
            case "3":
                if current_room == number_of_rooms - 1:
                    print("This room only has the door you just came from,")
                    print("there must be some other way to get out of here")
                else:
                    print("You open the door in front of you and enter the next room")
                    current_room += 1
            case "4":
                if current_room == 0:
                    print("This is the room you woke up in, there is only the door in front of you")
                else:
                    current_room -= 1
                    print("You go back into the room you just came from")
            case "5":
                print("You take a short break")
                break
            case _:
                print("Chose a valid number")

    # goblin = Enemy("Goblin", 8)
    # print(goblin)


if __name__ == "__main__":
    main()
