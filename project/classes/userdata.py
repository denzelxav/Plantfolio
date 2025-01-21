import datetime
from project.classes.plant import Plant
from project.classes.spot_notification import Spot
from project.classes.enums import Sunlight, Health
from project.query_function import query_from_database
from project.classes.public_methods import string_to_sunlight, string_to_water_frequency
from project.classes.exceptions import ContainerNotEmpty, NameTakenError, EmptyNameError


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
        if len(new_plant.personal_name) == 0:
            raise EmptyNameError("Plant name cannot be empty")
        if len(self.plants) > 0:
            max_id = max(plant.personal_id for plant in self.plants)
            new_plant.personal_id = max_id+1
        else:
            new_plant.personal_id = 0

        if assigned_spot.room not in self.rooms:
            self.add_room(assigned_spot.room)
        if assigned_spot not in self.rooms[assigned_spot.room]:
            self.add_spot(assigned_spot)

        if assigned_spot in [spot for room in self.rooms.values() for spot in room]:
            new_plant.change_spot(assigned_spot)
            self.plants.append(new_plant)

    def add_spot(self, new_spot: Spot) -> None:
        """
        Adds a spot to an existing room
        """
        if len(new_spot.spot_id) == 0:
            raise EmptyNameError("Spot name cannot be empty")
        if new_spot.room not in self.rooms:
            self.rooms[new_spot.room] = []
        for room in self.rooms.values():
            for spot in room:
                if spot.spot_id.lower() == new_spot.spot_id.lower():
                    raise NameTakenError(f"Spot named {new_spot.spot_id} already exists.")
        self.rooms[new_spot.room].append(new_spot)


    def add_room(self, new_room: str) -> None:
        """
        Adds a new room
        """
        if len(new_room) == 0:
            raise EmptyNameError("Room name cannot be empty.")
        if new_room not in self.rooms:
            self.rooms[new_room] = []
        else:
            raise NameTakenError(f"room with name '{new_room}' already exists'")

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
            self.rooms[bad_spot.room].remove(bad_spot)
        else:
            raise ContainerNotEmpty(f"{bad_spot} is not empty")

    def delete_room(self, room_name: str) -> None:
        """
        Removes a room
        """
        if not self.rooms[room_name]:
            del self.rooms[room_name]
        elif len(self.rooms[room_name]) > 0:
            raise ContainerNotEmpty(f"room: '{room_name}' is not empty and can't be deleted.")

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
        Converts the tasks of a plant to a sorted string of the priority of the tasks
        """
        task_priority = {'repot': 3, 'nutrition': 2, 'water': 1}
        sorted_tasks = sorted(list(plant.current_tasks),
                key=lambda task: task_priority.get(task, 100))
        result = ''.join([task[0] for task in sorted_tasks])
        return result

    def load_spot_data(self, spot_data):
        """
        Loads a spot from a dictionary
        """
        spot_id = spot_data['spot_id']
        light_level = Sunlight[spot_data['light_level']]
        humidity = spot_data['humidity']
        temperature = spot_data['temperature']
        room = spot_data['room']

        spot = Spot(spot_id = spot_id,
                    light_level = light_level,
                    humidity = humidity,
                    assigned_plant = None,
                    temperature = temperature,
                    room = room)

        self.add_room(room)
        self.add_spot(spot)

    def load_plant_data(self, plant: dict):
        """
        Loads a plant from a dictionary
        """
        plant_id = plant['core_id']
        personal_id = plant['personal_id']
        personal_name = plant['personal_name']
        icon_type = plant['icon_type']
        spot_id = plant['spot_id']
        health = Health(plant['health'])
        watered = [datetime.datetime.fromisoformat(date) for date in plant['watered']]
        nutrition = [datetime.datetime.fromisoformat(date) for date in plant['nutrition']]
        repotted = datetime.datetime.fromisoformat(plant['repotted']) if plant['repotted'] else None
        manual_health = plant['manual_health']
        max_log_size = plant['max_log_size']
        notes = plant['notes']
        current_tasks = {str(task) for task in plant['current_tasks']}
        custom_image = plant['custom_image'] if "custom_image" in plant else None

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
        new_plant.custom_icon = custom_image

        for room in self.rooms.values():
            for spot in room:
                if spot.spot_id == spot_id:
                    self.add_plant(new_plant, spot)
                    return

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
