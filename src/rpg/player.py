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
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
