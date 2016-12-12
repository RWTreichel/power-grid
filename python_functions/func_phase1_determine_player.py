"""
Phase 1 - Determine Player Order

During this phase, the new player order is determined.   The first player is the player with the most cities in his
network (first house on the scoring track). If two or more players are tied for the most cities, the first player is
the player among them with the largest-numbered power plant. Place this player‘s house in the first position in the
player order area. Determine the remaining player positions using the same rules.

Changelog:
12/11/2016 - Created by Justin
"""

# Import Modules
import operator
from python_classes.class_game import *


def phase_1(board_obj):
    # Count up cities owned by each player
    player_city_count = {}
    for city in board_obj.city_list:
        if city.owner in player_city_count:
            player_city_count[city.owner] += 1
        else:
            player_city_count[city.owner] = 1

    # Determine order
    sorted_city_count = sorted(player_city_count.items(), key=operator.itemgetter(1))
    sorted_city_count = [x for x in sorted_city_count if x[0]]
    sorted_city_count.reverse()

    # NEED to add in tie breaker rule
    return sorted_city_count


# FOR TESTING
if __name__ == '__main__':
    from python_classes.class_board import *
    myBoard = Board(regions=['brown'])
    # Make up fake city owners
    myBoard.city_list[0].owner = 2
    myBoard.city_list[1].owner = 1
    myBoard.city_list[2].owner = 2
    myBoard.city_list[3].owner = None
    myBoard.city_list[4].owner = 1
    myBoard.city_list[5].owner = 2
    myBoard.city_list[6].owner = None

    new_order = phase_1(myBoard)
    print(new_order)
