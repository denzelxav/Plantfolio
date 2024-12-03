from dataclasses import dataclass
from datetime import datetime

class Plant:
    pass

@dataclass
class Spot:
    '''Class for setting the attributes for a spot created in a room
    with the properties lightlevel, humidity, temperature and 
    setting a plant to a spot.'''
    spot_id: str
    light_level: str
    humidity: str
    assigned_plant: Plant | None
    temperature: int

@dataclass
class Notification:
    '''Class that stores a notification together with 
    the importance(weight), the type and the time 
    of the notification for a certain plant.
    '''
    weight: int
    time_sent: datetime
    name: str
    notification_type: str
    plant_notification: Plant




