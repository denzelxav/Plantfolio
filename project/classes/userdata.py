from project.classes.plant import Plant
from project.classes.spot_notification import Spot



class UserData:

    """
    Userdata stores all the current data of the user. 
    It has the attributes:

    Plants, which keeps track of all the plants the user currently owns, 
    this is a set of Plant objects.

    Rooms, which is a dictionary where the key is the room name and the
    value is a list of Spot objects.

    Preferences, which is a dictionary where the key is the type 
    of preference, such as 'pet toxicity' and the value is the
    information about this preference
    """

    def __init__(self) -> None:
        self.plants: list[Plant]= []
        self.rooms: dict[str, list[Spot]] = {}
        self.pet_toxicity = False

    def water_all(self) -> None:
        """
        Water all the plants in the users possession
        """
        for plant in self.plants:
            plant.water_plant()

    def add_plant(self, new_plant: Plant, assigned_spot: Spot) -> None:
        """
        Adds a plant
        """
        if len(self.plants) > 0:
            max_id = max(plant.personal_id for plant in self.plants)
            new_plant.personal_id = max_id+1
        else:
            new_plant.personal_id = 0
            
        if assigned_spot in [spot for room in self.rooms.values() for spot in room]:
            new_plant.change_spot(assigned_spot)
            self.plants.append(new_plant)

    def add_spot(self, new_spot: Spot, room: str) -> None:
        """
        Adds a spot to an existing room
        """
        self.rooms[room].append(new_spot)

    def add_room(self, new_room: str) -> None:
        """
        Adds a new room
        """
        if new_room not in self.rooms:
            self.rooms[new_room] = []

    def delete_plant(self, bad_plant: Plant) -> None:
        """
        Removes a plant based on the name
        """
        if bad_plant.spot:
            bad_plant.spot.assigned_plant = None
        self.plants.remove(bad_plant)

    def delete_spot(self, bad_spot: Spot) -> None:
        """
        Removes a spot, but only if it is empty
        """
        if bad_spot.assigned_plant is None:
            for spots in self.rooms.values():
                if bad_spot in spots:
                    spots.remove(bad_spot)

    def delete_room(self, room_name: str) -> None:
        """
        Removes a room 
        """
        if self.rooms[room_name] == []:
            del self.rooms[room_name]

    def sort_plants(self, attribute: str, reverse: bool) -> list[Plant] | None:
        '''Sorts the plants based on the prompted attribute'''
        if attribute in ['core_name', 'scientific_name', 'personal_name']:
            return sorted(list(self.plants),
                          key=lambda plant: getattr(plant, attribute), reverse=reverse)
        if attribute == 'room':
            result = []
            for room in sorted(self.rooms.keys(), reverse=reverse):
                result.extend([plant for plant in self.plants if plant.spot in self.rooms[room]])
            return result
        if attribute == 'current_task':
            return sorted(list(self.plants), key=self.tasks_to_string, reverse=reverse)
        return None

    def tasks_to_string(self, plant: Plant) -> str:
        '''Converts the tasks of a plant to a sorted string of the first letter of each task'''
        result = ''
        sorted_tasks = sorted(list(plant.current_tasks))
        for task in sorted_tasks:
            result += task[0]
        return result
