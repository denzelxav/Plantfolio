import datetime
from enum import Enum

class Health(Enum):
    DEAD = 0
    UNHEALTHY = 1
    SLIGHTLY_UNHEALTHY = 2
    HEALTHY = 3



class Plant:
    def __init__(self,
                 core_id: int,
                 personal_id: int,
                 plant_name: str,
                 icon_type: str,
                 watering_frequency: int,
                 preff_sunlight: int) -> None:

        self.core_id = core_id
        self.personal_id = personal_id
        self.personal_name: None | str = None
        self.plant_name = plant_name
        self.icon_type = icon_type
        self.spot: None | "Spot" = None
        self.health: Health = Health.HEALTHY
        self.watering_frequency = watering_frequency
        self.preff_sunlight = preff_sunlight
        self.watered: None | datetime.datetime = None
        self.nutrition: None | datetime.datetime = None
        self.repotted: None | datetime.datetime = None
        self.notes: None | str = None

