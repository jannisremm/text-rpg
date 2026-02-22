# Definiert Items.

#     Heiltrank
#     Waffe
#     ggf. Basisklasse Item

# Verantwortung:

#     Effekt definieren
#     Anwendung auf Spieler, Gegner oder Welt


class Item:
    def __init__(self, name) -> None:
        self.name = name
