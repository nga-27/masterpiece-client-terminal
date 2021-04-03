from libs.api import ping_server
from libs.start_game import (
    start_game, list_characters, add_user_character
)

ping_server()
start_game()

players = []

for _ in range(3):
    user_name = input("Add user's name: ")

    print("\r\nHere are the characters...\r\n")
    list_characters()
    character_id = input("Pick a character based on id: ")

    user_name = add_user_character(user_name, character_id)
    players.append(user_name)

