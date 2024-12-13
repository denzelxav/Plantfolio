import datetime
from project.classes.plant import Plant
from project.classes.spot_notification import Spot
from project.classes.enums import Sunlight, Health
from project.query_function import query_from_database
from project.classes.public_methods import string_to_sunlight, string_to_water_frequency, string_to_health


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
        self.plants: set[Plant]= set()
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
                          key=lambda plant: getattr(plant, attribute).lower(), reverse=reverse)
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
            spot_id = str(spot_data['spot_id'])
        else:
            raise ValueError('spot_id must be a string')

        if isinstance(spot_data['light_level'], str):
            light_level = Sunlight[str(spot_data['light_level'])]
        else:
            raise ValueError('light_level must be a string')

        if isinstance(spot_data['humidity'], str):
            humidity = str(spot_data['humidity'])
        else:
            raise ValueError('humidity must be a string')

        if isinstance(spot_data['temperature'], float):
            temperature = float(spot_data['temperature'])
        else:
            raise ValueError(f'temperature must be a integer. Got {type(spot_data['temperature'])}. value {spot_data["temperature"]}')

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
        if isinstance(plant['core_id'], int):
            plant_id = int(plant['core_id'])
        else:
            raise ValueError(f'core_id must be a integer. Got {type(plant["core_id"])}. value {plant["core_id"]}')
        if isinstance(plant['personal_id'], int):
            personal_id = int(plant['personal_id'])
        else:
            raise ValueError(f'personal_id must be a integer. Got {type(plant['personal_id'])}. value {plant["personal_id"]}')
        if isinstance(plant['personal_name'], str):
            personal_name = str(plant['personal_name'])
        elif not plant['personal_name']:
            personal_name = None
        else:
            raise ValueError('personal_name must be a string or None')
        if isinstance(plant['icon_type'], str):
            icon_type = str(plant['icon_type'])
        else:
            raise ValueError('icon_type must be a string')
        if isinstance(plant['spot_id'], str):
            spot_id = str(plant['spot_id'])
        else:
            raise ValueError('spot_id must be a string')
        if isinstance(plant['health'], str):
            health = string_to_health((plant['health']))
        else:
            raise ValueError(f'health must be a integer. Got {type(plant["health"])}. value {plant["health"]}')
        if isinstance(plant['watered'], list):
            watered = [datetime.datetime.fromisoformat(date)
                       for date in plant['watered']
                       if isinstance(date, str)]
        else:
            raise ValueError('watered must be a list of datetime objects')
        if isinstance(plant['nutrition'], list):
            nutrition = [datetime.datetime.fromisoformat(date)
                         for date in plant['nutrition']
                         if isinstance(date, str)]
        else:
            raise ValueError('nutrition must be a list of datetime objects')
        if isinstance(plant['repotted'], str):
            repotted = datetime.datetime.fromisoformat(plant['repotted'])
        elif not plant['repotted']:
            repotted = None
        else:
            raise ValueError('repotted must be a str object or None')
        if isinstance(plant['manual_health'], bool):
            manual_health = bool(plant['manual_health'])
        else:
            raise ValueError('manual_health must be a boolean')
        if isinstance(plant['max_log_size'], int):
            max_log_size = int(plant['max_log_size'])
        else:
            raise ValueError('max_log_size must be a integer')
        if isinstance(plant['notes'], str):
            notes = str(plant['notes'])
        elif not plant['notes']:
            notes = None
        else:
            raise ValueError('notes must be a string or None')
        if isinstance(plant['current_tasks'], list):
            current_tasks = {str(task) for task in plant['current_tasks']}
        else:
            raise ValueError('current_tasks must be a list')

        core_name = self.get_core_name(plant_id)
        scientific_name = self.get_scientific_name(plant_id)
        watering_frequency = self.get_watering_frequency(plant_id)
        watering_frequency_timedelta = string_to_water_frequency(watering_frequency)
        preff_sunlight = self.get_preferred_sunlight(plant_id)
        preff_sunlight_enums = []
        for sunlight in preff_sunlight:
            preff_sunlight_enums.append(string_to_sunlight(sunlight))

        new_plant = Plant(plant_id,
                          personal_id,
                          scientific_name,
                          core_name,
                          icon_type,
                          watering_frequency_timedelta,
                          preff_sunlight_enums)

        new_plant.personal_name = personal_name
        new_plant.health = health
        new_plant.watered = watered
        new_plant.nutrition = nutrition
        new_plant.repotted = repotted
        new_plant.manual_health = manual_health
        new_plant.max_log_size = max_log_size
        new_plant.notes = notes
        new_plant.current_tasks = current_tasks

        for room in self.rooms.values():
            for spot in room:
                if spot.spot_id == spot_id:
                    self.add_plant(new_plant, spot)

    def get_core_name(self, plant_id: int) -> str:
        """
        Returns the core name of a plant from the database
        """
        result = query_from_database(f"""
                                    SELECT common_name
                                    FROM plant_details
                                    WHERE plant_id = '{plant_id}'
                                    """)
        return str(result[0][0])

    def get_scientific_name(self, plant_id: int) -> str:
        """
        Returns the scientific name of a plant from the database
        """
        result = query_from_database(f"""
                                    SELECT scientific_name
                                    FROM plant_details
                                    WHERE plant_id = '{plant_id}'
                                    """)
        return str(result[0][0])

    def get_watering_frequency(self, plant_id: int) -> str:
        """
        Returns the watering frequency of a plant from the database
        """
        result = query_from_database(f"""
                                    SELECT watering
                                    FROM plant_details
                                    WHERE plant_id = '{plant_id}'
                                    """)
        return str(result[0][0])

    def get_preferred_sunlight(self, plant_id: int) -> list[str]:
        """
        Retuns the preferred sunlight of a plant from the database
        """
        result = query_from_database(f"""
                                    SELECT sunlight_list
                                    FROM plant_details
                                    WHERE plant_id = '{plant_id}'
                                    """)

        preff_sunlight_big_str = str(result[0][0]).replace('[', '').replace(']', '').split(',')
        preff_sunlight_small_strs = [s.strip('"') for s in preff_sunlight_big_str]
        return preff_sunlight_small_strs


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, UserData):
            return False
        return (self.plants == other.plants and
                self.rooms == other.rooms and
                self.pet_toxicity == other.pet_toxicity)
