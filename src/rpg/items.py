# Definiert Items.

#     Heiltrank
#     Waffe
#     ggf. Basisklasse Item

# Verantwortung:

#     Effekt definieren
#     Anwendung auf Spieler, Gegner oder Welt

from rpg.llm_integration import generate_description


class Item:
    """This class contains all basic properties of all items, which all items should inherit from"""

    def __init__(
        self,
        name,
        weight=0,
        value=0,
        size="small",
        condition=85,
    ):

        self.name = name
        self.weight = weight
        self.value = value
        self.size = size
        self.condition = condition
        self.ai_description = None

    def __str__(self) -> str:
        item_description = f"It is a {self.name}, it looks {self.size} and {self.weight}, "
        f"and has a value of {self.value}"
        return item_description

    def create_prompt_dict(self):
        return {
            "item": self.name,
            "weight": self.weight,
            "value": self.value,
            "size": self.size,
            "condition": self.condition,
        }

    def get_ai_description(self):
        if self.ai_description is None:
            self.ai_description = generate_description(self.create_prompt_dict())
        return self.ai_description


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


class Sword(Item):
    def __init__(
        self,
        name,
        weight=0,
        value=0,
        size="medium",
        condition=85,
    ):

        super().__init__(name, weight, value, size, condition)
        self.base_damage = 12
        self.damage = int(self.base_damage * self.condition / 100)

    def create_prompt_dict(self):
        prompt_dict = super().create_prompt_dict()
        prompt_dict["damage"] = self.damage
        return prompt_dict


if __name__ == "__main__":
    # red_potion = HealingPotion("health potion", 1, 12, "small", "", 7)

    # red_potion.inspect()
    # red_potion.drink_potion()

    # green_potion = Poison("Cyanide", 1, 8, "medium", "", 9)
    # green_potion.inspect()
    # green_potion.drink_potion()

    # print(red_potion.ai_description)
    # print(green_potion.ai_description)

    guard_sword = Sword("guard sword", 1, 10, "medium", 60)

    print(guard_sword.get_ai_description())

    golden_sword = Sword("sword with inticate gold patterning", 1, 500, "large", 98)

    print(golden_sword.get_ai_description())
