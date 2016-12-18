"""
Resources

Changelog:
12/11/2016 - Created by Justin
"""

# Import Modules
import math


# Class Definition
class Resource:
    def __init__(self, type):
        # type can be: coal, oil, garbage, uranium
        self.type = type


class ResourceMarket:
    def __init__(self):
        self.market = {'coal': [24, 1],
                       'oil': [18, 3],
                       'garbage': [6, 7],
                       'uranium': [2, 14]}

    def update_market(self, resource_delta):
        """
        resource_delta =  {'coal': 6,
                           'oil': 4,
                           'garbage': 1,
                           'uranium': 0}
        """
        # Update market quantities
        for resource in resource_delta:
            self.market[resource][0] += resource_delta[resource]

        # Update market prices
        # Formulas based off visual inspection of board
        self.market['coal'][1] = math.ceil(8 - ((1 / 3.01) * self.market['coal'][0]))
        self.market['oil'][1] = math.ceil(8 - ((1 / 3.01) * self.market['oil'][0]))
        self.market['garbage'][1] = math.ceil(8 - ((1 / 3.01) * self.market['garbage'][0]))
        self.market['uranium'][1] = 18 - (2 * self.market['uranium'][0]) if self.market['uranium'][0] < 5 else 13 - self.market['uranium'][0]

    def refill_market(self, players, step):
        refill_rates = {2: {1: {'coal': 3, 'oil': 2, 'garbage': 1, 'uranium': 1},
                            2: {'coal': 4, 'oil': 2, 'garbage': 2, 'uranium': 1},
                            3: {'coal': 3, 'oil': 4, 'garbage': 3, 'uranium': 1}},
                        3: {1: {'coal': 4, 'oil': 2, 'garbage': 1, 'uranium': 1},
                            2: {'coal': 5, 'oil': 3, 'garbage': 2, 'uranium': 1},
                            3: {'coal': 3, 'oil': 4, 'garbage': 3, 'uranium': 1}},
                        4: {1: {'coal': 5, 'oil': 3, 'garbage': 2, 'uranium': 1},
                            2: {'coal': 6, 'oil': 4, 'garbage': 3, 'uranium': 2},
                            3: {'coal': 4, 'oil': 5, 'garbage': 4, 'uranium': 2}},
                        5: {1: {'coal': 5, 'oil': 4, 'garbage': 3, 'uranium': 2},
                            2: {'coal': 7, 'oil': 5, 'garbage': 3, 'uranium': 3},
                            3: {'coal': 5, 'oil': 6, 'garbage': 5, 'uranium': 2}},
                        6: {1: {'coal': 7, 'oil': 5, 'garbage': 3, 'uranium': 2},
                            2: {'coal': 9, 'oil': 6, 'garbage': 5, 'uranium': 3},
                            3: {'coal': 6, 'oil': 7, 'garbage': 6, 'uranium': 3}}}
        self.update_market(refill_rates[players][step])
