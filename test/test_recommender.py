from project.classes.recommender import *
from project.classes.plant import Plant, plant_from_database
from project.classes.spot_notification import Spot
from project.classes.userdata import UserData


def fake_log(interval: datetime.timedelta, max_log_size: int = 4) -> list[datetime.datetime]:
    return [datetime.datetime.now() - interval * i for i in range(max_log_size, 0, -1)]

def apply_fake_logs(plant: Plant) -> None:
    plant.watered = fake_log(plant.watering_frequency, plant.max_log_size)
    plant.nutrition = fake_log(datetime.timedelta(days=30), plant.max_log_size)

def create_userdata() -> UserData:
    ud = UserData()
    plant1 = plant_from_database(425)
    apply_fake_logs(plant1)
    plant2 = plant_from_database(426)
    apply_fake_logs(plant2)
    plant3 = plant_from_database(427)
    apply_fake_logs(plant3)
    plant4 = plant_from_database(502)
    apply_fake_logs(plant4)
    spot1 = Spot("1", Sunlight.FULL_SUN, "high", None, 20)
    spot2 = Spot("2", Sunlight.FULL_SUN, "high", None, 20)
    spot3 = Spot("3", Sunlight.FULL_SUN, "high", None, 20)
    spot4 = Spot("4", Sunlight.FULL_SUN, "high", None, 20)
    ud.add_room("room")
    for spot in [spot1, spot2, spot3, spot4]:
        ud.add_spot(spot, "room")
    ud.add_plant(plant1, spot1)
    ud.add_plant(plant2, spot2)
    ud.add_plant(plant3, spot3)
    ud.add_plant(plant4, spot4)
    spot5 = Spot("5", Sunlight.PART_SHADE, "high", None, 20)
    ud.add_spot(spot5, "room")
    return ud

def test_recommender():
    ud = create_userdata()
    recommender = Recommender(ud)
    rec_res = recommender.get_recommendations()
    print(rec_res)
    rec_expect = [1024, 1222, 2568, 1036, 1038, 2242, 2244, 543, 546, 551, 552, 1130, 1133, 625, 626, 627, 628, 1150,
                  1195, 1196, 1198, 1199, 1200, 1201, 1202, 1203, 1716, 1208, 1210, 1211, 1212, 1213, 1214, 1215, 1216,
                  1217, 1218, 1219, 1221, 710, 1224, 712, 713, 714, 715, 716, 717, 1225, 2774, 2775, 2272, 2274, 2275,
                  2277, 748, 2287, 2829, 2322, 2323, 1820, 1822, 1846, 1847, 1848, 2891, 861, 2915, 1416, 2962, 2976,
                  2468, 1457, 1971, 1469, 1470, 1471, 2499, 1993, 1999, 2528, 2529, 2531, 1001, 1023, 1031, 1147, 1194,
                  1220, 711, 747, 2288, 2294, 2295, 1272, 1821, 856, 434, 1468, 2501, 549, 1149, 1192, 1197, 1209, 718,
                  1226, 2773, 2290, 2354, 2885, 855, 2954, 2955, 2961, 2963, 2498, 2533, 2030, 1598, 2263, 2965, 1025,
                  1223, 721, 1845, 1891, 2500, 2530, 2532, 1597, 1601, 1603, 667, 1855, 1870, 1871, 1873, 2956, 2957,
                  2958, 2959, 428, 2000, 1864, 1868, 727, 2289, 540, 2193, 728, 425, 426, 427, 502]
    assert rec_res == rec_expect


def test_calculate_score():
    recommender = Recommender(create_userdata())
    calculated_score = recommender.calculate_score(428)
    assert calculated_score == 50.160000000000004, "Gold dust score failed."
    calculated_score = recommender.calculate_score(715)
    assert calculated_score == 66.66, "Macrorizhos score failed"

def test_favorite():
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
    recommender = Recommender(create_userdata())
    water_score = recommender.water_score(datetime.timedelta(weeks=1))
    assert water_score == 99, "water score failed test"
    water_score = recommender.water_score(datetime.timedelta(days=1))
    assert water_score == 85.76686701437117, "water score failed test"
    water_score = recommender.water_score(datetime.timedelta(weeks=3))
    assert water_score == 12.793154452508958, "water score failed test"

def test_sunlight_score():
    recommender = Recommender(create_userdata())
    sunlight_score = recommender.sunlight_score(Sunlight.PART_SHADE)
    assert sunlight_score == 100
    sunlight_score = recommender.sunlight_score(Sunlight.FULL_SHADE)
    assert sunlight_score == 75
    sunlight_score = recommender.sunlight_score(Sunlight.FULL_SUN)
    assert sunlight_score == 50