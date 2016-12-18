"""
Player

Changelog:
12/11/2016 - Created by Justin
"""

# Import Modules


# Class Definition
class Player:
    def __init__(self, id, name, color):
        self.id = id
        self.name = name
        self.color = color
        self.score = 0
        self.elektro = 0
        self.resources = {'coal': 0,
                          'oil': 0,
                          'garbage': 0,
                          'uranium': 0}

    def update_score(self, value):
        self.score += value
        return self.score

    def update_elektro(self, value):
        self.elektro += value
        return self.elektro

    def update_resources(self, delta_resources):
        for res in delta_resources:
            self.resources[res] += delta_resources[res]
        return self.resources


# FOR TESTING
if __name__ == '__main__':
    player_1 = Player(1, 'Justin', 'Green')
    player_2 = Player(2, 'Richard', 'Red')
    print('PLAYER 1 - NAME: {0}, COLOR: {1}, SCORE: {2}, RESOURCES: {3}'.format(player_1.name, player_1.color,
                                                                     player_1.score, player_1.resources))
    print('PLAYER 2 - NAME: {0}, COLOR: {1}, SCORE: {2}, RESOURCES: {3}'.format(player_2.name, player_2.color,
                                                                     player_2.score, player_2.resources))
