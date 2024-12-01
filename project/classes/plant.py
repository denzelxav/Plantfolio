import datetime
from enum import Enum

class Sunlight(Enum):
    FULL_SHADE = 0
    PART_SHADE = 1
    PART_SUN = 2
    FULL_SUN = 3

class Spot:
    """Placeholder Spot class"""
    def __init__(self, sunlight: Sunlight):
        self.sunlight = sunlight
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
        - watering_frequency(datetime.timedelta): the optimal time between watering entries
        - preff_sunlight(list[str]): List containing the best sunlight options for the plant
        - watered(list[datetime.datetime]): Log of the last few times the plant received water
        - nutrition(list[datetime.datetime]): Log of the last few times the plant received nutrition
        - repotted(datetime.datetime): the moment the plant was last repotted
        - notes(str): users notes about the plant
        - max_log_size(int): the maximum amount of entries in the watering and nutrition logs
    """
    def __init__(self,
                 core_id: int,
                 personal_id: int,
                 core_name: str,
                 icon_type: str,
                 watering_frequency: datetime.timedelta,
                 preff_sunlight: list[Sunlight]) -> None:

        self.core_id = core_id
        self.personal_id = personal_id
        self.personal_name: None | str = None
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
        self.max_log_size: int = 20
        self._water_score: None | int = None
        self._sunlight_score: None | int = None
        self._nutrition_score: None | int = None

    def give_nutrition(self) -> None:
        """Sets time when plant last received nutrition to the current date and time"""
        self.nutrition.append(datetime.datetime.now())
        if len(self.nutrition) > self.max_log_size:
            del self.nutrition[0]
        self._nutrition_score = None

    def change_spot(self, spot: Spot) -> None:
        """Changes spot of the plant"""
        self.spot = spot
        self.sunlight_score = self.get_sunlight_score()

    def water_plant(self) -> None:
        """Sets time when plant was last watered to current moment."""
        if datetime.datetime.now() < self.watered[-1]:
            raise ValueError(f"Last watering entry is in the future. ({self.watered[-1]})")
        self.watered.append(datetime.datetime.now())
        if len(self.watered) > self.max_log_size:
            del self.watered[0]
        self._water_score = None

    def get_water_score(self) -> int:
        """Calculates the water score based on time between watering sessions."""
        time_sum = datetime.timedelta()
        for i in range(len(self.watered) -1, 0 , -1):
            if self.watered[i] < self.watered[i - 1]:
                raise ValueError(f"Entry {i - 1} is before entry {i}. ({i-1}: {self.watered[i-1]}. {i}: {self.watered[i]})")
            time_sum += self.watered[i] - self.watered[i - 1]
        time_avg = time_sum / (len(self.watered) - 1)

        max_deviation = self.watering_frequency * 3

        if not self.watering_frequency - max_deviation <= time_avg <=  self.watering_frequency + max_deviation:
            return 0

        water_score = (-(time_avg.days - self.watering_frequency.days)**2 + max_deviation.days**2) / (max_deviation.days**2)

        return int(water_score * 100)

    def time_to_water_score(self) -> int:
        """Returns score based on time between now and last watering session"""
        time_diff = datetime.datetime.now() - self.watered[-1]
        max_deviation = self.watering_frequency * 3
        if time_diff < self.watering_frequency:
            return 100
        if time_diff > self.watering_frequency + max_deviation:
            return 0
        score = (-(time_diff.days - self.watering_frequency.days) ** 2 + max_deviation.days ** 2) / (max_deviation.days ** 2)
        return int(score * 100)

    def get_nutrition_score(self) -> int:
        time_sum = datetime.timedelta()
        for i in range(len(self.nutrition) - 1, 0, -1):
            if self.nutrition[i] < self.nutrition[i - 1]:
                raise ValueError(
                    f"Entry {i - 1} is before entry {i}. ({i - 1}: {self.nutrition[i - 1]}. {i}: {self.nutrition[i]})")
            time_sum += self.nutrition[i] - self.nutrition[i - 1]
        time_avg = time_sum / (len(self.nutrition) - 1)

        nutrition_frequency = datetime.timedelta(days=30)
        max_deviation = nutrition_frequency * 3

        if time_avg < nutrition_frequency:
            return 100
        if time_avg > nutrition_frequency + max_deviation:
            return 0

        nutrition_score = (-(time_avg.days - nutrition_frequency.days) ** 2 + max_deviation.days ** 2) / (
                    max_deviation.days ** 2)
        return int(nutrition_score * 100)

    def time_to_feed_score(self) -> int:
        time_diff = datetime.datetime.now() - self.nutrition[-1]
        nutrition_frequency = datetime.timedelta(days=30)
        max_deviation = nutrition_frequency * 3
        if time_diff < nutrition_frequency:
            return 100
        if time_diff > nutrition_frequency + max_deviation:
            return 0
        score = (-(time_diff.days - nutrition_frequency.days) ** 2 + max_deviation.days ** 2) / (
                    max_deviation.days ** 2)
        return int(score * 100)


    def get_sunlight_score(self) -> int:
        """returns score based on how close the current sunlight is to that which is preffered by the plant"""
        if self.spot:
            diff_to_preff = min([abs(self.spot.sunlight.value - preff.value) for preff in self.preff_sunlight])
            return int(100 - diff_to_preff*33.33)
        else:
            return 0


    def determine_health(self):
        if self.manual_health:
            return  self.health
        if self.health == Health.DEAD:
            return self.health
        time_to_water_score = self.time_to_water_score()
        time_to_feed_score = self.time_to_feed_score()
        health_score = 0.25 * self.water_score + 0.20 * time_to_water_score + 0.45 * self.sunlight_score + 0.05 * self.nutrition_score + 0.05 * time_to_feed_score
        return health_score

    @property
    def water_score(self) -> int:
        if len(self.watered) < 2:
            return 0
        if self._water_score is None:
            self._water_score = self.get_water_score()
        return self._water_score

    @water_score.setter
    def water_score(self, value: int | None) -> None:
        self._water_score = value

    @property
    def nutrition_score(self) -> int:
        if len(self.nutrition) < 2:
            return 0
        if self.nutrition_score is None:
            self._nutrition_score = self.get_nutrition_score()
        assert self._nutrition_score is not None
        return self._nutrition_score

    @nutrition_score.setter
    def nutrition_score(self, value: int | None) -> None:
        self._nutrition_score = value

    @property
    def preff_sunlight(self) -> list[Sunlight]:
        return self._preff_sunlight

    @preff_sunlight.setter
    def preff_sunlight(self, values: list[str | Sunlight]) -> None:
        res: list[Sunlight] = []
        for i in range(len(values)):
            match values[i]:
                case "full shade":
                    res.append(Sunlight.FULL_SHADE)
                case "part sun/part shade":
                    res.append(Sunlight.PART_SUN)
                case "part shade":
                    res.append(Sunlight.PART_SHADE)
                case "full sun":
                    res.append(Sunlight.FULL_SUN)
                case value if isinstance(value, Sunlight):
                    res.append(value)
                case value:
                    raise ValueError(f"Unexpected preff_sunlight value {value}")
        self._preff_sunlight: list[Sunlight] = res
        if self.spot:
            self.sunlight_score = self.get_sunlight_score()

    def __repr__(self) -> str:
        return (f"Plant({self.core_id}, {self.personal_id}, {self.core_name}, {self.icon_type}, "
                f"{self.watering_frequency}, {self.preff_sunlight})")

    def __str__(self) -> str:
        return f"{self.personal_id}: {self.core_name}"

