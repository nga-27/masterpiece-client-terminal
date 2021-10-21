import time

from libs.read_fixture import read_fixture
from libs.api import ping_server, get_item
from libs.start_game import (
    start_game, list_characters, add_user_character, starting_positions
)
from libs.take_turn import (
    take_turn
)

GAME_CONTENT = read_fixture()

IS_AUTO_GAME = False
if len(GAME_CONTENT) > 0:
    IS_AUTO_GAME = True
    print("\r\n")

ping_server()
start_game()

players = []

if not IS_AUTO_GAME:
    for i in range(3):
        user_name = input("Add user's name: ")

        print("\r\nHere are the characters...\r\n")
        list_characters()
        character_id = input("Pick a character based on id: ")

        user_name = add_user_character(user_name, character_id)
        players.append({'name': user_name, 'computer': True})
        if i==0:
            players[0]['computer'] = False

else:
    for player in GAME_CONTENT['players']:
        user_name = GAME_CONTENT['players'][player]['name']
        character_id = GAME_CONTENT['players'][player]['character_id']
        user_name = add_user_character(user_name, character_id)
        players.append({'name': user_name, 'computer': True})
        time.sleep(2)

print("\r\n*******************\r\n")

starting_positions()

for round_num in range(GAME_CONTENT['rounds']):
    print(f"\r\n***** ROUND {round_num+1} *****\r\n")
    for player in players:
        take_turn(player['name'], computer=player['computer'])
        time.sleep(2)


print("\r\n*******************\r\n")
print("Final scores!")
scores = []
users, _ = get_item('user/')
for player in players:
    amount = users[player['name']]['current_cash']
    for painting in users[player['name']]['paintings']:
        amount += painting['actual_value']
    scores.append(amount)
    print(f"{player['name'].upper()} == ${amount} :: cash = {users[player['name']]['current_cash']}")
