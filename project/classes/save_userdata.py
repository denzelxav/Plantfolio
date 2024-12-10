import json
import os
from project.classes.userdata import UserData
from enum import Enum


class EnumEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.name
        return json.JSONEncoder.default(self, obj)


def save_user_data(user: UserData) -> None:
    """
    Saves the user data in json format to a file to access later
    """
    data = {"plant_data": [],
            "spots": []}
    
    for plant in user.plants:
        data["plant_data"].append(plant.get_data_to_save())

    for room in user.rooms.values():
        for spot in room:
            data["spots"].append(spot.get_spot_data())

    data["pet_preference"] = user.preferences.get("pet_toxicity", False)

    user_data_path = os.path.join("project", "user_data.json")
    with open(user_data_path, "w") as file:
        json.dump(data, file, cls=EnumEncoder, indent=4)

    