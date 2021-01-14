from abc import ABCMeta, abstractmethod


class Building(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, building_name):
        self.building_name=building_name
        pin = random.randint(999, 9999)
        self.building_id=pin

class Bungalow(Building):
    def __init__(self, building_name):
        Building.__init__(self, )
        self.no_of_floors = 1
        self.no_of_bedrooms=3
        self.building_name='Bungalow'
        self.max_no_occupants = 4


    def __repr__(self):
        return (self.building_name, self.building_type, self.no_of_floors, self.no_of_bedrooms)

class mansionette(Building):
    def __init__(self, building_name):
        Building.__init__(self, building_name)
        self.no_of_floors = 3
        self.no_of_bedrooms=6
        self.building_type='Mansionette'
        self.max_no_occupants = 10

    def __repr__(self):
        return (self.building_name, self.building_type, self.no_of_floors, self.no_of_bedrooms)

class Mansion(Building):
    def __init__(self, building_name):
        Building.__init__(self, building_name)
        self.no_of_floors = 2
        self.no_of_bedrooms=4
        self.building_type='Mansion'
        self.max_no_occupants = 6

    def __repr__(self):
        return (self.building_name, self.building_type, self.no_of_floors, self.no_of_bedrooms)

class Manyatta(Building):
    def __init__(self, building_name):
        Building.__init__(self, building_name)
        self.no_of_floors = 1
        self.no_of_bedrooms=1
        self.building_type='Maasai Manyatta'
        self.max_no_occupants = 2

    def __repr__(self):
        return (self.building_name, self.building_type, self.no_of_floors, self.no_of_bedrooms)
