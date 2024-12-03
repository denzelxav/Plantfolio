from project.classes.plant import Plant
from project.classes.spot_notification import Spot



class UserData:

    '''Userdata stores all the current data of the user. 
    It has thee attributes: 
    Plants, which keeps track of all the plants the user currently owns, this is a set of Plant objects.
    Rooms, which is a dictonary where the key is the room name and the value is a list of Spot objects.
    Preferences, which is a dictionary where the key is the type of preference, such as 'pet toxicity'
    and the value is the information about this preference
    '''

    def __init__(self) -> None:
        self.plants: set[Plant]= set()
        self.rooms: dict[str, list[Spot]] = {}
        self.preferences: dict[str, bool|str] = {}

    def water_all(self) -> None:
        '''Water all the plants in the users possesion'''
        for plant in self.plants:
            plant.water_plant()

    def add_plant(self, new_plant: Plant, assigned_spot: Spot) -> None:
        '''Adds a plant'''
        if assigned_spot in [spot for room in self.rooms.values() for spot in room]:
            new_plant.change_spot(assigned_spot)
            self.plants.add(new_plant)

    def add_spot(self, new_spot: Spot, room: str) -> None:
        '''Adds a spot to an existing room'''
        self.rooms[room].append(new_spot)

    def add_room(self, new_room: str) -> None:
        '''Adds a new room'''
        if new_room not in self.rooms:
            self.rooms[new_room] = []

    def delete_plant(self, bad_plant: Plant) -> None:
        '''Removes a plant based on the name'''
        if bad_plant.spot:
            bad_plant.spot.assigned_plant = None
        self.plants.remove(bad_plant)

    def delete_spot(self, bad_spot: Spot) -> None:
        '''Removes a spot, but only if it is empty'''
        if bad_spot.assigned_plant is None:
            for room in self.rooms.items():
                if bad_spot in self.rooms[room]:
                    self.rooms[room].remove(bad_spot)