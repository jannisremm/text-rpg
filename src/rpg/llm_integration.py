# Mit dieser Datei soll eine Schnittstelle zu der OpenAI API erstellt werden,
# mit der Beschreibungen für Objekte, Räume, Gegner etc. generiert werden


from dotenv import load_dotenv
from openai import OpenAI

# load environment variables from .env file
# .env file must be in project root directory (where pyproject.toml and .gitignore are)
# .env contents:
# OPENAI_API_KEY=abcdefg123456
# where abcdefg123456 needs to be replaced with an OpenAI API key

load_dotenv()
client = OpenAI()

ITEM_INSTRUCTIONS = """
Generate a brief description for use is a low fantasy text based roleplaying game.
The description will be used as flavourtext for an item.
Never mention exact numbers from the properties, use the stats only to influence tone and vibe. 
Keep everything immersive and grounded. Deviation labels describe how unusual a property is relative
to the typical item of that type. Emphasize properties that are highly unusual.
Do not dwell on properties marked as "about average". 
If a property is unusually high or low, you may invent a subtle, 
plausible explanation grounded in the setting. Do not contradict the item's stated properties.
The descriptions should be written in a gothic horror style, 
similar to HP Lovecraft or Edgar Allen Poe.
"""
ROOM_INSTRUCTIONS = """
Generate a brief description for use is a low fantasy text based roleplaying game.
The description will be used as flavourtext for a room.
You may invent a subtle, plausible explanaitions grounded in the setting
for why items are in the room,or what might have happened within.
Do not invent new items or features
The descriptions should be written in a gothic horror style, 
similar to HP Lovecraft or Edgar Allen Poe.
"""


def generate_description(properties: dict, interest_score=0, gptmodel="gpt-5.2"):

    if interest_score <= 2:
        length_instruction = "Write a brief, factual and mundane description (1 sentence)."

    elif interest_score <= 4:
        length_instruction = "Write a detailed yet grounded description (2 sentences)"
    elif interest_score <= 6:
        length_instruction = "Write a detialed and interesting description (3 sentences)."
    else:
        length_instruction = (
            "Write a rich, detailed imaginative description with flowery language (5 sentences)."
        )

    llm_instructions = ITEM_INSTRUCTIONS + length_instruction

    item_block = "\n".join(f"{key}:{value}" for key, value in properties.items())

    prompt = f"""{item_block}"""

    reasoning_level = (
        {"effort": "high"}
        if properties["rarity"] == "legendary"
        else {"effort": "medium"}
        if properties["rarity"] == "rare"
        else {"effort": "low"}
    )
    # print("------------------LLM INPUT------------------")
    # print(llm_instructions)
    # print(properties)
    # print(interest_score)
    # print(reasoning_level)
    ai_description = client.responses.create(
        model=gptmodel, instructions=llm_instructions, input=prompt, reasoning=reasoning_level
    )
    return ai_description.output_text


def generate_room_description(
    room_size,
    room_ambience,
    room_structural_features,
    room_thematic_items,
    room_items,
    gptmodel="gpt-5.2",
    reasoning_level={"effort": "high"},
):
    if room_size == "small":
        room_size_modifier = "The description should be two sentences long."
    elif room_size == "medium":
        room_size_modifier = "The description should be four sentences long"
    else:
        room_size_modifier = "The description should be six sentences long"
    llm_instructions = ROOM_INSTRUCTIONS + room_size_modifier
    prompt = f"""room ambience: {room_ambience}
    strucural features: {room_structural_features}
    thematic items: {room_thematic_items}
    general items: {room_items}"""
    ai_description = client.responses.create(
        model=gptmodel, instructions=llm_instructions, input=prompt, reasoning=reasoning_level
    )
    return ai_description.output_text


if __name__ == "__main__":
    response_nano = client.responses.create(
        model="gpt-5-nano",
        input="""Write a brief description of the following item. Your response will be used as 
        flavourtext for a low fantasy text based roleplaying game. 
        The items weight and size will be visible to the player, but beyond that they only have
        the flavourtext to determine whether the item is useful to them or not.
        Never mention the exact stats in the description, just use them as input to come up with
        a vibe.

        item: iron guard sword (standard issue)
        weight: 2kg
        rarity: common
        value: $50
        condition: 87%
        found in: weapons rack in armoury room
        """,
    )
    response_five_point_two = client.responses.create(
        model="gpt-5.2",
        input="""Write a brief description of the following item. Your response will be used as 
        flavourtext for a low fantasy text based roleplaying game. 
        The items weight and size will be visible to the player, but beyond that they only have
        the flavourtext to determine whether the item is useful to them or not.
        Never mention the exact stats in the description, just use them as input to come up with
        a vibe.

        item: iron guard sword (standard issue)
        weight: 2kg
        rarity: common
        value: $50
        condition: 87%
        found in: weapons rack in armoury room
        """,
    )
    response_five_point_two_bad_condition = client.responses.create(
        model="gpt-5.2",
        input="""Write a brief description of the following item. Your response will be used as 
        flavourtext for a low fantasy text based roleplaying game. 
        The items weight and size will be visible to the player, but beyond that they only have
        the flavourtext to determine whether the item is useful to them or not.
        Never mention the exact stats in the description, just use them as input to come up with
        a vibe.
        
        item: iron guard sword (standard issue)
        weight: 2kg
        rarity: common
        value: $50
        condition: 7%
        found in: weapons rack in armoury room
        """,
    )

    response2 = client.responses.create(
        model="gpt-5.2",
        input="""Write a brief description of the following item. Your response will be used as 
        flavourtext for a low fantasy text based roleplaying game. 
        The items weight and size will be visible to the player, but beyond that they only have
        the flavourtext to determine whether the item is useful to them or not.

        item: mithril blade of the undying
        weight: 0.5kg
        rarity: legendary
        value: $50000000
        condition: 97%
        found in: heart of a slain dragon
    """,
    )
    print(response_nano.output_text)
    # print(json.dumps(response_nano.model_dump(), indent=2))
    print("Token usage: ", response_nano.usage)
    print(response_five_point_two.output_text)
    # print(json.dumps(response_five_point_two.model_dump(), indent=2))
    print("Token usage: ", response_five_point_two.usage)
    print(response_five_point_two_bad_condition.output_text)
    # print(json.dumps(response_five_point_two.model_dump(), indent=2))
    print("Token usage: ", response_five_point_two_bad_condition.usage)

    # print(response2.output_text)
    # print(json.dumps(response2.model_dump(), indent=2))
    # print("Token usage: ", response2.usage)
