# Definiert die Spieler-Klasse.

# Verantwortung:
#     Name
#     HP
#     Angriff
#     Verteidigung
#     Inventar
# Methoden wie:
#     take_damage()
#     heal()
#     add_item()

# Hier lebt die Identität des Spielers.


class Player:
    hitpoints = 100
    inventory = ["Clothes", "Shoes", "Hat", "Gloves"]

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hi I am {self.name} and I am {self.age} years old!"

    def show_inventory(self):
        string = " ".join(self.inventory)
        return string
