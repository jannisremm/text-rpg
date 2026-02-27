# Definiert Items.

#     Heiltrank
#     Waffe
#     ggf. Basisklasse Item

# Verantwortung:

#     Effekt definieren
#     Anwendung auf Spieler, Gegner oder Welt
import random

from rpg.llm_integration import generate_description


class ItemProfile:
    """Creates a baseline for a type of item, with which other items of that type can be compared"""

    def __init__(
        self, mean_weight, std_weight, mean_value, std_value, mean_condition, std_condition
    ):
        self.mean_weight = mean_weight
        self.std_weight = std_weight
        self.mean_value = mean_value
        self.std_value = std_value
        self.mean_condition = mean_condition
        self.std_condition = std_condition

    def random_weight(self):
        return random.gauss(self.mean_weight, self.std_weight)

    def random_value(self):
        return random.gauss(self.mean_value, self.std_value)

    def random_condition(self):
        return random.gauss(self.mean_condition, self.std_condition)


class SwordProfile(ItemProfile):
    def __init__(
        self,
        mean_weight,
        std_weight,
        mean_value,
        std_value,
        mean_condition,
        std_condition,
        mean_base_damage,
        std_base_damage,
    ):
        super().__init__(
            mean_weight, std_weight, mean_value, std_value, mean_condition, std_condition
        )
        self.mean_base_damage = mean_base_damage
        self.std_base_damage = std_base_damage

    def random_base_damage(self):
        return random.gauss(self.mean_base_damage, self.std_base_damage)


def compute_deviation_label(value, mean, std):
    z = (value - mean) / std

    if abs(z) < 0.5:
        return "about average"
    elif abs(z) < 1.5:
        return "somewhat unusual"
    elif z > 0:
        return "far above average"
    else:
        return "far below average"


class Item:
    """This class contains all basic properties of all items, which all items should inherit from"""

    def __init__(
        self,
        name,
        item_profile=None,
        weight=None,
        value=None,
        size="small",
        condition=None,
        rarity="common",
        flavourtext=None,
        prompt_dict={},
        interest_score=0,
    ):

        self.name = name
        self.item_profile = item_profile
        self.weight = (
            weight if weight is not None else (item_profile.random_weight() if item_profile else 0)
        )
        self.value = (
            value if value is not None else (item_profile.random_value() if item_profile else 0)
        )
        self.size = size
        self.condition = (
            condition
            if condition is not None
            else (item_profile.random_condition() if item_profile else 0)
        )
        self.rarity = rarity
        self.flavourtext = flavourtext
        self.ai_description = None
        self.prompt_dict = prompt_dict
        self.interest_score = interest_score

    def __str__(self) -> str:
        item_description = f"It is a {self.name}, it looks {self.size} and {self.weight}, "
        f"and has a value of {self.value}"
        return item_description

    def create_prompt_dict(self):
        if len(self.prompt_dict) > 0:
            return self.prompt_dict
        else:
            data = {
                "item": self.name,
                "weight": self.weight,
                "value": self.value,
                "size": self.size,
                "condition": self.condition,
                "rarity": self.rarity,
                "flavourtext": self.flavourtext,
            }
            if self.item_profile:
                data["weight_deviation"] = compute_deviation_label(
                    self.weight,
                    self.item_profile.mean_weight,
                    self.item_profile.std_weight,
                )
                data["value_deviation"] = compute_deviation_label(
                    self.value,
                    self.item_profile.mean_value,
                    self.item_profile.std_value,
                )
                data["condition_deviation"] = compute_deviation_label(
                    self.condition,
                    self.item_profile.mean_condition,
                    self.item_profile.std_condition,
                )
            print(data)
            return data

    def create_interest_score(self):
        self.interest_score = 0
        for key, value in self.prompt_dict.items():
            if value == "legendary":
                self.interest_score += 4
            elif value == "rare":
                self.interest_score += 2
            elif value in ("far above average", "far below average"):
                self.interest_score += 2
            elif value == "somewhat unusual":
                self.interest_score += 1
        return self.interest_score

    def get_ai_description(self):
        if self.ai_description is None:
            self.prompt_dict = self.create_prompt_dict()
            self.interest_score = self.create_interest_score()
            self.ai_description = generate_description(self.prompt_dict, self.interest_score)
        return self.ai_description


class Potion(Item):
    def __init__(self, name, item_profile=None, weight=0, value=0, size="small", condition=85):
        super().__init__(name, item_profile, weight, value, size, condition)

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
        item_profile=None,
        weight=None,
        value=None,
        size="medium",
        condition=None,
        base_damage=None,
        rarity="common",
        flavourtext="standard issue guard sword",
    ):
        super().__init__(name, item_profile, weight, value, size, condition, rarity, flavourtext)
        if base_damage is not None:
            self.base_damage = base_damage
        elif isinstance(item_profile, SwordProfile):
            self.base_damage = item_profile.random_base_damage
        else:
            self.base_damage = 10

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

    # guard_sword = Sword("guard sword", 1, 10, "medium", 60)

    # print(guard_sword.get_ai_description())

    # golden_sword = Sword("sword with inticate gold patterning", 1, 500, "large", 98)

    # print(golden_sword.get_ai_description())

    GUARD_SWORD_PROFILE = ItemProfile(1.3, 0.05, 500, 100, 75, 10)

    g1 = Sword("guard sword", item_profile=GUARD_SWORD_PROFILE)
    print(g1.create_prompt_dict())
    print(g1.get_ai_description())
    g5 = Sword("guard sword", item_profile=GUARD_SWORD_PROFILE)
    print(g5.create_prompt_dict())
    print(g5.get_ai_description())
    g2 = Sword("guard sword", item_profile=GUARD_SWORD_PROFILE, weight=0.5, rarity="rare")
    print(g2.create_prompt_dict())
    print(g2.get_ai_description())
    g3 = Sword("guard sword", item_profile=GUARD_SWORD_PROFILE, condition=99, rarity="legendary")
    print(g3.create_prompt_dict())
    print(g3.get_ai_description())
    g4 = Sword("guard sword", item_profile=GUARD_SWORD_PROFILE, condition=0, value=10)
    print(g4.create_prompt_dict())
    print(g4.get_ai_description())
