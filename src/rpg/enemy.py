# Definiert Gegner.
#     Name
#     HP
#     Angriff
#     evtl. Spezialfähigkeiten (später)

# Kann als Klasse oder Factory-Funktion umgesetzt werden.
# Später könnte man hier Gegner-Typen oder Zufallsgegner definieren.
class Enemy:
    def __init__(self, name, hit_points):
        self.name = name
        self.hit_points = hit_points

    def __str__(self):
        return f"I am a dangerous {self.name} and have {self.hit_points} hit points"
