# Mit dieser Datei soll eine Schnittstelle zu der OpenAI API erstellt werden,
# mit der Beschreibungen für Objekte, Räume, Gegner etc. generiert werden


import random

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
You are writing flavour text for a low-fantasy, gothic-horror text RPG.
Your output must feel handcrafted, grounded, and varied.

Hard constraints:
- Return prose only. No lists, labels, headings, quotation marks, or meta commentary.
- Never mention exact numeric values, percentages, currency symbols, equations, or stat names.
- Do not mention game terms like "player", "inventory", "rarity tier", "interest score",
  or "deviation label".
- Do not contradict provided item properties.
- If a property is about average, keep it subtle.
- If a property is unusual, imply it through material, wear, balance, craftsmanship, provenance,
  or aura.

Variety rules:
- Avoid repetitive openings ("This item...", "You see...", "It appears...").
- Vary sentence rhythm and structure across generations.
- Change descriptive angle each time (craftsmanship, prior owner traces, practical use,
  hidden history, quiet menace).
- Prefer concrete nouns and verbs over stacked adjectives.
- Keep tone restrained: eerie and evocative, never melodramatic.

Style target:
- Gothic horror atmosphere inspired by Lovecraft/Poe, but concise and readable.
"""
ROOM_INSTRUCTIONS = """
You are writing room flavour text for a low-fantasy, gothic-horror text RPG.
Describe the first moments after entering a room.

Hard constraints:
- Write in second person ("you").
- Return prose only. No lists, headings, labels, or meta text.
- Mention only the provided ambience, structural features, thematic items, and general items.
- You may infer plausible placement/history,
  but do not invent additional named objects or architecture.
- Keep the room believable as recently abandoned (days, not long-decayed ages),
  unless input strongly implies otherwise.

Composition rules:
- Blend ambience, structure, and items naturally; do not list categories.
- Place items in sensible positions (shelved, hung, stacked, wedged, laid out, half-hidden).
- Highlight a few striking details and let the rest support atmosphere.
- Vary openings and cadence: sometimes start with sound/smell/light/temperature,
  other times with spatial layout.
- Avoid repeated templates and mirrored sentence patterns between generations.
- End with a subtle hook that invites curiosity without adding new concrete objects.

Style target:
- Gothic horror atmosphere inspired by Lovecraft/Poe, grounded and immersive.
"""

ITEM_VARIATION_STEERS = [
    "This description should focus on tactile detail and craftsmanship first, then implication.",
    "This description should hint at a prior owner through traces of use or neglect.",
    "This description should foreground practical function before mood.",
    "This description should center on one uncanny detail while remaining grounded.",
    "This description should imply history through subtle cause-and-effect clues.",
]

ROOM_VARIATION_STEERS = [
    "Open with sensory detail (sound, smell, light, or temperature), then widen to layout.",
    "Open with room layout and movement path, then reveal notable objects.",
    "Move from structural features to thematic items, then to general items.",
    "Start with a quiet unsettling detail, then anchor it with practical room logic.",
    "Describe details as if your gaze is scanning left to right across the room.",
]


def generate_description(properties: dict, interest_score=0, gptmodel="gpt-5.2"):

    if interest_score <= 2:
        length_instruction = "Length: exactly 1 sentence, compact and concrete."

    elif interest_score <= 4:
        length_instruction = "Length: exactly 2 sentences with distinct rhythm."
    elif interest_score <= 6:
        length_instruction = "Length: exactly 3 sentences; vary sentence length."
    else:
        length_instruction = "Length: 4 to 5 sentences; rich but controlled."

    variation_steer = random.choice(ITEM_VARIATION_STEERS)
    llm_instructions = f"{ITEM_INSTRUCTIONS}\n{length_instruction}\n{variation_steer}"

    item_block = "\n".join(f"{key}:{value}" for key, value in properties.items())

    prompt = f"""Item properties:
{item_block}

Write only the final description text."""

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
        room_size_modifier = "Length: exactly 2 sentences."
    elif room_size == "medium":
        room_size_modifier = "Length: exactly 4 sentences."
    else:
        room_size_modifier = "Length: exactly 6 sentences."
    variation_steer = random.choice(ROOM_VARIATION_STEERS)
    llm_instructions = f"{ROOM_INSTRUCTIONS}\n{room_size_modifier}\n{variation_steer}"
    prompt = f"""Room properties:
room size: {room_size}
room ambience: {room_ambience}
structural features: {room_structural_features}
thematic items: {room_thematic_items}
general items: {room_items}

Write only the final description text."""
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
