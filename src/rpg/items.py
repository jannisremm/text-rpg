# Definiert Items.

#     Heiltrank
#     Waffe
#     ggf. Basisklasse Item

# Verantwortung:

#     Effekt definieren
#     Anwendung auf Spieler, Gegner oder Welt


class Item:
    """This class contains all basic properties of all items, which all items should inherit from"""

    def __init__(self, name, weight=0, value=0, size="small", ai_description="No description yet"):

        self.name = name
        self.weight = weight
        self.value = value
        self.size = size
        self.ai_description = ai_description  # Placeholder for future idea:
        # pass item properties to llm to generate unique description for each item
        self.condition = 100  # as a percentage, where 100 is mint condition

    def __str__(self) -> str:
        item_description = f"It is a {self.name}, it looks {self.size} and {self.weight}, "
        f"and has a value of {self.value}"
        return item_description


class Potion(Item):
    def __init__(self, name, weight, value, size, description):
        super().__init__(name, weight, value, size, description)

    def inspect(self):
        print(f"It looks like you can drink this {self.size} bottle of {self.name}")

    def drink_potion(self):
        print("You drink the potion, and wonder what effect it will have on you")


class HealingPotion(Potion):
    def __init__(self, name, weight, value, size, description, hitpoints):
        super().__init__(name, weight, value, size, description)
        self.hitpoints = hitpoints

    # def __init__(self, name, value, size, hitpoints):
    #     super().__init__(name, value, size)
    #     self.hitpoints = hitpoints

    def drink_potion(self):
        print(f"You drink the {self.size} healing potion, and feel better immmediately")
        return self.hitpoints


class Poison(Potion):
    def __init__(self, name, weight, value, size, description, damage):
        super().__init__(name, weight, value, size, description)
        self.damage = damage

    def drink_potion(self):
        print(f"You drink the {self.size} bottle of poison, and don't feel so good anymore")
        return self.damage


if __name__ == "__main__":
    red_potion = HealingPotion("health potion", 1, 12, "small", "", 7)

    red_potion.inspect()
    red_potion.drink_potion()

    green_potion = Poison("Cyanide", 1, 8, "medium", "", 9)
    green_potion.inspect()
    green_potion.drink_potion()
