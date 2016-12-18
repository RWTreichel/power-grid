"""
Main Executing Python Script
Power Grid Game
"""
"""
Import Modules
"""
from python_classes.class_game import *
from python_functions.func_phase1_determine_player import *
from python_functions.func_phase2_auction_plants import *
from python_functions.func_phase3_buy_resources import *
from python_functions.func_phase4_build import *
from python_functions.func_phase5_bureaucracy import *

"""
Set up Game
"""
# Choose Options
myOptions = {'map': 'USA', 'regions': ['brown']}  # From front end

# Choose Players
myPlayer_List = [Player(1, 'Justin', 'Green'), Player(2, 'Richard', 'Red')]  # From front end

# Start New Game
myGame = Game(player_list=myPlayer_List, options=myOptions)
myGame.start_new_game()

"""
Round
"""
# Phase 1 - Determine Player Order
sorted_city_count = phase_1(myGame.board)

# Phase 2 - Auction Power Plants

# Phase 3 - Buy Resources

# Phase 4 - Build

# Phase 5 - Bureaucracy

"""
Finish Game
"""
# Determine Winner