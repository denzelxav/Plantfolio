from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from project.classes.enums import Sunlight
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from project.classes.plant import Plant


@dataclass
class Spot:
    """Class for setting the attributes for a spot created in a room
    with the properties lightlevel, humidity, temperature and
    setting a plant to a spot."""
    spot_id: str
    light_level: Sunlight
    humidity: str
    assigned_plant: Plant | None
    temperature: int

@dataclass
class Notification:
    """Class that stores a notification together with
    the importance(weight), the type and the time
    of the notification for a certain plant.
    """
    weight: int
    time_sent: datetime
    name: str
    notification_type: str
    plant_notification: Plant




