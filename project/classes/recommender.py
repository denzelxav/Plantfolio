"""
This module contains the Recommender class that handles
the automatic recommendation of plants for the user.
"""


import datetime

from project.classes.public_methods import string_to_sunlight, string_to_water_frequency
from project.classes.userdata import UserData
from project.classes.plant import time_average
from project.query_function import query_from_database
from project.classes.enums import Sunlight



class Recommender:
    """
    This class handles the recommendations for a user.
    It keeps data on the users preferences like favorites
    and calculates scores for each plant to return a list of fitting plants.

    Attributes:
        userdata(UserData): The user database that the recommender uses for its calculations.
        favorites(set[str]): Favorite family names. Add manually with favorites.add("fam_name")
    """
    def __init__(self, userdata: UserData) -> None:
        self.favorites: set[str] = set()
        self.family_count: dict[str, int] = {}
        self.plant_scores: dict[int, float] = {}
        self.userdata = userdata
        self.set_values()



    def set_values(self) -> None:
        """Sets or refreshes all values needed for the recommender to work"""
        query = "SELECT plant_id FROM plant_details"
        query_res = query_from_database(query)
        self.all_ids: set[int] = {tup[0] for tup in query_res} # type: ignore
        all_pos_light = set()
        for _, spots in self.userdata.rooms.items():
            for spot in spots:
                if spot.assigned_plant is None:
                    all_pos_light.add(spot.light_level)

        self.sunlight = all_pos_light

        all_averages = []

        for plant in self.userdata.plants:
            avg_water_time = time_average(plant.watered)
            all_averages.append(avg_water_time)

        time_sum = datetime.timedelta()
        for deltatime in all_averages:
            time_sum += deltatime
        self.user_water_frequency = time_sum / max(1,len(all_averages))
        self.family_count ={}
        self.already_owned = set()
        for plant in self.userdata.plants:
            self.already_owned.add(plant.core_id)
            family_name = plant.scientific_name.split()[0]
            self.family_count[family_name] = self.family_count.get(family_name, 0) + 1
            # all_families.add(family_name)
        self.max_familiy_count = 1 if not self.family_count.values() \
                else max(self.family_count.values())

    def get_recommendations(self) -> list[int]:
        """
        Returns a list of plant_ids that are sorted on
        how good they fit the users needs in descending order
        """
        for plant_id in self.all_ids:
            self.plant_scores[plant_id] = self.calculate_score(plant_id)
        recommendations = sorted([plant for plant in self.all_ids if self.plant_scores[plant] > 50],
                                 key=lambda plant_id: self.plant_scores[plant_id], reverse=True)
        print(self.calculate_score(recommendations[0]), self.calculate_score(recommendations[-1]))
        return recommendations


    def calculate_score(self, plant_id: int) -> float:
        """Calculates the recommendation score for a given plant."""
        if plant_id in self.already_owned:
            return 0

        query = ("SELECT toxic_to_pets, sunlight_list, watering, scientific_name "
                "FROM plant_details "
                 f"WHERE plant_id = '{plant_id}'")
        query_res = query_from_database(query)
        plant_data = list(query_res[0])

        if isinstance(plant_data[0], int):
            pet_toxicity = plant_data[0]
        else:
            raise TypeError("pet_toxicity must be of type int. "
                            f"Got {type(plant_data[0])}. Value: {plant_data[0]}.")
        if isinstance(plant_data[1], str):
            sunlight_list = [string_to_sunlight(sunlight)
                     for sunlight in  plant_data[1].strip("[").strip("]")\
                         .replace('"',"").split(",")]
        else:
            raise TypeError("sunlight must be of type str. "
                            f"Got {type(plant_data[1])}. Value: {plant_data[1]}.")
        if isinstance(plant_data[2], str):
            watering_frequency = plant_data[2]
        else:
            raise TypeError("watering_frequency must be of type str. "
                f"Got {type(plant_data[2])}. Value: {plant_data[2]}.")
        if isinstance(plant_data[3], str):
            names = plant_data[3].split()
            family = names[0]
        else:
            raise TypeError("family must be of type str. "
                f"Got {type(plant_data[3])}. Value: {plant_data[3]}.")



        if self.userdata.pet_toxicity and pet_toxicity == 1:
            return 0


        sunlight_score = max(self.sunlight_score(sunlight) for sunlight in sunlight_list)
        water_score = self.water_score(string_to_water_frequency(watering_frequency))
        favorite_score = self.favorite_score(family)
        total_score = 0.33 * sunlight_score + 0.34 * water_score + 0.33 * favorite_score
        return total_score



    def sunlight_score(self, sunlight: Sunlight) -> int:
        """
        Returns a score between 0 and 100 for the plant based on
        the sunlight of the available spots
        """
        if len(self.sunlight) == 0:
            return 0
        best_score: int = min(abs(sunlight.value - available_light.value)
                             for available_light in self.sunlight)
        return 100 - best_score * 100 // 4

    def water_score(self, water_frequency: datetime.timedelta) -> int:
        """
        Returns a score between 0 and 100 for the plant based on
        the average watering frequency of the user.
        """
        water_diff = abs(water_frequency.days - self.user_water_frequency.days)**1.65
        water_score = 100 - water_diff
        if water_score < 0:
            return 0
        return water_score

    def favorite_score(self, family: str) -> float:
        """
        Returns a score between 0 and 100 for the plant based on if the family name is a favourite
        or on how many plants the user already has from that family.
        """
        if family in self.favorites:
            return 100
        return self.family_count.get(family, 0) / self.max_familiy_count * 100
