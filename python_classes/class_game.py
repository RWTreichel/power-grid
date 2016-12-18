"""
Game Instance

Changelog:
12/11/2016 - Created by Justin
"""

# Import Modules
from python_classes.class_player import *
from python_classes.class_board import *
from python_classes.class_card import *
from python_classes.class_resource import *


# Class Definition
class Game:
    def __init__(self, player_list=[], options=None):
        self.player_list = player_list
        self.options = options
        self.step = 1
        self.round = 0
        self.order = []
        self.CardDeck = CardDeck()
        self.resource_market = ResourceMarket()  # Initialize Resource Market
        # Create Board Object
        if self.options:
            self.board = Board(self.options['regions'], map=self.options['map'])
        else:
            self.board = Board(['brown'])  # Default Region list

    def add_player(self, player_obj):
        self.player_list.append(player_obj)

        return self.player_list

    def start_new_game(self):
        for player in self.player_list:
            player.elektro = 50  # Start each player with 50 Elecktro
            player.score = 0  # Start each player with 0 Cities
            self.order.append(player.id)  # Initialize Player Order
        self.CardDeck.new_deck()  # Initialize Power Plant Market
        self.resource_market = ResourceMarket()


# FOR TESTING
if __name__ == '__main__':
    myPlayers = [Player(1, 'Justin', 'Green'),
                 Player(2, 'Richard', 'Red')]
    myoptions = {'map': 'USA',
                 'regions': ['brown']}
    myGame = Game(player_list=myPlayers, options=myoptions)
    myGame.start_new_game()

    print(myGame.player_list)
