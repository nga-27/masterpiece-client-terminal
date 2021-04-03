import uuid

from .api import start_new_game, fetch_characters, post_item

def start_game():
    print("Starting game...")
    start_new_game()

def list_characters():
    characters = fetch_characters()
    for member in characters:
        print(f"id = {characters[member]['id']} :: {member}")
    print("")

def add_user_character(name: str, character_id):
    data = {
        "uuid": str(uuid.uuid4()),
        "name": name,
        "character": "string",
        "character_id": character_id,
        "current_position": 0,
        "current_roll": 0,
        "paintings": [],
        "current_cash": 1500000
    }
    req, code = post_item("user/", data)
    if code == 201:
        print(f"\r\ncharacter '{req['value']['character']}' added to player '{name}'")
        return name
    return None