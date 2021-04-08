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
    print(new_position)