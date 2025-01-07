import json
import os
import datetime
from test.test_userdata_class import create_plant1, create_plant2, create_plant3
from project.classes.save_and_load_userdata import save_user_data, load_user_data
from project.classes.userdata import UserData
from project.classes.enums import Sunlight, Health
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

    save_user_data(test_user, test_mode=True)
    test_path = os.path.join("test", "test_user_data.json")

    assert os.path.exists(test_path)

    with open(test_path, "r", encoding='utf-8') as file:
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

    save_user_data(test_user, test_mode=True)
    test_path = os.path.join("test", "test_user_data.json")

    assert os.path.exists(test_path)

    with open(test_path, "r", encoding='utf-8') as file:
        data = json.load(file)

    assert data["plant_data"] == [test_plant1.get_data_to_save(),
                                  test_plant2.get_data_to_save(),
                                  test_plant3.get_data_to_save()]
    assert data["rooms"] == {'bedroom': [{
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
    }

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

    save_user_data(test_user, test_mode=True)
    test_path = os.path.join("test", "test_user_data.json")

    with open(test_path, "r", encoding='utf-8') as file:
        data = json.load(file)

    assert data["plant_data"] == [test_plant1.get_data_to_save(),
                                  test_plant2.get_data_to_save(),
                                  test_plant3.get_data_to_save()]
    assert data["rooms"] == {'bedroom': [{
                                        'spot_id': 'Window',
                                        'light_level': 'FULL_SHADE',
                                        'humidity': 'high humidity',
                                        'temperature': 21,
                                        'room': 'bedroom'
                                        }],
                            'kitchen': [{
                                        'spot_id': 'Cabinet',
                                        'light_level': 'FULL_SUN',
                                        'humidity': 'high humidity',
                                        'temperature': 21,
                                        'room': 'kitchen'
                                        }],
                            'living room': [{
                                        'spot_id': 'Shelf',
                                        'light_level': 'FULL_SHADE',
                                        'humidity': 'low humidity',
                                        'temperature': 21,
                                        'room': 'living room'
                                        }]
    }

    assert data["pet_preference"] is True

def test_load_data():
    """
    Tests loading user data
    """
    test_user = UserData()
    test_user.pet_toxicity = True

    test_plant1 = create_plant1()
    test_plant2 = create_plant2()
    test_plant3 = create_plant3()
    test_plant4 = create_plant1()
    test_plant4.personal_id = 4

    test_plant1.health = Health.DEAD
    test_plant2.manual_health = True
    test_plant3.notes = "This is a note"
    test_plant1.watered = [datetime.datetime.now()]
    test_plant2.nutrition = [datetime.datetime.now()]
    test_plant3.repotted = datetime.datetime.now()
    test_plant1.current_tasks = {"water", "repot"}

    test_spot1 = Spot('Window', Sunlight.FULL_SHADE, 'high humidity', None, 21, 'bedroom')
    test_spot2 = Spot('Cabinet', Sunlight.FULL_SUN, 'high humidity', None, 21, 'kitchen')
    test_spot3 = Spot('Shelf living room',
                      Sunlight.FULL_SHADE,
                      'low humidity',
                      None,
                      21,
                      'living room')
    test_spot4 = Spot('Shelf garage', Sunlight.FULL_SHADE, 'low humidity', None, 15, 'garage')

    test_user.add_plant(test_plant1, test_spot1)
    test_user.add_plant(test_plant2, test_spot2)
    test_user.add_plant(test_plant3, test_spot3)
    test_user.add_plant(test_plant4, test_spot4)

    assert test_plant1 in test_user.plants
    assert test_plant2 in test_user.plants
    assert test_plant3 in test_user.plants
    assert test_plant4 in test_user.plants

    save_user_data(test_user, test_mode=True)
    test_path = os.path.join("test", "test_user_data.json")
    loaded_data = load_user_data(test_mode=True)

    print('Testuser plants')
    for plant in test_user.plants:
        print(vars(plant))

    print('Loaded data plants')
    for plant in loaded_data.plants:
        print(vars(plant))

    assert test_plant1 in test_user.plants
    assert test_plant2 in test_user.plants
    assert test_plant3 in test_user.plants
    assert test_plant4 in test_user.plants

    assert test_plant1 in loaded_data.plants
    assert test_plant2 in loaded_data.plants
    assert test_plant3 in loaded_data.plants
    assert test_plant4 in loaded_data.plants

    loaded_data = load_user_data(test_path)

    assert loaded_data.rooms == test_user.rooms
    assert loaded_data.plants == test_user.plants
    assert loaded_data.pet_toxicity == test_user.pet_toxicity
    assert loaded_data == test_user

    plant_list = sorted(loaded_data.plants, key=lambda x: x.personal_id)
    assert plant_list == [test_plant1, test_plant2, test_plant3, test_plant4]
    assert plant_list[0].health == Health.DEAD
