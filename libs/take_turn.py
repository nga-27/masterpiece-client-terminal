# Roll dice
# Move left or right
# Fetch space information
import random

from .api import ( get_item, patch_item, post_item )

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
    print(f"{board_types}")

    if position['type'] == 'buy_from_bank':
        res, code = get_item('actions/next_painting')
        painting = res[0]['value']
        buy_from_bank(player, painting, position['value'])

    elif position['type'] == 'collect':
        collect_money(player, position['value'])

    elif position['type'] == 'must_sell_to_bank':
        must_sell_to_bank(player)

    print("")


def buy_from_bank(player, painting_obj, amount):
    print(f"BUY FROM BANK for ${amount*1000}\r\n")
    res, _ = get_item(f"user/{player}")
    if res[0]['value']['current_cash'] >= amount * 1000:
        data = {
            "name": player,
            "character": "",
            "character_id": "",
            "current_position": 0,
            "current_roll": 0,
            "paintings": [painting_obj],
            "current_cash": -1 * amount * 1000
        }
        res, code = patch_item("user/update_holdings", data)



def collect_money(player, amount):
    print(f"COLLECT ${amount*1000}\r\n")
    data = {
        "name": player,
        "character": "",
        "character_id": "",
        "current_position": 0,
        "current_roll": 0,
        "paintings": [],
        "current_cash": amount * 1000
    }
    res, code = patch_item("user/update_holdings", data)


def must_sell_to_bank(player):
    print("MUST SELL TO BANK\r\n")
    res, _ = get_item(f"user/{player}")
    data = res[0]['value']
    if len(data['paintings']) == 0:
        print("There are no paintings to sell :(")
        return
    amounts = []
    for painting in data['paintings']:
        amounts.append(painting['actual_value'])
    max_item = max(amounts)
    max_index = amounts.index(max_item)
    res, code = post_item(f'actions/sell/{player}', data['paintings'][max_index])
    new_amount = res[0]['value'] + data['current_cash']
    new_data = {
        "name": player,
        "character": "",
        "character_id": "",
        "current_position": 0,
        "current_roll": 0,
        "paintings": [],
        "current_cash": new_amount
    }
    res, code = patch_item("user/update_holdings", data)
    