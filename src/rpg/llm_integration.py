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

SYSTEM_PROMPT = """
Generate a brief description for use is a low fantasy text based roleplaying game.
The description will be used as flavourtext for items, locations, characters etc.
Never mention exact numbers from the properties, use the stats only to influence tone and vibe. 
Keep everything immersive and grounded."""


def generate_description(properties: dict, gptmodel="gpt-5.2"):
    item_block = "\n".join(f"{key}:{value}" for key, value in properties.items())

    prompt = f"""{SYSTEM_PROMPT} Here are the properties: {item_block}"""
    ai_description = client.responses.create(model=gptmodel, input=prompt)
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
