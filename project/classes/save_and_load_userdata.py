import json
import os
from typing import Any
from enum import Enum
from project.classes.userdata import UserData



class EnumEncoder(json.JSONEncoder):
    """
    Makes sure that enums are saved as strings correctly in the json file
    """
    def default(self, o):
        if isinstance(o, Enum):
            return o.name
        return json.JSONEncoder.default(self, o)


def save_user_data(user: UserData) -> None:
    """
    Saves the user data in json format to a file to access later
    """
    data: dict[str, Any] = {"plant_data": [],
                            "spots": [],
                            "pet_preference": False}

    for plant in sorted(user.plants, key=lambda x: x.core_id):
        data["plant_data"].append(plant.get_data_to_save())

    for room in user.rooms.values():
        for spot in room:
            data["spots"].append(spot.get_spot_data())

    data["pet_preference"] = user.pet_toxicity

    user_data_path = os.path.join("project", "user_data.json")
    with open(user_data_path, "w", encoding='utf-8') as file:
        json.dump(data, file, cls=EnumEncoder, indent=4)
