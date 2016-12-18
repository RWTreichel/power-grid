"""
City

Changelog:
12/11/2016 - Created by Justin
"""

# Import Modules


# Class Definition
class City:
    def __init__(self, id):
        self.id = id
        self.owner = None

        # Read in city config file
        city_definitions = '../python_resources/vanilla_cities.csv'
        with open(city_definitions, 'r') as csvfile:
            for row in csvfile:
                row_data = row.replace('\n', '').split(',')
                if str(id) == row_data[0]:
                    self.name = row_data[1]
                    self.region = row_data[2]
                    self.connections = [(row_data[i], row_data[i+1]) for i in range(3, len(row_data)-1) if i % 2 == 1]
                    """
                    FYI - List comprehension example, loop below is same as line above.
                    self.connections = []
                    for i in range(3, len(row_data) - 1):
                        if i % 2 == 1:
                            data = (row_data[i], row_data[i+1])
                            self.connections.append(data)
                    """
                    self.slot_10 = None
                    self.slot_15 = None
                    self.slot_20 = None


# FOR TESTING
if __name__ == '__main__':
    myCity = City(5)
    print('ID: {0}, NAME: {1}, REGION: {2}, CONNECTIONS: {3}'.format(myCity.id, myCity.name,
                                                                     myCity.region, myCity.connections))
