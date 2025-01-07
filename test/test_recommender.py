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
    rec_expect = [8480, 428, 6178, 6199, 6200, 6201, 6202, 6203, 6204, 6206, 6210, 4181, 4182,
                  4183, 6252, 6253, 8314, 6317, 6318, 8377, 2242, 8386, 2244, 2272, 2274, 2275,
                  2277, 8422, 2287, 6405, 2322, 2323, 8509, 8538, 8549, 6554, 2468, 2499, 8652,
                  4557, 4559, 2528, 2529, 2531, 8682, 8685, 2568, 8717, 8722, 543, 546, 551, 552,
                  8755, 8763, 8778, 8791, 625, 626, 627, 628, 4727, 710, 712, 713, 714, 715, 716,
                  717, 2774, 2775, 748, 2829, 2891, 4956, 861, 2915, 7030, 5007, 2962, 2976, 1001,
                  1024, 7169, 7170, 7172, 7173, 1036, 1038, 7187, 7188, 7189, 1023, 5203, 7265,
                  7266, 1130, 7276, 1133, 1150, 1195, 1196, 1198, 1199, 1200, 1201, 1202, 1203,
                  7352, 7354, 3259, 1208, 1210, 1211, 1212, 1213, 1214, 1215, 1216, 1217, 1222,
                  1218, 1219, 1221, 1224, 1225, 7384, 7410, 3353, 3355, 7463, 5443, 5445, 5462,
                  5465, 5466, 5467, 1416, 7571, 7572, 1457, 1469, 1470, 1471, 5564, 7639, 7640,
                  7681, 5726, 5736, 5737, 5741, 5806, 5808, 1716, 7864, 7866, 7873, 5836, 7890,
                  7902, 7903, 7904, 7905, 7907, 7908, 7911, 7914, 7915, 5868, 5871, 7919, 7920,
                  7921, 1820, 1822, 1846, 1847, 1848, 3972, 1971, 6068, 6069, 1993, 1999, 6205,
                  6208, 2288, 2294, 2295, 8494, 8603, 434, 2501, 8704, 8709, 711, 747, 4901,
                  4947, 856, 1031, 1147, 5269, 3236, 1194, 7353, 1220, 1272, 3347, 3349, 3352,
                  5449, 7569, 1468, 5739, 7858, 7901, 7906, 7910, 7913, 1821, 6071, 4122, 6207,
                  6311, 4280, 4304, 2279, 2290, 8487, 2354, 8512, 8543, 8550, 6535, 8596, 8613,
                  2498, 4554, 4558, 8653, 2533, 8677, 8680, 8683, 8699, 8700, 549, 8743, 8765,
                  718, 2773, 6913, 2885, 855, 2954, 2955, 2961, 2963, 7171, 3089, 3090, 5159,
                  7245, 1149, 5257, 5258, 1192, 1197, 1209, 1226, 3351, 3354, 5588, 7743, 5706,
                  5738, 5807, 5810, 5837, 7912, 5870, 3828, 7923, 5950, 3971, 2030, 3256, 6197,
                  2263, 8588, 8610, 8766, 8836, 2965, 3087, 5180, 5497, 5520, 5589, 3637, 1598,
                  8387, 8565, 2500, 2530, 2532, 721, 7163, 7164, 7165, 7166, 7167, 1025, 7168,
                  7174, 7176, 7186, 7345, 1223, 3350, 5740, 5869, 7918, 1845, 1891, 4349, 8601,
                  8622, 8625, 8681, 8691, 8794, 4722, 6809, 667, 6920, 2956, 2957, 2958, 2959,
                  7244, 7405, 7409, 5444, 5446, 5498, 1597, 1601, 1603, 7917, 1855, 8004, 1870,
                  1871, 1873, 3986, 3988, 8132, 2000]

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
    assert 710 not in rec_res
    assert 711 not in rec_res
    assert 712 not in rec_res
    assert 713 not in rec_res
    assert 714 not in rec_res
    assert 715 not in rec_res
    assert 716 not in rec_res
    assert 717 not in rec_res
    assert 718 not in rec_res
    assert 1999 not in rec_res
    assert 2272 not in rec_res
    assert 2274 not in rec_res
    assert 2468 not in rec_res
    assert 2773 not in rec_res
    assert 2774 not in rec_res
    assert 3347 not in rec_res
    assert 3349 not in rec_res
    assert 3350 not in rec_res
    assert 3351 not in rec_res
    assert 3352 not in rec_res
    assert 3353 not in rec_res
    assert 3354 not in rec_res
    assert 3355 not in rec_res
    assert 4557 not in rec_res
    assert 4947 not in rec_res
    assert 5203 not in rec_res
    assert 5868 not in rec_res
    assert 7245 not in rec_res
    assert 7345 not in rec_res
    assert 7463 not in rec_res
    assert 8485 not in rec_res
    assert 8487 not in rec_res
    assert 8565 not in rec_res
    assert 8596 not in rec_res
    assert 8603 not in rec_res
    assert 8755 not in rec_res
    assert 8763 not in rec_res
