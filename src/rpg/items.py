# Definiert Items.

#     Heiltrank
#     Waffe
#     ggf. Basisklasse Item

# Verantwortung:

#     Effekt definieren
#     Anwendung auf Spieler, Gegner oder Welt


class Potion:
    def __init__(self, name, value, size):
        self.name = name
        self.value = value
        self.size = size

    def inspect(self):
        print(f"It looks like you can drink this {self.size} bottle of {self.name}")

    def drink_potion(self):
        print("You drink the potion, and wonder what effect it will have on you")


class HealingPotion(Potion):
    def __init__(self, name, value, size, hitpoints):
        super().__init__(name, value, size)
        self.hitpoints = hitpoints

    def drink_potion(self):
        print(f"You drink the {self.size} healing potion, and feel better immmediately")
        return self.hitpoints


class Poison(Potion):
    def __init__(self, name, value, size, damage):
        super().__init__(name, value, size)
        self.damage = damage

    def drink_potion(self):
        print(f"You drink the {self.size} bottle of poison, and don't feel so good anymore")
        return self.damage


if __name__ == "__main__":
    red_potion = HealingPotion("Red potion", 5, "small", 12)

    red_potion.inspect()
    red_potion.drink_potion()

    green_potion = Poison("Cyanide", 8, "medium", 9)
    green_potion.inspect()
    green_potion.drink_potion()
