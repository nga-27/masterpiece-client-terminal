# Roll dice
# Move left or right
# Fetch space information
import random

from .api import ( get_item, patch_item )

def take_turn(player: str, computer=False):
    dice_roll, _ = get_item("dice/roll/1")
    direction = 'cw'
    if computer:
        binary = random.randint(0, 1)
        if binary:
            direction = 'ccw'
    else:
        direction = input('direction? (cw, ccw)')
    data = {
        "name": player,
        "move_direction": direction,
        "roll_value": dice_roll,
        "position": 0
    }
    new_position, _ = patch_item("user/update_position", data)
    print(f"{new_position['value']['name']} rolls a {dice_roll}")
    board, _ = get_item("board/positions")
    print(f"Board :: {board[0]['value'][player]['position_name']}")
    process_position(board[0]['value'][player], player)


def process_position(position, player):
    print(position)
    types, code = get_item("board/types")
    board_types = types[0]['value']
    print(f"{board_types}\r\n")

    if position['type'] == 'buy_from_bank':
        res, code = get_item('paintings/next')
        print(res)
        buy_from_bank(player, "painting", position['value'])


def buy_from_bank(player, painting_obj, amount):
    print("BUY FROM BANK")
    data = {
        "name": player,
        "painting": painting_obj,
        "character": "",
        "character_id": "",
        "current_position": 0,
        "current_roll": 0,
        "paintings": painting_obj,
        "current_cash": -1*amount
    }


