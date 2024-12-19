from project.classes.plant import Plant
from project.classes.enums import Type_of_action, Sunlight
from project.classes.spot_notification import Notification
from project.classes.notifier import Notifier
import datetime

def create_plant1():
    """
    Create maple plant
    """
    return Plant(425, 1, "flowerus_mapelus", "flowering-maple",
                 "default", datetime.timedelta(days=3),
                 [Sunlight.FULL_SUN, Sunlight.PART_SHADE]
                 )

def create_plant2():
    """
    Create Sansevieria plant
    """
    return Plant(435, 2, "sansevieria", "sansevieria",
                 "default", datetime.timedelta(days=10),
                 [Sunlight.FULL_SUN, Sunlight.PART_SHADE]
                 )

def create_plant3():
    """
    Create Strelitzia plant
    """
    return Plant(498, 2, "strelitzia", "bird of paradise flower",
                 "default", datetime.timedelta(days=14),
                 [Sunlight.FULL_SHADE, Sunlight.PART_SHADE]
                 )

def create_notification_watering(plant, notifier):
    return Notification((datetime.datetime.now() - (plant.watered[-1] + plant.watering_frequency)).days + 1,
                        plant.watered[-1] + plant.watering_frequency,
                        datetime.datetime.now(),
                        plant.personal_id, Type_of_action.WATERING,
                        plant, notifier)

def create_notification_nutrition(plant, notifier):
    nutrition_frequency = datetime.timedelta(days=30)
    return Notification(((datetime.datetime.now() - (plant.nutrition[-1] + nutrition_frequency)).days + 1) / 2,
                 plant.nutrition[-1] + nutrition_frequency,
                 datetime.datetime.now(),
                 plant.personal_id, Type_of_action.NUTRITION,
                 plant, notifier)

def create_notification_repotting(plant, notifier):
    repotting_frequency = datetime.timedelta(days=365)
    return Notification(((datetime.datetime.now() - (plant.repotted + repotting_frequency)).days + 1) / 10,
                  plant.repotted + repotting_frequency,
                  datetime.datetime.now(),
                  plant.personal_id, Type_of_action.REPOTTING,
                  plant, notifier)

def test_intialize_notifier():
    maple = create_plant1()
    assert maple.list_notifications == [], "Plant object should be initialized with an empty list"
    notifier = Notifier([maple])
    assert notifier.check_tasks_today() is None, "There should be no task yet when you inialize a plant"
    assert maple.watered[-1] == datetime.datetime.now(), ("Last watering time should correspond "
                                                          "with creation date of the plant")
    assert maple.nutrition[-1] == datetime.datetime.now(), ("Last nutrition time should correspond "
                                                          "with creation date of the plant")
    assert maple.repotted == datetime.datetime.now(), ("Last repotting time should correspond "
                                                          "with creation date of the plant")

def test_watering_notification():
    sansevieria = create_plant2()
    sansevieria.watered = [datetime.datetime(2024, 11, 22, 12, 6)]
    notifier = Notifier([sansevieria])
    assert notifier.check_tasks_today() == [create_notification_watering(sansevieria, notifier)], "Notification was uncorrectly added to the list"
    assert sansevieria.list_notifications == [create_notification_watering(sansevieria, notifier)], "Notification was uncorrectly added to the list"
    assert notifier.all_notifications == [create_notification_watering(sansevieria, notifier)], "Notification was uncorrectly added to the list"

    sansevieria.water_plant()
    assert sansevieria.list_notifications == [], "The list should be empty after watering the plant"
    assert notifier.all_notifications == [], "The list should be empty after watering the plant"
    assert notifier.check_tasks_today() is None, "After watering the plant there should be no new Notifications"

def test_nutrition_notification():
    sansevieria = create_plant2()
    sansevieria.nutrition = [datetime.datetime(2024, 11, 15, 12, 6)]
    notifier = Notifier([sansevieria])
    assert notifier.check_tasks_today() == [create_notification_nutrition(sansevieria, notifier)], "Notification was uncorrectly added to the list"
    assert sansevieria.list_notifications == [create_notification_nutrition(sansevieria, notifier)], "Notification was uncorrectly added to the list"
    assert notifier.all_notifications == [create_notification_nutrition(sansevieria, notifier)], "Notification was uncorrectly added to the list"

    sansevieria.give_nutrition()
    assert sansevieria.list_notifications == [], "The list should be empty after feeding the plant"
    assert notifier.all_notifications == [], "The list should be empty after feeding the plant"
    assert notifier.check_tasks_today() is None, "After feeding the plant there should be no new Notifications"


def test_repot_notification():
    sansevieria = create_plant2()
    sansevieria.repotted = datetime.datetime(2023, 11, 15, 12, 6)
    notifier = Notifier([sansevieria])
    assert notifier.check_tasks_today() == [create_notification_repotting(sansevieria, notifier)], ("Notification was uncorrectly "
                                                                                                    "added to the list")
    assert sansevieria.list_notifications == [create_notification_repotting(sansevieria, notifier)], ("Notification was "
                                                                                                      "uncorrectly added to the list")
    assert notifier.all_notifications == [create_notification_repotting(sansevieria, notifier)], ("Notification was "
                                                                                                  "uncorrectly added to the list")

    sansevieria.repot_plant()
    assert sansevieria.list_notifications == [], "The list should be empty after repotting the plant"
    assert notifier.all_notifications == [], "The list should be empty after repotting the plant"
    assert notifier.check_tasks_today() is None, "After feeding the plant there should be no new Notifications"

def test_multiple_notifications_same_plant():
    strelitzia = create_plant3()
    strelitzia.watered = [datetime.datetime(2024, 11, 22, 12, 6)]
    strelitzia.nutrition = [datetime.datetime(2024, 11, 15, 12, 6)]
    strelitzia.repotted = datetime.datetime(2023, 11, 15, 12, 6)
    notifier = Notifier([strelitzia])
    assert len(notifier.check_tasks_today()) == 3, "there should be 3 notifications"
    assert notifier.check_tasks_today() == [create_notification_watering(strelitzia, notifier),
                                            create_notification_nutrition(strelitzia, notifier),
                                            create_notification_repotting(strelitzia, notifier)]
    assert strelitzia.list_notifications == [create_notification_watering(strelitzia, notifier),
                                            create_notification_nutrition(strelitzia, notifier),
                                            create_notification_repotting(strelitzia, notifier)]
    assert notifier.sort_by_weight() == [create_notification_watering(strelitzia, notifier),
                                         create_notification_repotting(strelitzia, notifier),
                                         create_notification_nutrition(strelitzia, notifier)]
    assert notifier.sort_by_date() == [create_notification_repotting(strelitzia, notifier),
                                       create_notification_watering(strelitzia, notifier),
                                       create_notification_nutrition(strelitzia, notifier)]
    assert notifier.sort_by_type() == [create_notification_watering(strelitzia, notifier),
                                        create_notification_nutrition(strelitzia, notifier),
                                        create_notification_repotting(strelitzia, notifier)]

def test_multiple_plants_same_task():
    maple = create_plant1()
    sansevieria = create_plant2()

    maple.watered = [datetime.datetime(2024, 11, 22)]
    sansevieria.watered = [datetime.datetime(2024, 11, 20)]

    notifier = Notifier([maple, sansevieria])

    assert len(notifier.check_tasks_today()) == 2, "There should be 2 notifications"
    assert maple.list_notifications == [create_notification_watering(maple, notifier)]
    assert sansevieria.list_notifications == [create_notification_watering(sansevieria, notifier)]

def test_no_notifications_when_up_to_date():
    maple = create_plant1()
    sansevieria = create_plant2()

    # Set the plants' last actions as recent enough to avoid triggering notifications
    maple.watered = [datetime.datetime(2024, 12, 18)]
    sansevieria.watered = [datetime.datetime(2024, 12, 14)]

    notifier = Notifier([maple, sansevieria])

    assert notifier.check_tasks_today() is None, "There should be no notifications when tasks are up to date"
    assert maple.list_notifications == [], "Maple should have no notifications"
    assert sansevieria.list_notifications == [], "Sansevieria should have no notifications"


def test_all_plants_all_notifications():
    # Create all three plants
    maple = create_plant1()
    sansevieria = create_plant2()
    strelitzia = create_plant3()

    # Set up their watering, nutrition, and repotting dates to make sure all notifications are generated
    maple.watered = [datetime.datetime(2024, 11, 20)]
    sansevieria.watered = [datetime.datetime(2024, 11, 15)]
    strelitzia.watered = [datetime.datetime(2024, 11, 18)]

    maple.nutrition = [datetime.datetime(2024, 10, 25)]
    sansevieria.nutrition = [datetime.datetime(2024, 11, 10)]
    strelitzia.nutrition = [datetime.datetime(2024, 11, 5)]

    maple.repotted = datetime.datetime(2023, 11, 15)
    sansevieria.repotted = datetime.datetime(2023, 11, 10)
    strelitzia.repotted = datetime.datetime(2023, 11, 1)

    # Create the notifier for all the plants
    notifier = Notifier([maple, sansevieria, strelitzia])

    # Check that the notifications list contains the expected notifications for all plants
    expected_notifications = [
        create_notification_watering(maple, notifier),
        create_notification_nutrition(maple, notifier),
        create_notification_repotting(maple, notifier),
        create_notification_watering(sansevieria, notifier),
        create_notification_nutrition(sansevieria, notifier),
        create_notification_repotting(sansevieria, notifier),
        create_notification_watering(strelitzia, notifier),
        create_notification_nutrition(strelitzia, notifier),
        create_notification_repotting(strelitzia, notifier)
    ]

    # Assert that the notifications are generated correctly
    assert notifier.check_tasks_today() == expected_notifications, "Notifications for all plants are not correct"

    # Assert that each plant has all its notifications in its own list
    assert maple.list_notifications == [create_notification_watering(maple, notifier),
                                        create_notification_nutrition(maple, notifier),
                                        create_notification_repotting(maple,
                                                                      notifier)], "Maple's notifications are incorrect"

    assert sansevieria.list_notifications == [create_notification_watering(sansevieria, notifier),
                                              create_notification_nutrition(sansevieria, notifier),
                                              create_notification_repotting(sansevieria,
                                                                            notifier)], "Sansevieria's notifications are incorrect"

    assert strelitzia.list_notifications == [create_notification_watering(strelitzia, notifier),
                                             create_notification_nutrition(strelitzia, notifier),
                                             create_notification_repotting(strelitzia,
                                                                           notifier)], "Strelitzia's notifications are incorrect"

    # Assert that all notifications are in the notifier's all_notifications list
    assert notifier.all_notifications == expected_notifications, "All notifications are not correctly added to the notifier"


















