import json
import os
import sys
from typing import Any
from enum import Enum
from project.classes.userdata import UserData
from project.classes.spot_notification import Spot
from project.classes.enums import Sunlight



class EnumEncoder(json.JSONEncoder):
    """
    Makes sure that enums are saved as strings correctly in the json file
    """
    def default(self, o):
        if isinstance(o, Enum):
            return o.name
        return json.JSONEncoder.default(self, o)


def save_user_data(user: UserData, test_mode: bool=False) -> None:
    """
    Saves the user data in json format to a file to access later
    """
    if test_mode:
        save_path = os.path.join("test", "test_user_data.json")
    elif getattr(sys, 'frozen', False):
        appdata = os.getenv('APPDATA')
        if appdata is None:
            raise FileNotFoundError("Appdata folder could not be found")
        directory = os.path.join(appdata, "Plantfolio")
        try:
            os.mkdir(directory)
        except FileExistsError:
            pass
        save_path = os.path.join(directory, "user_data.json")
    else:
        save_path = os.path.join("project", "user_data.json")

    data: dict[str, Any] = {"plant_data": [],
                            "rooms": {},
                            "pet_preference": False}

    for room_name, room in user.rooms.items():
        data["rooms"][room_name] = [spot.get_spot_data() for spot in room]

    for plant in sorted(user.plants, key=lambda x: x.personal_id):
        data["plant_data"].append(plant.get_data_to_save())

    data["pet_preference"] = user.pet_toxicity

    with open(save_path, "w", encoding='utf-8') as file:
        json.dump(data, file, cls=EnumEncoder, indent=4)

def load_user_data(test_mode: bool=False) -> UserData:
    """
    Loads the user data from the json file
    """
    if test_mode:
        load_path = os.path.join("test", "test_user_data.json")
    elif getattr(sys, 'frozen', False):
        appdata = os.getenv('APPDATA')
        if appdata is None:
            raise FileNotFoundError("Appdata folder could not be found")
        load_path = os.path.join(appdata, "Plantfolio", "user_data.json")
    else:
        load_path = os.path.join("project", "user_data.json")

    user = UserData()

    if not os.path.exists(load_path):
        return user

    with open(load_path, "r", encoding='utf-8') as file:
        data = json.load(file)

    if "rooms" in data:
        for room_name, room_data in data["rooms"].items():
            user.add_room(room_name)
            for spot_data in room_data:
                spot = Spot(
                    spot_data["spot_id"],
                    Sunlight[spot_data["light_level"]],
                    spot_data["humidity"],
                    None,
                    spot_data["temperature"],
                    spot_data["room"]
                    )

                user.add_spot(spot)

    for plant_data in data["plant_data"]:
        user.load_plant_data(plant_data)

    user.pet_toxicity = data["pet_preference"]

    return user
