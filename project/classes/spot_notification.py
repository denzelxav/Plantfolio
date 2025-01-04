from __future__ import annotations
from dataclasses import dataclass
import datetime
from typing import TYPE_CHECKING
from project.classes.enums import Sunlight, Action
if TYPE_CHECKING:
    from project.classes.plant import Plant
    from project.classes.notifier import Notifier


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

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Spot):
            return False
        return (self.spot_id == other.spot_id and
                self.light_level == other.light_level and
                self.humidity == other.humidity and
                self.temperature == other.temperature and
                self.room == other.room)

@dataclass
class Notification:
    """Class that stores a notification together with
    the importance(weight), the type and the time
    of the notification for a certain plant.
    """
    weight: float
    original_due_date: datetime.datetime
    time_sent: datetime.datetime
    personal_id_plant: int #is nu de core_id van de plant.
    notification_type: Action
    plant_notification: Plant
    notifier: Notifier
