"""
Game Board

Changelog:
12/11/2016 - Created by Justin
"""

# Import Modules
from python_classes.class_city import *


# Class Definition
class Board:
    def __init__(self, regions, map='USA'):
        # Create city list
        city_definitions = '../python_resources/vanilla_cities.csv'
        self.city_list = []
        with open(city_definitions, 'r') as csvfile:
            for row in csvfile:
                row_data = row.replace('\n', '').split(',')
                if row_data[2] in regions:
                    self.city_list.append(City(row_data[0]))


if __name__ == '__main__':
    reg = ['brown']
    myBoard = Board(reg)
