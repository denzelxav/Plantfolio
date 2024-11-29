import datetime
from enum import Enum
from typing import Type

class Spot:
    """Placeholder Spot class"""
    pass

class Health(Enum):
    DEAD = 0
    UNHEALTHY = 1
    SLIGHTLY_UNHEALTHY = 2
    HEALTHY = 3



class Plant:
    """Plant object that holds information about a specific plant the user has.
        attributes:
        - core_id(int): the id the plant has in the core database
        - personal_id(int): the id the plant has in the user database
        - personal_name(str): the name of the plant in the user database
        - plant_name(str): the name of the plant in the core database
        - icon_type(str): the type of icon the plant will show in the interface
        - spot(Spot): the spot where the plant is located
        - health(Health): indication how healthy the plant is based
        - watering_frequency(int): the frequency at which the plant should be watered
        - preff_sunlight(int): the amount of sunlight that is best for the plant
        - watered(datetime.datetime): the moment the plant was last watered
        - nutrition(datetime.datetime): the moment the plant last received nutrition
        - repotted(datetime.datetime): the moment the plant was last repotted
        - notes(str): users notes about the plant
    """
    def __init__(self,
                 core_id: int,
                 personal_id: int,
                 core_name: str,
                 icon_type: str,
                 watering_frequency: int,
                 preff_sunlight: int) -> None:

        self.core_id = core_id
        self.personal_id = personal_id
        self.personal_name: None | str = None
        self.core_name = core_name
        self.icon_type = icon_type
        self.spot: None | Spot = None
        self.health: Health = Health.HEALTHY
        self.watering_frequency = watering_frequency
        self.preff_sunlight = preff_sunlight
        self.watered: None | datetime.datetime = None
        self.nutrition: None | datetime.datetime = None
        self.repotted: None | datetime.datetime = None
        self.notes: None | str = None

    def give_nutrition(self) -> None:
        """Sets time when plant last received nutrition to the current date and time"""
        self.nutrition = datetime.datetime.now()

    def change_spot(self, spot: Spot) -> None:
        """Changes spot of the plant"""
        self.spot = spot

    def water_plant(self) -> None:
        """Sets time when plant was last watered to current moment."""
        self.watered = datetime.datetime.now()


    def __repr__(self) -> str:
        return (f"Plant({self.core_id}, {self.personal_id}, {self.core_name}, {self.icon_type}, "
                f"{self.watering_frequency}, {self.preff_sunlight})")

    def __str__(self) -> str:
        return f"{self.personal_id}: {self.core_name}"

