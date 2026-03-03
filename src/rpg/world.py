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

from rpg.llm_integration import generate_room_description
from rpg.world_content import AMBIENCES, GENERAL_ITEMS, STRUCTURAL_FEATURES, THEMATIC_ITEMS


class Room:
    def __init__(self, size, room_type=None):
        self.size = size
        self.room_type = room_type
        (
            self.room_ambience,
            self.room_structural_features,
            self.room_thematic_items,
            self.room_items,
        ) = generate_description2(self.size, self.room_type)
        self.ai_description = None

    def get_ai_description(self):
        if self.ai_description is None:
            self.ai_description = generate_room_description(
                self.size,
                self.room_ambience,
                self.room_structural_features,
                self.room_thematic_items,
                self.room_items,
            )
        return self.ai_description


# def generate_description(room_size, room_type=None):
#     if room_type is None:
#         room_type = random.randrange(len(thematic_rooms))
#     match room_size:
#         case "small":
#             room_description = (
#                 f"The small room contains a {random.choice(thematic_rooms[room_type])}"
#                 f" and a {random.choice(general_items[random.randint(0, len(general_items) - 1)])}"
#             )
#             return room_description
#         case "medium":
#             room_description = (
#                 f"The medium sized room contains a {random.choice(thematic_rooms[room_type])},"
#                 f" a {random.choice(thematic_rooms[room_type])},"
#                 f" a {random.choice(general_items[random.randint(0, 4)])},"
#                 f" and a {random.choice(general_items[random.randint(0, 4)])}"
#             )
#             return room_description
#         case "large":
#             room_type = random.randint(0, 5)
#             room_description = (
#                 f"The large room contains a {random.choice(thematic_rooms[room_type])},"
#                 f" a {random.choice(thematic_rooms[room_type])},"
#                 f" a {random.choice(thematic_rooms[room_type])},"
#                 f" a {random.choice(general_items[random.randint(0, 4)])},"
#                 f" a {random.choice(general_items[random.randint(0, 4)])},"
#                 f" and a {random.choice(general_items[random.randint(0, 4)])}"
#             )
#             return room_description


def generate_description2(room_size=None, room_type=None):
    if room_type is None:
        room_type = random.randrange(len(THEMATIC_ITEMS))

    if room_size is None:
        room_size = random.choice(["small", "medium", "large"])

    room_ambience = random.choice(AMBIENCES)
    room_structural_features = []
    room_thematic_items = []
    room_items = []

    match room_size:
        case "small":
            room_structural_features = random.sample(STRUCTURAL_FEATURES, k=2)
            room_thematic_items = random.sample(THEMATIC_ITEMS[room_type], k=2)
            room_items = random.sample(GENERAL_ITEMS, k=2)

        case "medium":
            room_structural_features = random.sample(STRUCTURAL_FEATURES, k=4)
            room_thematic_items = random.sample(THEMATIC_ITEMS[room_type], k=4)
            room_items = random.sample(GENERAL_ITEMS, k=4)

        case "large":
            room_structural_features = random.sample(STRUCTURAL_FEATURES, k=6)
            room_thematic_items = random.sample(THEMATIC_ITEMS[room_type], k=6)
            room_items = random.sample(GENERAL_ITEMS, k=6)

        case _:
            room_structural_features = random.sample(STRUCTURAL_FEATURES, k=4)
            room_thematic_items = random.sample(THEMATIC_ITEMS[room_type], k=4)
            room_items = random.sample(GENERAL_ITEMS, k=4)

    # print(
    #     f"Room abience: {room_ambience}, room features: {room_structural_features},"
    #     f"items: {room_thematic_items}, {room_items}"
    # )
    return room_ambience, room_structural_features, room_thematic_items, room_items


def generate_level(number_of_rooms):
    room_list = []
    starting_room = Room("medium", 0)
    room_list.append(starting_room)
    for room in range(number_of_rooms - 1):
        size = random.choice(["small", "medium", "large"])
        room = Room(size)
        room_list.append(room)

    return room_list


if __name__ == "__main__":
    print("Sample room descriptions:")
    print("")
    small_room = Room("small")
    # print(
    #     small_room.room_ambience,
    #     small_room.room_structural_features,
    #     small_room.room_thematic_items,
    #     small_room.room_items,
    # )
    print("")
    print(small_room.get_ai_description())
    print("")
    medium_room = Room("medium")
    # print(
    #     medium_room.room_ambience,
    #     medium_room.room_structural_features,
    #     medium_room.room_thematic_items,
    #     medium_room.room_items,
    # )
    print("")
    print(medium_room.get_ai_description())
    print("")
    large_room = Room("large")
    # print(
    #     large_room.room_ambience,
    #     large_room.room_structural_features,
    #     large_room.room_thematic_items,
    #     large_room.room_items,
    # )
    print("")
    print(large_room.get_ai_description())
