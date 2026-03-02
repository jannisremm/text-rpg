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

from rpg.llm_integration import generate_description


class Room:
    def __init__(self, size, room_type=None):
        self.size = size
        self.description = generate_contents(size)
        self.ai_description = None

    def get_ai_description(self):
        if self.ai_description is None:
            self.ai_description = generate_description(
                {
                    "size": self.size,
                    "lighting": "torches on the wall",
                    "temperature": "low",
                    "humidity": "high",
                    "contents": [
                        "cracked bed",
                        "bundle of blankets",
                        "torn pillow",
                        "small bedside table",
                        "sack of old clothes",
                        "candles arranged in a circle",
                        "pile of bones",
                        "group of strange runes carved into the floor",
                        "shattered mirror",
                    ],
                }
            )
        return self.ai_description


def generate_contents(room_size):
    room_type = random.randrange(len(thematic_rooms))
        self.room_type = room_type
        self.description = generate_description2(size, room_type)


def generate_description(room_size, room_type=None):
    if room_type is None:
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


def generate_description2(room_size=None, room_type=None):
    if room_type is None:
        room_type = random.randrange(len(thematic_items))

    if room_size is None:
        room_size = random.choice(["small", "medium", "large"])

    room_ambience = random.choice(ambiences)
    room_structural_features = []
    room_themematic_items = []
    room_items = []

    match room_size:
        case "small":
            room_structural_features = random.sample(structural_features, k=2)
            room_themematic_items = random.sample(thematic_items[room_type], k=2)
            room_items = random.sample(general_items_2, k=2)

        case "medium":
            room_structural_features = random.sample(structural_features, k=4)
            room_themematic_items = random.sample(thematic_items[room_type], k=4)
            room_items = random.sample(general_items_2, k=4)

        case "large":
            room_structural_features = random.sample(structural_features, k=6)
            room_themematic_items = random.sample(thematic_items[room_type], k=6)
            room_items = random.sample(general_items_2, k=6)

    print(
        f"Room abience: {room_ambience}, room features: {room_structural_features},"
        f"items: {room_themematic_items}, {room_items}"
    )


def generate_level(number_of_roooms):
    room_list = []
    starting_room = Room("medium", 0)
    room_list.append(starting_room)
    for room in range(number_of_roooms):
        size = random.choice(["small", "medium", "large"])
        room = Room(size)
        room_list.append(room)

    return room_list


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
        "pouch of dried herb bundles",
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

ambiences = [
    "cold and slimy",
    "bright and airy",
    "thick with damp mist",
    "heavy with the smell of mildew",
    "eerily silent",
    "echoing with distant dripping water",
    "oppressively hot",
    "filled with drifting dust motes",
    "charged with static electricity",
    "suffocatingly stale",
    "strangely tranquil",
    "buzzing faintly with unseen insects",
    "permeated by the scent of burnt herbs",
    "claustrophobic and tight",
    "wide and hollow-sounding",
    "bathed in flickering shadows",
    "tinged with metallic air",
    "unsettlingly still",
    "haunted by faint whispers",
    "vibrating softly beneath your feet",
    "carrying a low mechanical hum",
    "humid and suffocating",
    "dry as old parchment",
    "tainted with the odor of rot",
    "permeated by incense smoke",
    "unnaturally cold",
    "warped by strange acoustics",
    "filled with faint blue luminescence",
    "smelling faintly of sulfur",
    "tinged with ozone",
    "shrouded in unnatural gloom",
    "lit by a soft golden glow",
    "restless, as if watched",
]

structural_features = [
    "arched stone ceiling",
    "cracked marble pillars",
    "narrow arrow slits in the walls",
    "spiral staircase descending into darkness",
    "raised stone dais",
    "sunken central pit",
    "iron-barred gate",
    "collapsed section of wall",
    "ornate carved doorway",
    "heavy oak door reinforced with iron",
    "stone support columns",
    "vaulted ceiling",
    "wooden rafters",
    "crumbling brickwork",
    "intricately tiled floor",
    "mosaic depicting a forgotten battle",
    "faded frescoes",
    "deep drainage trench",
    "built-in stone shelves",
    "alcove carved into the wall",
    "recessed torch holders",
    "grated floor section",
    "large circular skylight",
    "chained iron chandelier",
    "trapdoor set into the floor",
    "stone archway",
    "reinforced iron beams",
    "curved corridor branching outward",
    "carved gargoyle supports",
    "slanted stone floor",
    "wood-paneled walls",
    "low hanging ceiling beams",
    "narrow observation balcony",
    "iron spiral ladder",
]
thematic_items = [
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
    # Sleeping Quarters
    [
        "bunk bed",
        "straw mattress",
        "wooden wardrobe",
        "small bedside table",
        "wash basin on a stand",
        "writing desk covered in dust",
        "folding privacy screen",
    ],
    # Workshop / Smithy
    [
        "anvil",
        "large forge",
        "blackened workbench",
        "tool rack fixed to the wall",
        "bellows beside the furnace",
        "grindstone mounted on a frame",
        "metalworking table",
        "broken wheel",
    ],
    # Storage
    [
        "barrel",
        "wooden crate",
        "chest of drawers",
        "stacked wooden crates",
        "row of sealed barrels",
        "tall shelving unit",
        "large storage chest bolted to the floor",
        "hanging rack of canvas sacks",
        "supply ledger nailed to a beam",
    ],
    # Ritual Chamber
    [
        "stone altar",
        "circle of candles",
        "chalk-drawn summoning circle",
        "obsidian pedestal",
        "faded tapestry",
        "group of strange runes carved into the floor",
        "tapestry depicting occult symbols",
        "bone arrangement in ritual pattern",
        "incense brazier",
    ],
    # Alchemy Study
    [
        "alchemy workstation",
        "rack of bubbling flasks",
        "herb drying rack",
        "cracked mirror",
        "large distillation apparatus",
        "glass retort stand",
        "chalkboard covered in formulas",
    ],
    # Guard Post
    [
        "weapon rack",
        "faded banner",
        "armor stand",
        "map table",
        "wooden chair",
        "small table",
        "wooden barricade",
        "signal gong mounted on frame",
        "training dummy stuffed with straw",
    ],
    # Noble Chamber
    [
        "canopied bed",
        "ornate vanity mirror",
        "velvet chaise lounge",
        "long dining table",
        "grand bookshelf",
        "embroidered wall tapestry",
    ],
]

general_items_2 = [
    "rusted dagger",
    "well-balanced short sword",
    "iron helmet",
    "leather gloves",
    "pair of sturdy boots",
    "silver ring",
    "gold signet ring",
    "small polished gem",
    "jeweled brooch",
    "pouch of copper coins",
    "pouch of silver coins",
    "small vial of red liquid",
    "rolled parchment scroll",
    "iron key",
    "ornate brass key",
    "bone-handled knife",
    "set of lockpicks",
    "folded cloak",
    "embroidered sash",
    "brass compass",
    "small hand mirror",
    "bundle of dried herbs",
    "sealed wax letter",
    "ivory dice set",
    "bronze medallion",
    "engraved locket",
    "cracked monocle",
    "silver chain necklace",
    "coin purse with hidden compartment",
    "small wooden idol",
    "metal flask",
    "pair of iron bracers",
    "worn leather satchel",
    "sturdy rope coil",
    "flint and steel kit",
]

if __name__ == "__main__":
    print("Sample room descriptions:")
    small_room = Room("small")
    print(small_room.description)
    print("")
    print(small_room.get_ai_description())
    print("")
    print(small_room.get_ai_description())
    print("")
    # medium_room = Room("medium")
    # print(medium_room.description)
    # print("")
    # print(medium_room.ai_description)
    # print("")
    # large_room = Room("large")
    # print(large_room.description)
