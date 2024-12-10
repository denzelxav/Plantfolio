from project.classes.save_userdata import save_user_data
from project.classes.userdata import UserData
from project.classes.enums import Health, Sunlight
from project.classes.plant import Plant
from project.classes.spot_notification import Spot
import datetime
import json
import os


def create_plant1(sunlight: Sunlight = Sunlight.FULL_SHADE):
    return Plant(425, 1, "flowerus_mapelus", "flowering-maple",
                 "default", datetime.timedelta(days=7),
                 ["full sun", "part shade"]
                 )

def create_plant2(sunlight: Sunlight = Sunlight.FULL_SUN):
    return Plant(435, 2, "sansevieria", "sansevieria",
                 "default", datetime.timedelta(days=10),
                 ["full sun", "part shade"]
                 )

def create_plant3(sunlight: Sunlight = Sunlight.FULL_SHADE):
    return Plant(498, 2, "strelitzia", "bird of paradise flower",
                 "default", datetime.timedelta(days=14),
                 ["full shade", "part shade"]
                 )

def test_save_userdata_basic():
    test_user = UserData()

    test_plant1 = create_plant1()
    test_spot1 = Spot('Window', Sunlight.FULL_SHADE, 'high humidity', None, 21, 'bedroom')
    test_user.add_plant(test_plant1, test_spot1)

    assert (test_user.rooms == {'bedroom': [test_spot1]})
    assert (test_plant1 in test_user.plants)

    save_user_data(test_user)

    assert os.path.exists(os.path.join("project", "user_data.json"))

    saved_data_path = os.path.join("project", "user_data.json")
    with open(saved_data_path, "r") as file:
        data = json.load(file)
        assert data["plant_data"] == [test_plant1.get_data_to_save()]
        
def test_save_userdata_multiple_plants_one_room():
    test_user = UserData()
    test_user.preferences["pet_toxicity"] = True

    test_plant1 = create_plant1()
    test_plant2 = create_plant2()
    test_plant3 = create_plant3()

    test_spot1 = Spot('Window', Sunlight.FULL_SHADE, 'high humidity', None, 21, 'bedroom')
    test_spot2 = Spot('Cabinet', Sunlight.FULL_SUN, 'high humidity', None, 21, 'bedroom')
    test_spot3 = Spot('Shelf', Sunlight.FULL_SHADE, 'high humidity', None, 21, 'bedroom')

    test_user.add_plant(test_plant1, test_spot1)
    test_user.add_plant(test_plant2, test_spot2)
    test_user.add_plant(test_plant3, test_spot3)

    assert (test_user.rooms == {'bedroom': [test_spot1, test_spot2, test_spot3]})
    assert (test_plant1 in test_user.plants)
    assert (test_plant2 in test_user.plants)
    assert (test_plant3 in test_user.plants)

    save_user_data(test_user)

    assert os.path.exists(os.path.join("project", "user_data.json"))

    saved_data_path = os.path.join("project", "user_data.json")
    with open(saved_data_path, "r") as file:
        data = json.load(file)

    assert data["plant_data"] == [test_plant1.get_data_to_save(), test_plant2.get_data_to_save(), test_plant3.get_data_to_save()]
    assert data["spots"] == [test_spot1.get_spot_data(), test_spot2.get_spot_data(), test_spot3.get_spot_data()]
    assert data["pet_preference"] == True

        