"""
This module contains independent public methods
"""

from __future__ import annotations
import datetime
from project.classes.enums import Sunlight





def string_to_sunlight(sunlight_string: str) -> Sunlight:
    """Converts sunlight string from core database to Sunlight enum"""
    if isinstance(sunlight_string, (str, Sunlight)):
        match sunlight_string:
            case "full shade" | "deep shade":
                return Sunlight.FULL_SHADE
            case "part sun/part shade":
                return Sunlight.PART_SUN
            case "part shade" | "filtered shade":
                return Sunlight.PART_SHADE
            case "full sun" | "full sun only if soil kept moist":
                return Sunlight.FULL_SUN
            case sunlight if isinstance(sunlight, Sunlight):
                return sunlight
            case unexpected_value:
                raise ValueError(f"Unexpected sunlight value {unexpected_value}")
    else:
        raise TypeError(f"Expected str type. Got {type(sunlight_string)}. Value: {sunlight_string}")

def string_to_water_frequency(watering_string: str) -> datetime.timedelta:
    """Converts water frequency string from core database to appropriate datetime.timedelta"""
    if isinstance(watering_string, (str, datetime.timedelta)):
        match watering_string:
            case "Frequent":
                return datetime.timedelta(days=4)
            case "Average":
                return datetime.timedelta(weeks=1)
            case "Minimum":
                return datetime.timedelta(weeks=2)
            case time_delta if isinstance(time_delta, datetime.timedelta):
                return time_delta
            case unexpected_value:
                raise ValueError(f"Unexpected watering_string {unexpected_value}")
    else:
        raise TypeError(
            f"Expected str type. Got {type(watering_string)}. Value: {watering_string}"
        )
