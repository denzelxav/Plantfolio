from project.classes.plant import Plant
from project.classes.enums import Sunlight, Health
from project.classes.spot_notification import Spot
import datetime

def create_plant(sunlight: Sunlight = Sunlight.FULL_SHADE):
    spot = Spot("spot", sunlight, "humid", None, 20)
    return Plant(425, 1, "flowering-maple",
                 "default", datetime.timedelta(days=7),
                 ["full sun", "part shade"]
                 ), spot

def test_sunlight():
    maple, dark_spot = create_plant()
    assert maple.sunlight_score == 0
    maple.change_spot(dark_spot)
    assert maple.sunlight_score == 66, "sunlight score was not calculated or calculated incorrectly"
    sunny_spot = Spot("spot", Sunlight.FULL_SUN, "humid", None, 20)
    maple.change_spot(sunny_spot)
    assert maple.sunlight_score == 100, "sunlight score cache was not updated"

def test_water():
    maple, spot = create_plant()
    maple.change_spot(spot)
    test_datetime = datetime.datetime(2002, 1, 24, 4, 20,)
    good_water_log = [test_datetime + datetime.timedelta(weeks=i) for i in range(maple.max_log_size)]
    maple.watered = good_water_log
    assert maple.water_score == 100, "water score was not calculated or calculated incorrectly"

    bad_water_log = [datetime.datetime.now() - datetime.timedelta(weeks=4*i) for i in range(maple.max_log_size - 1, 0 , -1)]
    maple.watered = bad_water_log
    maple.water_score = None
    assert maple.water_score == 0

    water_log = [datetime.datetime.now() - datetime.timedelta(weeks=(i + 5)) for i in range(maple.max_log_size, 0 , -1)]
    maple.watered = water_log
    maple.water_score = None
    assert len(maple.watered) == maple.max_log_size
    assert maple.water_score == 100
    maple.water_plant()
    assert len(maple.watered) == maple.max_log_size, "water log exceeded max log size"
    assert maple.water_score == 38, "water score cache wasn't updated or calculated incorrectly"
    assert maple.time_to_water_score() == 100
    water_log = [datetime.datetime.now() - datetime.timedelta(weeks=(i + 1)) for i in range(maple.max_log_size, 0, -1)]
    maple.watered = water_log
    assert maple.time_to_water_score() == 75, "Time to water score was calculated incorrectly"

def test_nutrition():
    maple, spot = create_plant()
    maple.change_spot(spot)
    nutri_log = [datetime.datetime.now() - datetime.timedelta(days=30*i) for i in range(maple.max_log_size, 0, -1)]
    maple.nutrition = nutri_log
    assert maple.nutrition_score == 100, "nutrition score was not calculated or calculated incorrectly"
    assert maple.time_to_feed_score() == 100, "time to feed score was calculated incorrectly"

    nutri_log = [datetime.datetime.now() - datetime.timedelta(days=30 * (i + 2)) for i in range(maple.max_log_size, 0, -1)]
    maple.nutrition = nutri_log
    maple.give_nutrition()
    assert maple.nutrition_score == 88, "nutrition score cache was not updated or calculated incorrectly"

def test_health():
    maple, _ = create_plant()
    spot = Spot("spot", Sunlight.FULL_SUN, "humid", None, 20)
    maple.change_spot(spot)
    nutri_log = [datetime.datetime.now() - datetime.timedelta(days=30 * i) for i in range(maple.max_log_size, 0, -1)]
    maple.nutrition = nutri_log
    water_log = [datetime.datetime.now() - datetime.timedelta(weeks=i) for i in range(maple.max_log_size, 0 , -1)]
    maple.watered = water_log
    maple.health = Health.UNHEALTHY
    assert maple.get_health_score() == 100, "health score was not calculated incorrectly"
    assert maple.health == Health.HEALTHY, "health was not set properly"
    maple.manual_health = True
    maple.health = Health.UNHEALTHY
    assert maple.health == Health.UNHEALTHY, "Manual health not working properly"
    maple.manual_health = False
    maple.health = Health.DEAD
    assert maple.health == Health.DEAD, "Dead status overwritten"



