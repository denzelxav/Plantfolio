import datetime
from project.classes.recommender import Recommender
from project.classes.plant import Plant, plant_from_database
from project.classes.spot_notification import Spot
from project.classes.userdata import UserData
from project.classes.enums import Sunlight


def fake_log(interval: datetime.timedelta, max_log_size: int = 4) -> list[datetime.datetime]:
    """
    Creates a fake log for testing purposes
    """
    return [datetime.datetime.now() - interval * i for i in range(max_log_size, 0, -1)]

def apply_fake_logs(plant: Plant) -> None:
    """
    Sets fake logs for a plant
    """
    plant.watered = fake_log(plant.watering_frequency, plant.max_log_size)
    plant.nutrition = fake_log(datetime.timedelta(days=30), plant.max_log_size)

def create_userdata() -> UserData:
    """
    Creates a user data object for testing
    """
    ud = UserData()
    plant1 = plant_from_database(425)
    apply_fake_logs(plant1)
    plant2 = plant_from_database(426)
    apply_fake_logs(plant2)
    plant3 = plant_from_database(427)
    apply_fake_logs(plant3)
    plant4 = plant_from_database(502)
    apply_fake_logs(plant4)
    spot1 = Spot("1", Sunlight.FULL_SUN, "high", None, 20, "room")
    spot2 = Spot("2", Sunlight.FULL_SUN, "high", None, 20, "room")
    spot3 = Spot("3", Sunlight.FULL_SUN, "high", None, 20, "room")
    spot4 = Spot("4", Sunlight.FULL_SUN, "high", None, 20, "room")
    ud.add_room("room")
    for spot in [spot1, spot2, spot3, spot4]:
        ud.add_spot(spot)
    ud.add_plant(plant1, spot1)
    ud.add_plant(plant2, spot2)
    ud.add_plant(plant3, spot3)
    ud.add_plant(plant4, spot4)
    spot5 = Spot("5", Sunlight.PART_SHADE, "high", None, 20, "room")
    ud.add_spot(spot5)
    return ud

def create_userdata2() -> UserData:
    ud = UserData()
    plant1 = plant_from_database(626)
    apply_fake_logs(plant1)
    plant2 = plant_from_database(552)
    apply_fake_logs(plant2)
    plant3 = plant_from_database(710)
    apply_fake_logs(plant3)
    plant4 = plant_from_database(715)
    apply_fake_logs(plant4)
    spot1 = Spot("1", Sunlight.FULL_SUN, "high", None, 20, "room")
    spot2 = Spot("2", Sunlight.FULL_SUN, "high", None, 20, "room")
    spot3 = Spot("3", Sunlight.FULL_SUN, "high", None, 20, "room")
    spot4 = Spot("4", Sunlight.FULL_SUN, "high", None, 20, "room")
    ud.add_room("room")
    for spot in [spot1, spot2, spot3, spot4]:
        ud.add_spot(spot)
    ud.add_plant(plant1, spot1)
    ud.add_plant(plant2, spot2)
    ud.add_plant(plant3, spot3)
    ud.add_plant(plant4, spot4)
    spot5 = Spot("5", Sunlight.FULL_SUN, "high", None, 20, "room")
    ud.add_spot(spot5)
    return ud

def test_recommender():
    ud1 = create_userdata()
    recommender1 = Recommender(ud1)
    rec_res1 = recommender1.get_recommendations()
    print(rec_res1)
    rec_expect = [8480, 428, 6178, 6199, 6200, 6201, 6202, 6203, 6204, 6206, 6210, 4181, 4182, 4183,
                  6252, 6253, 8314, 6317, 6318, 8377, 2242, 8386, 2244, 2272, 2274]


    assert rec_res1 == rec_expect
    ud2 = create_userdata2()
    recommender2 = Recommender(ud2)
    rec_res2 = recommender2.get_recommendations()
    assert rec_res1 != rec_res2, "Different userdata gives same reccomendation"


def test_calculate_score():
    """
    Tests the calculate_score method of the recommender
    """
    recommender = Recommender(create_userdata())
    calculated_score = recommender.calculate_score(428)
    assert calculated_score == 83.16, "Gold dust score failed."
    calculated_score = recommender.calculate_score(715)
    assert calculated_score == 66.66, "Macrorizhos score failed"

def test_favorite():
    """
    Tests the favorite_score method of the recommender
    """
    recommender = Recommender(create_userdata())
    favorite_score = recommender.favorite_score("Abutilon")
    assert favorite_score == 100, "most common family failed favourite test"
    favorite_score = recommender.favorite_score("Achimenes")
    assert favorite_score == 33.33333333333333, "mid common family failed favourite test"
    recommender.favorites.add("Achimenes")
    favorite_score = recommender.favorite_score("Achimenes")
    assert favorite_score == 100, "Favorite system doesn't work :("
    favorite_score = recommender.favorite_score("test")
    assert favorite_score == 0, "Unknown family failed favourite test"

def test_water_score():
    """
    Tests the water_score method of the recommender
    """
    recommender = Recommender(create_userdata())
    water_score = recommender.water_score(datetime.timedelta(weeks=1))
    assert water_score == 99, "water score failed test"
    water_score = recommender.water_score(datetime.timedelta(days=1))
    assert water_score == 85.76686701437117, "water score failed test"
    water_score = recommender.water_score(datetime.timedelta(weeks=3))
    assert water_score == 12.793154452508958, "water score failed test"

def test_sunlight_score():
    """
    Tests the sunlight_score method of the recommender
    """
    recommender = Recommender(create_userdata())
    sunlight_score = recommender.sunlight_score(Sunlight.PART_SHADE)
    assert sunlight_score == 100
    sunlight_score = recommender.sunlight_score(Sunlight.FULL_SHADE)
    assert sunlight_score == 75
    sunlight_score = recommender.sunlight_score(Sunlight.FULL_SUN)
    assert sunlight_score == 50

def test_recommendation_with_pets():
    ud = create_userdata()
    ud.pet_toxicity = 1
    recommender = Recommender(ud)
    rec_res = recommender.get_recommendations()
    recommended_plants = [710, 711, 712, 713, 714, 715, 716, 717, 718, 1999, 2272,
                          2274, 2468, 2773, 2774, 3347, 3349, 3350, 3351, 3352, 3353,
                          3354, 3355, 4557, 4947, 5203, 5868, 7245, 7345, 7463, 8485,
                          8487, 8565, 8596, 8603, 8755, 8763]
    for plant_id in recommended_plants:
        assert plant_id not in rec_res
