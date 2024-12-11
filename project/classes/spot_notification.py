from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING
from project.classes.enums import Sunlight
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
    room: str

    def get_spot_data(self) -> dict[str, str | int | Sunlight]:
        """
        Returns the spot data in a dictionary format to save in a json file
        """
        return {"spot_id": self.spot_id,
                "light_level": self.light_level,
                "humidity": self.humidity,
                "temperature": self.temperature,
                "room": self.room}

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
