"""
Player

Changelog:
12/11/2016 - Created by Justin
"""

# Import Modules


# Class Definition
class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.score = 0
        self.resources = {'coal': 0,
                          'oil': 0,
                          'garbage': 0,
                          'uranium': 0}

    def update_score(self, value):
        self.score += value
        return self.score

    def update_resources(self, delta_resources):
        for res in delta_resources:
            self.resources[res] += delta_resources[res]
        return self.resources


# FOR TESTING
if __name__ == '__main__':
    player_1 = Player('Justin', 'Green')
    print('NAME: {0}, COLOR: {1}, SCORE: {2}, RESOURCES: {3}'.format(player_1.name, player_1.color, player_1.score, player_1.resources))
