import json
import os
from test.test_userdata_class import create_plant1, create_plant2, create_plant3
from project.classes.save_userdata import save_user_data
from project.classes.userdata import UserData
from project.classes.enums import Sunlight
from project.classes.spot_notification import Spot


def test_save_userdata_basic():
    """
    Tests saving user data with one plant and one room
    """
    test_user = UserData()

    test_plant1 = create_plant1()
    test_spot1 = Spot('Window', Sunlight.FULL_SHADE, 'high humidity', None, 21, 'bedroom')
    test_user.add_plant(test_plant1, test_spot1)

    assert test_user.rooms == {'bedroom': [test_spot1]}
    assert test_plant1 in test_user.plants

    save_user_data(test_user)

    assert os.path.exists(os.path.join("project", "user_data.json"))

    saved_data_path = os.path.join("project", "user_data.json")
    with open(saved_data_path, "r", encoding='utf-8') as file:
        data = json.load(file)
        assert data["plant_data"] == [test_plant1.get_data_to_save()]

def test_save_userdata_multiple_plants_one_room():
    """
    Tests saving user data with multiple plants in one room
    """
    test_user = UserData()
    test_user.pet_toxicity = True

    test_plant1 = create_plant1()
    test_plant2 = create_plant2()
    test_plant3 = create_plant3()

    test_spot1 = Spot('Window', Sunlight.FULL_SHADE, 'high humidity', None, 21, 'bedroom')
    test_spot2 = Spot('Cabinet', Sunlight.FULL_SUN, 'high humidity', None, 21, 'bedroom')
    test_spot3 = Spot('Shelf', Sunlight.FULL_SHADE, 'high humidity', None, 21, 'bedroom')

    test_user.add_plant(test_plant1, test_spot1)
    test_user.add_plant(test_plant2, test_spot2)
    test_user.add_plant(test_plant3, test_spot3)

    assert test_user.rooms == {'bedroom': [test_spot1, test_spot2, test_spot3]}
    assert test_plant1 in test_user.plants
    assert test_plant2 in test_user.plants
    assert test_plant3 in test_user.plants

    save_user_data(test_user)

    assert os.path.exists(os.path.join("project", "user_data.json"))

    saved_data_path = os.path.join("project", "user_data.json")
    with open(saved_data_path, "r", encoding='utf-8') as file:
        data = json.load(file)

    assert data["plant_data"] == [test_plant1.get_data_to_save(),
                                  test_plant2.get_data_to_save(),
                                  test_plant3.get_data_to_save()]
    assert data["spots"] == [   {
                                'spot_id': 'Window',
                                'light_level': 'FULL_SHADE',
                                'humidity': 'high humidity',
                                'temperature': 21,
                                'room': 'bedroom'
                                },
                                {
                                'spot_id': 'Cabinet',
                                'light_level': 'FULL_SUN',
                                'humidity': 'high humidity',
                                'temperature': 21,
                                'room': 'bedroom'
                                },
                                {
                                'spot_id': 'Shelf',
                                'light_level': 'FULL_SHADE',
                                'humidity': 'high humidity',
                                'temperature': 21,
                                'room': 'bedroom'
                                }]
    assert data["pet_preference"] is True


def test_save_userdata_mulitple_plants_multiple_rooms():
    """
    Tests saving user data with multiple plants in multiple rooms
    """
    test_user = UserData()
    test_user.pet_toxicity = True

    test_plant1 = create_plant1()
    test_plant2 = create_plant2()
    test_plant3 = create_plant3()

    test_spot1 = Spot('Window', Sunlight.FULL_SHADE, 'high humidity', None, 21, 'bedroom')
    test_spot2 = Spot('Cabinet', Sunlight.FULL_SUN, 'high humidity', None, 21, 'kitchen')
    test_spot3 = Spot('Shelf', Sunlight.FULL_SHADE, 'low humidity', None, 21, 'living room')

    test_user.add_plant(test_plant1, test_spot1)
    test_user.add_plant(test_plant2, test_spot2)
    test_user.add_plant(test_plant3, test_spot3)

    assert test_user.rooms == {'bedroom': [test_spot1],
                                'kitchen': [test_spot2],
                                'living room': [test_spot3]}
    assert test_plant1 in test_user.plants
    assert test_plant2 in test_user.plants
    assert test_plant3 in test_user.plants

    saved_data_path = os.path.join("project", "user_data.json")
    with open(saved_data_path, "r", encoding='utf-8') as file:
        data = json.load(file)

    assert data["plant_data"] == [test_plant1.get_data_to_save(),
                                  test_plant2.get_data_to_save(),
                                  test_plant3.get_data_to_save()]
    assert data["spots"] == [   {
                                'spot_id': 'Window',
                                'light_level': 'FULL_SHADE',
                                'humidity': 'high humidity',
                                'temperature': 21,
                                'room': 'bedroom'
                                },
                                {
                                'spot_id': 'Cabinet',
                                'light_level': 'FULL_SUN',
                                'humidity': 'high humidity',
                                'temperature': 21,
                                'room': 'bedroom'
                                },
                                {
                                'spot_id': 'Shelf',
                                'light_level': 'FULL_SHADE',
                                'humidity': 'high humidity',
                                'temperature': 21,
                                'room': 'bedroom'
                                }]
    assert data["pet_preference"] is True
