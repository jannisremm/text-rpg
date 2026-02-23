# Verantwortlich für:
#     Räume
#     Reihenfolge
#     Events
#     Begegnungen

# Im MVP reicht:
#     Liste von Räumen
#     Zufälliges Event beim Betreten

# Später kann hier:
#     Map-Graph
#     Dungeon-Struktur
#     Seed-basierte Generierung
# hineinkommen.

import random


class Room:
    def __init__(self, size):
        self.size = size
        self.description = generate_description(size)


def generate_description(room_size):
    room_type = random.randrange(len(thematic_rooms))
    match room_size:
        case "small":
            room_description = (
                f"The small room contains a {random.choice(thematic_rooms[room_type])}"
                f" and a {random.choice(general_items[random.randint(0, len(general_items) - 1)])}"
            )
            return room_description
        case "medium":
            room_description = (
                f"The medium sized room contains a {random.choice(thematic_rooms[room_type])},"
                f" a {random.choice(thematic_rooms[room_type])},"
                f" a {random.choice(general_items[random.randint(0, 4)])},"
                f" and a {random.choice(general_items[random.randint(0, 4)])}"
            )
            return room_description
        case "large":
            room_type = random.randint(0, 5)
            room_description = (
                f"The large room contains a {random.choice(thematic_rooms[room_type])},"
                f" a {random.choice(thematic_rooms[room_type])},"
                f" a {random.choice(thematic_rooms[room_type])},"
                f" a {random.choice(general_items[random.randint(0, 4)])},"
                f" a {random.choice(general_items[random.randint(0, 4)])},"
                f" and a {random.choice(general_items[random.randint(0, 4)])}"
            )
            return room_description


# Each sublist is a distinct room theme

thematic_rooms = [
    # 0 - Abandoned Sleeping Quarters
    [
        "straw mattress",
        "bunk bed",
        "cracked bed",
        "bundle of blankets",
        "torn pillow",
        "small bedside table",
        "empty wardrobe",
    ],
    # 1 - Workshop / Smithy
    [
        "anvil",
        "workbench",
        "rusty shovel",
        "hammer",
        "crowbar",
        "broken wheel",
        "few nails scattered across the floor",
    ],
    # 2 - Storage Room
    [
        "barrel",
        "wooden crate",
        "locked chest",
        "old trunk",
        "sack of old clothes",
        "small pouch",
        "chest of drawers",
    ],
    # 3 - Ritual Chamber
    [
        "stone altar",
        "candles arranged in a circle",
        "pile of bones",
        "group of strange runes carved into the floor",
        "shattered mirror",
        "faded tapestry",
        "ceremonial dagger",
    ],
    # 4 - Alchemy Study
    [
        "bunch of dusty potion bottles",
        "cracked vial",
        "dirty mortar and pestle",
        "stained tome",
        "parchment scroll",
        "book of formulas",
        "puch of dried herb bundles",
    ],
    # 5 - Guard Post
    [
        "weapon rack",
        "rusted spear",
        "round shield",
        "wooden chair",
        "small table",
        "discarded helmet",
        "small bag of dice carved from bone",
    ],
]

general_items = [
    # 0 - Basic Furniture
    ["wooden chair", "stool", "bench", "small table", "shelf", "dresser", "sofa"],
    # 1 - Debris and Rubble
    [
        "pile of rocks",
        "couple of loose stones",
        "bunch of rubble",
        "load of broken pottery",
        "pile of splintered beams",
        "ash pile",
        "few scattered pebbles",
    ],
    # 2 - Containers
    ["barrel", "crate", "small chest", "locked coffer", "iron-bound trunk", "canvas sack"],
    # 3 - Minor Loot
    [
        "rusted dagger",
        "pouch of coins",
        "silver ring",
        "small gem",
        "jeweled brooch",
        "tarnished copper key",
    ],
    # 4 - Wall and Decor Elements
    [
        "faded banner",
        "torn tapestry",
        "mounted torch bracket",
        "line of iron hooks on the wall",
        "cracked mirror",
        "rotting wooden beam",
    ],
]


if __name__ == "__main__":
    print("Sample room descriptions:")
    small_room = Room("small")
    print(small_room.description)
    medium_room = Room("medium")
    print(medium_room.description)
    large_room = Room("large")
    print(large_room.description)
