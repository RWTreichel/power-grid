"""
Power Plant Cards, and Card Deck

Changelog:
12/11/2016 - Created by Justin
"""

# Import Modules


# Class Definition
class Card:
    def __init__(self, id):
        self.id = id

        # Read in card config file
        card_definitions = '../python_resources/vanilla_cards.csv'
        with open(card_definitions, 'r') as csvfile:
            for row in csvfile:
                row_data = row.split(',')
                if str(id) == row_data[0]:
                    self.number = row_data[1]
                    self.resource_req_type1 = row_data[2]
                    self.resource_req_type2 = row_data[3] if row_data[3] != '' else None
                    self.resource_req_count = row_data[4]
                    self.cities_powered = row_data[5]


# Card Deck Definition
class CardDeck:
    def __init__(self):
        pass


# FOR TESTING
if __name__ == '__main__':
    myCard = Card(8)
    print('ID: {0}, VALUE: {1}, RESOURCE: {2}'.format(myCard.id, myCard.number, myCard.resource_req_type1 + ' & ' + myCard.resource_req_type2 if myCard.resource_req_type2 else myCard.resource_req_type1))
