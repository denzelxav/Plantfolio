"""
This file contains the enumerations that are used in the program.
"""


from enum import Enum

class Sunlight(Enum):
    """
    Enum for all possible sunlight conditions
    """
    FULL_SHADE = 0
    PART_SHADE = 1
    PART_SUN = 2
    FULL_SUN = 3


class Health(Enum):
    """
    Enum for all possible health conditions
    """
    DEAD = "dead"
    UNHEALTHY = "unhealthy"
    SLIGHTLY_UNHEALTHY = "slightly_unhealthy"
    HEALTHY = "healthy"

class Action(Enum):
    """
    Enum for all possible Notifications
    """
    WATERING = 0
    NUTRITION = 1
    REPOTTING = 2
