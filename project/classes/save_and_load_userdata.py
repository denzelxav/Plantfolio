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


def save_user_data(user: UserData, save_path: str) -> None:
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

    with open(save_path, "w", encoding='utf-8') as file:
        json.dump(data, file, cls=EnumEncoder, indent=4)

def load_user_data(load_path: str) -> UserData:
    """
    Loads the user data from the json file
    """
    user = UserData()

    if not os.path.exists(load_path):
        return user

    with open(load_path, "r", encoding='utf-8') as file:
        data = json.load(file)

    for spot_data in data["spots"]:
        user.load_spot_data(spot_data)

    for plant_data in data["plant_data"]:
        user.load_plant_data(plant_data)

    user.pet_toxicity = data["pet_preference"]

    return user
