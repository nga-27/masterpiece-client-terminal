import uuid
import random

from .api import (
    start_new_game, fetch_characters, post_item, get_item, patch_item
)

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

def starting_positions():
    req, _ = get_item("user/")
    for player in req:
        # print(f"player: {player}")
        # print(f"keys: {req[player].keys()}")
        position = random.randint(0, 29)
        data = {
            "name": player,
            "roll_value": req[player]['current_roll'],
            "move_direction": "cw",
            "position": position
        }
        p_req, code = patch_item("user/start_position", data)
        if code != 201:
            print(f"{p_req}")
    print(f"\r\nPlayer positions loaded.\r\n")
    req, _ = get_item("user/")
    for player in req:
        print(f"{req[player]['name']} --> start on position: {req[player]['current_position']} ")
    print("\r\n")