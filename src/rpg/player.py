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

    def __str__(self):
        return f"Hi I am {self.name} and I am {self.age} years old!"
