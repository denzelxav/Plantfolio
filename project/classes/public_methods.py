"""
This module contains independent public methods
"""

from __future__ import annotations
import datetime
from project.classes.enums import Sunlight, Health


def string_to_sunlight(sunlight_string: str) -> Sunlight:
    """Converts sunlight string from core database to Sunlight enum"""
    if isinstance(sunlight_string, (str, Sunlight)):
        match sunlight_string:
            case "full shade" | "deep shade":
                return Sunlight.FULL_SHADE
            case "part sun" | "part sun/part shade":
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

def sunlight_to_string(sunlight: Sunlight) -> str:
    """
    Returns string representation of Sunlight enum
    """
    match sunlight:
        case Sunlight.FULL_SHADE:
            return "full shade"
        case Sunlight.PART_SUN:
            return "part sun/part shade"
        case Sunlight.PART_SHADE:
            return "part shade"
        case Sunlight.FULL_SUN:
            return "full sun"
        case unexpected_value:
            raise ValueError(f"Unexpected sunlight value {unexpected_value}")


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

def get_sun_icon_path(sunlight: Sunlight) -> str:
    """
    returns the path to the appropriate sunlight icon
    """
    match sunlight:
        case Sunlight.FULL_SHADE:
            return "./project/art/full_shade.png"
        case Sunlight.PART_SUN:
            return "./project/art/half_sun.png"
        case Sunlight.PART_SHADE:
            return "./project/art/half_shade.png"
        case Sunlight.FULL_SUN:
            return "./project/art/full_sun.png"
        case unexpected_value:
            raise ValueError(f"Unexpected sunlight value {unexpected_value}")

def string_to_health(health: str) -> Health:
    """
    Returns Health enum that corresponds to given string
    """
    match health.lower():
        case "healthy":
            return Health.HEALTHY
        case "slightly unhealthy" | "slightly_unhealthy":
            return Health.SLIGHTLY_UNHEALTHY
        case "unhealthy":
            return Health.UNHEALTHY
        case "dead":
            return Health.DEAD
        case unexpected_value:
            raise ValueError(f"Unexpected health value {unexpected_value}")


def health_to_string(health: Health) -> str:
    """
    Returns string representation of health enum
    """
    match health:
        case Health.DEAD:
            return "dead"
        case Health.UNHEALTHY:
            return "unhealthy"
        case Health.SLIGHTLY_UNHEALTHY:
            return "slightly unhealthy"
        case Health.HEALTHY:
            return "healthy"
        case unexpected_value:
            raise ValueError(f"Unexpected health value {unexpected_value}")
