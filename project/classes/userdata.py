import datetime
from project.classes.plant import Plant
from project.classes.spot_notification import Spot
from project.classes.enums import Sunlight
from project.query_function import query_from_database



class UserData:

    """
    Userdata stores all the current data of the user. 
    It has thee attributes: 

    Plants, which keeps track of all the plants the user currently owns, 
    this is a set of Plant objects.

    Rooms, which is a dictonary where the key is the room name and the 
    value is a list of Spot objects.

    Preferences, which is a dictionary where the key is the type 
    of preference, such as 'pet toxicity'and the value is the 
    information about this preference
    """

    def __init__(self) -> None:
        self.plants: set[Plant]= set()
        self.rooms: dict[str, list[Spot]] = {}
        self.pet_toxicity = False

    def water_all(self) -> None:
        """
        Water all the plants in the users possesion
        """
        for plant in self.plants:
            plant.water_plant()

    def add_plant(self, new_plant: Plant, assigned_spot: Spot) -> None:
        """
        Adds a plant
        """
        if assigned_spot not in [spot for room in self.rooms.values() for spot in room]:
            self.add_room(assigned_spot.room)
            self.add_spot(assigned_spot)

        if assigned_spot in [spot for room in self.rooms.values() for spot in room]:
            new_plant.change_spot(assigned_spot)
            self.plants.add(new_plant)

    def add_spot(self, new_spot: Spot) -> None:
        """
        Adds a spot to an existing room
        """
        if new_spot.room not in self.rooms:
            self.rooms[new_spot.room] = []
        self.rooms[new_spot.room].append(new_spot)

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
        """
        Sorts the plants based on the prompted attribute
        """
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
        """
        Converts the tasks of a plant to a sorted string of the first letter of each task
        """
        result = ''
        sorted_tasks = sorted(list(plant.current_tasks))
        for task in sorted_tasks:
            result += task[0]
        return result

    def load_spot_data(self, spot_data: dict[str, str | int]) -> None:
        """
        Loads a spot from a dictionary
        """
        if isinstance(spot_data['spot_id'], str):
            spot_id = int(spot_data['spot_id'])
        else:
            raise ValueError('spot_id must be a string')
        
        if isinstance(spot_data['light_level'], str):
            light_level = Sunlight[str(spot_data['light_level'])]
        else:
            raise ValueError('light_level must be a string')
        
        if isinstance(spot_data['humidity'], str):
            humidity = str(spot_data['humidity'])

        if isinstance(spot_data['temperature'], int):
            temperature = int(spot_data['temperature'])

        if isinstance(spot_data['room'], str):
            room = str(spot_data['room'])
        else:
            raise ValueError('room must be a string')
        
        spot = Spot(spot_id = spot_id,
                    light_level = light_level,
                    humidity = humidity,
                    assigned_plant = None,
                    temperature = temperature,
                    room = room)

        self.add_room(room)
        self.add_spot(spot)

    def load_plant_data(self,
                        plant: dict[str, str | int | list[datetime.datetime] | list[str] | None]
                        ) -> None:
        """
        Loads a plant from a dictionary
        """
        plant_id = plant['core_id']
        personal_id = plant['personal_id']
        scientific_name = self.get_scientific_name(plant_id)
        core_name = plant['personal_name']
        icon_type = plant['icon_type']
        watering_frequency = self.get_watering_frequency(plant_id)
        preff_sunlight = self.get_preferred_sunlight(plant_id)

        new_plant = Plant(plant_id,
                          personal_id,
                          scientific_name,
                          core_name,
                          icon_type,
                          watering_frequency,
                          preff_sunlight)

        for room in self.rooms.values():
            for spot in room:
                if spot.spot_id == plant['spot_id']:
                    self.add_plant(new_plant, spot)

    def get_scientific_name(self, plant_id: str) -> str:
        """
        Returns the scientific name of a plant from the database
        """
        result = query_from_database(f"""
                                    SELECT scientific_name
                                    FROM plant_details
                                    WHERE plant_id = '{plant_id}'
                                    """)
        return result[0][0] if result else None

    def get_watering_frequency(self, plant_id: str) -> datetime.timedelta:
        """
        Returns the watering frequency of a plant from the database
        """
        result = query_from_database(f"""
                                    SELECT watering
                                    FROM plant_details
                                    WHERE plant_id = '{plant_id}'
                                    """)
        watering_frequency_str = result[0][0] if result else None
        watering_mapping = {
            'Frequent': datetime.timedelta(days=1),
            'Average': datetime.timedelta(days=3),
            'Minimum': datetime.timedelta(days=7)
        }
        return watering_mapping.get(watering_frequency_str, datetime.timedelta(days=0))

    def get_preferred_sunlight(self, plant_id: str) -> list[Sunlight]:
        """
        Retuns the preferred sunlight of a plant from the database
        """
        result = query_from_database(f"""
                                    SELECT sunlight_list
                                    FROM plant_details
                                    WHERE plant_id = '{plant_id}'
                                    """)
        if result:
            preff_sunlight_big_str = result[0][0].replace('[', '').replace(']', '').split(',')
            preff_sunlight_small_strs = [s.strip('"') for s in preff_sunlight_big_str]
            enum_lights = [light.upper().replace(' ', '_') for light in preff_sunlight_small_strs]
            return [Sunlight[enum_light] for enum_light in enum_lights]
        return [Sunlight.FULL_SHADE, Sunlight.FULL_SUN, Sunlight.PART_SHADE, Sunlight.PART_SUN]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, UserData):
            return False
        return (self.plants == other.plants and
                self.rooms == other.rooms and
                self.pet_toxicity == other.pet_toxicity)
