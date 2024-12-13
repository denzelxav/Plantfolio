"""
Module containing the Plant class which handles the data from a single plant.
The time_average public method is also included for easy calculation of averages
between datetime entries in a sequence.

It also contains the plant_from_database function
that creates a plant class based on the database data.
"""

import datetime
from collections.abc import Sequence

from project.classes.public_methods import string_to_water_frequency, string_to_sunlight
from project.classes.spot_notification import Spot
from project.classes.enums import Health, Sunlight
from project.query_function import query_from_database
from project.classes.spot_notification import Spot, Notification
from project.classes.enums import Health, Sunlight, Type_of_action

def time_average(events: Sequence[datetime.datetime]) -> datetime.timedelta:
    """
    Calculates the average time inbetween datetime events in a list of datetime objects.

    Arguments:
        events(list[datetime.datetime]): list of datetime objects to calculate the average time for.

    Returns:
        datetime.timedelta: average time between events
    """
    time_sum = datetime.timedelta()
    for i in range(len(events) - 1, 0, -1):
        if events[i] < events[i - 1]:
            raise ValueError(
                f"Entry {i} is before entry {i - 1}. "
                f"({i}: {events[i]}. {i - 1}: {events[i - 1]})"
            )
        time_sum += events[i] - events[i - 1]
    time_avg = time_sum / (len(events) - 1)
    return time_avg

class Plant:
    """
    Plant object that holds information about a specific plant the user has.
        attributes:
        - core_id(int): the id the plant has in the core database
        - personal_id(int): the id the plant has in the user database
        - personal_name(str): the name of the plant in the user database
        - scientific_name(str): the scientific name of the plant in the core database
        - core_name(str): the name of the plant in the core database
        - icon_type(str): the type of icon the plant will show in the interface
        - spot(Spot): the spot where the plant is located
        - health(Health): indication how healthy the plant is based
        - watering_frequency(datetime.timedelta): the optimal time between watering entries
        - preff_sunlight(list[Sunlight]): Best sunlight options for the plant
        - watered(list[datetime.datetime]): Log of the last few times the plant received water
        - nutrition(list[datetime.datetime]): Log of the last few times the plant received nutrition
        - repotted(datetime.datetime): the moment the plant was last repotted
        - manual_health(bool): Signifies if health should be refreshed by the get_health_score
                               function or from manually set health attribute
        - max_log_size(int): the number of entries before that log sizes deletes the oldest value.
        - notes(str): users notes about the plant
    """
    def __init__(self,
                 core_id: int,
                 personal_id: int,
                 scientific_name: str,
                 core_name: str,
                 icon_type: str,
                 watering_frequency: datetime.timedelta,
                 preff_sunlight: list[Sunlight]) -> None:

        self.core_id = core_id
        self.personal_id = personal_id
        self.personal_name: None | str = None
        self.scientific_name: str = scientific_name
        self.core_name = core_name
        self.icon_type = icon_type
        self.spot: None | Spot = None
        self.health: Health = Health.HEALTHY
        self.watering_frequency = watering_frequency
        self.preff_sunlight = preff_sunlight
        self.watered: list[datetime.datetime] = []
        self.nutrition: list[datetime.datetime] = []
        self.repotted: None | datetime.datetime = None
        self.notes: None | str = None
        self.manual_health: bool = False
        self.max_log_size: int = 4
        self.water_score: None | int = None # type: ignore
        self.sunlight_score: int = 0 # type: ignore
        self.nutrition_score: None | int = None # type: ignore
        self.current_tasks: set[str] = set() # choose from repot, water, nutrition
        self.water_plant()
        self.give_nutrition()

    def give_nutrition(self, list_notifications) -> list[Notification]:
        """
        Sets time when plant last received nutrition to the current date and time and deletes notifcation
        """
        self.nutrition.append(datetime.datetime.now())
        if len(self.nutrition) > self.max_log_size:
            del self.nutrition[0]
        self._nutrition_score: int | None = None

        # remove the task from the notifications
        for notification in list_notifications:
            if notification.name == self.core_id and notification.notification_type == Type_of_action.NUTRITION:
                list_notifications.remove(notification)
        return list_notifications

    def change_spot(self, spot: Spot) -> None:
        """
        Changes spot of the plant and calculates new sunlight score
        """
        self.spot = spot
        self.spot.assigned_plant = self
        self.sunlight_score = self.get_sunlight_score()

    def water_plant(self, list_notifications) -> list[Notification]:
        """
        Sets time when plant was last watered to current moment. and deletes water_score cache and notification
        """
        if len(self.watered) > 1 and datetime.datetime.now() < self.watered[-1]:
            raise ValueError(f"Last watering entry is in the future. ({self.watered[-1]})")
        self.watered.append(datetime.datetime.now())

        if len(self.watered) > self.max_log_size:
            del self.watered[0]
        self._water_score: int | None = None

        for notification in list_notifications:
            if notification.name == self.core_id and notification.notification_type == Type_of_action.WATERING:
                list_notifications.remove(notification)
        return list_notifications

    def repot_plant(self, list_notifications) -> list[Notification]:
        """
        Sets time when plant was last repotted to current moment.
        """
        self.repotted = datetime.datetime.now()
        for notification in list_notifications:
            if notification.name == self.core_id and notification.notification_type == Type_of_action.REPOTTING:
                list_notifications.remove(notification)
        return list_notifications

    def get_water_score(self) -> int:
        """
        Calculates the water score based on time between watering sessions.
        """
        time_avg = time_average(self.watered)

        max_deviation = self.watering_frequency * 2

        if not (self.watering_frequency - max_deviation
                <= time_avg <=
                self.watering_frequency + max_deviation):
            return 0

        water_score = ((-(time_avg.days - self.watering_frequency.days)**2 + max_deviation.days**2)/
                       (max_deviation.days**2))

        return int(water_score * 100)

    def time_to_water_score(self) -> int:
        """
        Returns score based on time between now and last watering session
        """
        time_diff = datetime.datetime.now() - self.watered[-1]
        max_deviation = self.watering_frequency * 2
        if time_diff < self.watering_frequency:
            return 100
        if time_diff > self.watering_frequency + max_deviation:
            return 0
        score = ((-(time_diff.days - self.watering_frequency.days) ** 2 + max_deviation.days ** 2)/
                 (max_deviation.days ** 2))
        return int(score * 100)

    def get_nutrition_score(self) -> int:
        """
        Calculates the nutrition score based on time between nutrition entries
        """

        time_avg = time_average(self.nutrition)

        nutrition_frequency = datetime.timedelta(days=30)
        max_deviation = nutrition_frequency * 2

        if time_avg < nutrition_frequency:
            return 100
        if time_avg > nutrition_frequency + max_deviation:
            return 0

        nutrition_score = \
            ((-(time_avg.days - nutrition_frequency.days) ** 2 + max_deviation.days ** 2) /
             (max_deviation.days ** 2))
        return int(nutrition_score * 100)

    def time_to_feed_score(self) -> int:
        """
        Returns score based on time between now and last time the plant received nutrition
        """
        time_diff = datetime.datetime.now() - self.nutrition[-1]
        nutrition_frequency = datetime.timedelta(days=30)
        max_deviation = nutrition_frequency * 2
        if time_diff < nutrition_frequency:
            return 100
        if time_diff > nutrition_frequency + max_deviation:
            return 0
        score = (-(time_diff.days - nutrition_frequency.days) ** 2 + max_deviation.days ** 2) / (
                    max_deviation.days ** 2)
        return int(score * 100)


    def get_sunlight_score(self) -> int:
        """
        returns score based on how close the current sunlight is to that preferred by the plant
        """
        if self.spot:
            diff_to_preff = min(abs(self.spot.light_level.value - pref.value)
                                for pref in self.preff_sunlight)
            return int(100 - diff_to_preff*25)
        return 0


    def get_health_score(self) -> int:
        """
        Returns a health score ranging from 0 to 100, based on nutrition, water and sunlight.
        Returns -1 when health score was not calculated
        """
        if self.manual_health:
            return  -1
        if self._health == Health.DEAD:
            return -1
        time_to_water_score = self.time_to_water_score()
        time_to_feed_score = self.time_to_feed_score()
        health_score = (0.25 * self.water_score +
                        0.20 * time_to_water_score +
                        0.45 * self.sunlight_score +
                        0.05 * self.nutrition_score +
                        0.05 * time_to_feed_score)
        return int(health_score)

    @property
    def health(self) -> Health:
        """
        returns health status and calculates it from health score if needed.
        """
        health_score = self.get_health_score()
        if health_score == -1:
            return self._health

        if health_score <= 33:
            new_health = Health.UNHEALTHY
        elif health_score <= 66:
            new_health = Health.SLIGHTLY_UNHEALTHY
        else:
            new_health = Health.HEALTHY
        self._health: Health = new_health
        return new_health

    @health.setter
    def health(self, value: Health) -> None:
        self._health = value


    @property
    def water_score(self) -> int:
        """
        returns cached water score if available and calculates new one otherwise
        """
        if len(self.watered) < 2:
            return 0

        if self._water_score:
            return self._water_score

        new_score = self.get_water_score()
        self._water_score = new_score
        return new_score

    @water_score.setter
    def water_score(self, value: int | None) -> None:
        self._water_score = value

    @property
    def nutrition_score(self) -> int:
        """
        returns cached nutrition score if available and calculates new one otherwise
        """
        if len(self.nutrition) < 2:
            return 0
        if self._nutrition_score is None:
            self._nutrition_score = self.get_nutrition_score()
        assert self._nutrition_score is not None
        return self._nutrition_score

    @nutrition_score.setter
    def nutrition_score(self, value: int | None) -> None:
        self._nutrition_score = value

    @property
    def preff_sunlight(self) -> list[Sunlight]:
        """
        returns list of preferred sunlight conditions
        """
        return self._preff_sunlight

    @preff_sunlight.setter
    def preff_sunlight(self, value: list[Sunlight]) -> None:
        """
        Sets preferred sunlight and recalculates cached sunlight score if a spot has been set.
        """

        self._preff_sunlight = value
        if self.spot:
            self.sunlight_score = self.get_sunlight_score()

    def __repr__(self) -> str:
        return (f"Plant({self.core_id}, {self.personal_id}, {self.core_name}, {self.icon_type}, "
                f"{self.watering_frequency}, {self.preff_sunlight})")

    def __str__(self) -> str:
        return f"{self.personal_id}: {self.core_name}"


def plant_from_database(plant_id: int) -> Plant:
    """Returns Plant object with given id from core database."""
    query = ("SELECT scientific_name, common_name, watering, sunlight_list "
             "FROM plant_details "
             f"WHERE plant_id = '{plant_id}'")

    query_res = query_from_database(query)[0]

    if isinstance(query_res[0], str):
        scientific_name = query_res[0]
    else:
        raise TypeError(f"scientific_name must be str, "
                        f"got {type(query_res[0])}. Value: {query_res[0]}")
    if isinstance(query_res[1], str):
        common_name = query_res[1]
    else:
        raise TypeError(f"common_name must be str, got {type(query_res[1])}. Value: {query_res[1]}")
    if isinstance(query_res[2], str):
        watering = string_to_water_frequency(query_res[2])
    else:
        raise TypeError(f"watering must be str, got {type(query_res[2])}. Value: {query_res[2]}")
    if isinstance(query_res[3], str):
        sunlight_list = [string_to_sunlight(sunlight)
                         for sunlight in  query_res[3].strip("[").strip("]")\
                             .replace('"',"").split(",")]
    else:
        raise TypeError(f"sunlight must be string, got {type(query_res[3])}. Value: {query_res[3]}")
    plant = Plant(plant_id, 1, scientific_name, common_name,
                 "default", watering,
                 sunlight_list
                 )
    return plant
