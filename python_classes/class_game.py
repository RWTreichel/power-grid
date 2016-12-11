"""
Game Instance

Changelog:
12/11/2016 - Created by Justin
"""

# Import Modules
from collections import OrderedDict
from python_classes.class_player import *
from python_classes.class_board import *
from python_functions.func_phase1_determine_player import *
from python_functions.func_phase2_auction_plants import *
from python_functions.func_phase3_buy_resources import *
from python_functions.func_phase4_build import *
from python_functions.func_phase5_bureaucracy import *


# Class Definition
class Game:
    def __init__(self, player_list=[], options=None):
        self.player_list = player_list
        self.round = 0
        self.round_phases = []
        if options:
            self.board = Board(options['regions'], map=options['map'])
        else:
            self.board = Board(['brown'])  # Default Region list

    def add_player(self, player_obj):
        self.player_list.append(player_obj)

        return self.player_list

    def play_round(self):
        # Phase 1 - Determine Player Order
        sorted_city_count = phase_1(self.board)

        # Phase 2 - Auction Power Plants

        # Phase 3 - Buying Resources

        # Phase 4 - Building

        # Phase 5 - Bureaucracy


# FOR TESTING
if __name__ == '__main__':
    myGame = Game()
    myGame.options = {'map': 'USA',
                      'regions': ['brown']}
    myGame.add_player(Player('Justin', 'Green'))
    myGame.add_player(Player('Richard', 'Red'))
    print(myGame.player_list)
