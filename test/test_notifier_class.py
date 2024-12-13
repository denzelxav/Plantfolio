from project.classes.plant import Plant
from project.classes.enums import Type_of_action, Sunlight
from project.classes.spot_notification import Notification
from project.classes.notifier import Notifier
import datetime


def create_plant1(sunlight: Sunlight = Sunlight.FULL_SHADE):
    """
    Create maple plant
    """
    return Plant(425, 1, "flowerus_mapelus", "flowering-maple",
                 "default", datetime.timedelta(days=3),
                 ["full sun", "part shade"]
                 )

def create_plant2(sunlight: Sunlight = Sunlight.FULL_SUN):
    """
    Create Sansevieria plant
    """
    return Plant(435, 2, "sansevieria", "sansevieria",
                 "default", datetime.timedelta(days=10),
                 ["full sun", "part shade"]
                 )

def create_plant3(sunlight: Sunlight = Sunlight.FULL_SHADE):
    """
    Create Strelitzia plant
    """
    return Plant(498, 2, "strelitzia", "bird of paradise flower",
                 "default", datetime.timedelta(days=14),
                 ["full shade", "part shade"]
                 )



def create_notifications():
    """
    Create Notifications for testing the refresh/check task module
    """
    maple = create_plant1()
    sansevieria = create_plant2()
    strelitzia = create_plant3()

    # test datetimes
    last_watering_datetime = datetime.datetime(2024, 11, 22, 12, 6)
    last_nutrition_datetime = datetime.datetime(2024, 11, 2, 12, 6)
    time_last_repotted = datetime.datetime(2023, 9, 5, 12, 6)

    # creating logs for maple
    water_log_maple = [last_watering_datetime]
    nutri_log_maple = [last_nutrition_datetime]
    maple.watered = water_log_maple
    maple.nutrition = nutri_log_maple
    maple.repotted = time_last_repotted

    # creating logs for sansevieria
    water_log_sansevieria = [last_watering_datetime]
    nutri_log_sansevieria = [last_nutrition_datetime]
    sansevieria.watered = water_log_sansevieria
    sansevieria.nutrition = nutri_log_sansevieria
    sansevieria.repotted = time_last_repotted

    # creating logs for strelitzia
    water_log_strelitzia = [last_watering_datetime]
    nutri_log_strelitzia = [last_nutrition_datetime]
    strelitzia.watered = water_log_strelitzia
    strelitzia.nutrition = nutri_log_strelitzia
    strelitzia.repotted = time_last_repotted

    # weight is how many we are passed the original due date

    not1 = Notification((datetime.datetime.now() - (water_log_maple[-1] + maple.watering_frequency)).days + 1,
                        water_log_maple[-1] + maple.watering_frequency,
                        datetime.datetime.now(), maple.core_id, Type_of_action.WATERING,
                        maple)
    not2 = Notification((datetime.datetime.now() - (water_log_sansevieria[-1] + sansevieria.watering_frequency)).days + 1,
                        water_log_sansevieria[-1] + sansevieria.watering_frequency,
                        datetime.datetime.now(), sansevieria.core_id, Type_of_action.WATERING,
                        sansevieria)
    not3 = Notification((datetime.datetime.now() - (water_log_strelitzia[-1] + strelitzia.watering_frequency)).days + 1,
                        water_log_strelitzia[-1] + strelitzia.watering_frequency,
                        datetime.datetime.now(), strelitzia.core_id, Type_of_action.WATERING,
                        strelitzia)

    # nutrition notification
    not4 = Notification((datetime.datetime.now() - (nutri_log_maple[-1] + datetime.timedelta(days=30))).days + 1,
                        nutri_log_maple[-1] + datetime.timedelta(days=30),
                        datetime.datetime.now(), maple.core_id, Type_of_action.NUTRITION, maple)
    not5 = Notification((datetime.datetime.now() - (nutri_log_sansevieria[-1] + datetime.timedelta(days=30))).days + 1,
                        nutri_log_sansevieria[-1] + datetime.timedelta(days=30),
                        datetime.datetime.now(), sansevieria.core_id, Type_of_action.NUTRITION, sansevieria)
    not6 = Notification((datetime.datetime.now() - (nutri_log_strelitzia[-1] + datetime.timedelta(days=30))).days + 1,
                        nutri_log_strelitzia[-1] + datetime.timedelta(days=30),
                        datetime.datetime.now(), strelitzia.core_id, Type_of_action.NUTRITION, strelitzia)

    not7 = Notification((datetime.datetime.now() - (time_last_repotted + datetime.timedelta(days=365))).days + 1,
                        time_last_repotted + datetime.timedelta(days=365),
                        datetime.datetime.now(), maple.core_id, Type_of_action.REPOTTING,
                        maple)
    not8 = Notification((datetime.datetime.now() - (time_last_repotted + datetime.timedelta(days=365))).days + 1,
                        time_last_repotted + datetime.timedelta(days=365),
                        datetime.datetime.now(), sansevieria.core_id, Type_of_action.REPOTTING,
                        sansevieria)
    not9 = Notification((datetime.datetime.now() - (time_last_repotted + datetime.timedelta(days=365))).days + 1,
                        time_last_repotted + datetime.timedelta(days=365),
                        datetime.datetime.now(), strelitzia.core_id, Type_of_action.REPOTTING,
                        strelitzia)

    plants = [maple, sansevieria, strelitzia]
    notifier1 = Notifier(plants)
    notifications = notifier1.check_tasks_today()

    plants2 = [strelitzia, maple, sansevieria]
    notifier2 = Notifier(plants2)
    notifications2 = notifier2.check_tasks_today()

    # test if plants are available
    assert notifier2.plants == [strelitzia, maple, sansevieria], "Plants were not added correctly"

    return not1, not2, not3, not4, not5, not6, not7, not8, not9, notifications, notifications2, notifier1, notifier2

def test_notification_creation():
    (not1, not2, not3, not4, not5, not6, not7, not8, not9, _, _, _, _) = create_notifications()

    assert not1.weight > 0, "Notification weight should be greater than zero"
    assert not1.notification_type == Type_of_action.WATERING, "Notification type mismatch for maple"
    assert isinstance(not1.original_due_date, datetime.datetime), "Notification due_date should be a datetime object"

def test_notifier_edge_cases():
    notifier = Notifier([])
    assert notifier.check_tasks_today() == None, "Notifier should handle empty plant list"

    maple = create_plant1()
    notifier_with_one_plant = Notifier([maple])
    assert len(notifier_with_one_plant.plants) == 1, "Notifier did not correctly add a single plant"


def test_notifier():
    (not1, not2, not3, not4, not5, not6, not7, not8, not9, notifications,
     notifications2, notifier1, notifier2) = create_notifications()

    assert notifier1.plants[0].core_id == 425, "Maple was not added in the rigth way"
    assert notifier1.plants[1].core_id == 435, "Sansevieria was not added in the rigth way"
    assert notifier1.plants[2].core_id == 498, "Strelitzia was not added in the rigth way"
    assert notifier1.list_notifications is not None, ("list notifications should not be empty "
                                                      "before running check_task_today")

def test_notifications():
    (not1, not2, not3, not4, not5, not6, not7, not8, not9, notifications,
     notifications2, notifier1, notifier2) = create_notifications()


    assert notifications is not None, "There should be notifications for the tasks"
    assert len(notifications) == 9, f"Expected 6 notifications, got {len(notifications)}"
    assert notifications == [not1, not4, not7, not2, not5, not8, not3, not6, not9], ("Notifications should be stored in order"
                                                                   "of the plants in the list "
                                                                   "[maple, sansevieria, strelitzia]")
    assert notifications2 == [not3, not6, not9, not1, not4, not7, not2, not5, not8], ("Notificarions should be stored"
                                                                    "in order of a different order input list"
                                                                    "[strelitzia, maple, sansevieria]")

def test_remove_task():
    maple = create_plant1()
    sansevieria = create_plant2()
    strelitzia = create_plant3()
    (not1, not2, not3, not4, not5, not6, not7, not8, not9,
     notifications, notifications2, notifier1, notifier2) = create_notifications()

    # remove watering task for maple
    list_task_removed = maple.water_plant(notifications)

    # manually remove for the check
    check_notifications = [not4, not7, not2, not5, not8, not3, not6, not9]

    # assert list_task_removed == not1, "Watering task removed from maple"
    assert list_task_removed == check_notifications, "Watering task unsuccesfully removed for maple"

    list_second_task_removed = strelitzia.water_plant(notifications)
    check_notifications_2 = [not4, not7, not2, not5, not8, not6, not9]
    assert list_second_task_removed == check_notifications_2, ("Watering task unsuccesfully removed "
                                                               "for maple and strelitzia")

    list_third_task_removed = sansevieria.give_nutrition(notifications)
    check_notifications_3 = [not4, not7, not2, not8, not6, not9]
    assert list_third_task_removed == check_notifications_3, "Remove nutrition task from notifications"

    # remove repotting rask for maple
    list_repotted_removed = maple.repot_plant(notifications)
    check_notifications_3 = [not4, not2, not8, not6, not9]
    assert not7 not in list_repotted_removed, "Remove repotting task from notifications for maple"
    assert list_repotted_removed == check_notifications_3, "Remove repotting task from notifications for maple"

    feed_maple = maple.give_nutrition(notifications)
    assert not4 not in feed_maple, "Giving nutrition to maple failed"
    assert feed_maple == [not2, not8, not6, not9], "List without nutrition notification maple"

def test_empty_plant_list():
    """
    Test Notifier behavior when initialized with an empty plant list.
    """
    notifier = Notifier([])
    assert notifier.check_tasks_today() is None, "Notifier should return None when no plants are present"
    assert notifier.sort_by_weight() == [], "Sorting on empty notification list should return empty"
    assert notifier.sort_by_type() == [], "Sorting by type on empty notification list should return empty"
    assert notifier.sort_by_date() == [], "Sorting by date on empty notification list should return empty"


def test_no_notifications_due():
    """
    Test when plants do not require any tasks .
    """
    plant = Plant(425, 1, "flowerus_mapelus", "flowering-maple",
                 "default", datetime.timedelta(days=3),
                 ["full sun", "part shade"]
                 )
    plant.watered = [datetime.datetime.now()]
    plant.nutrition = [datetime.datetime.now()]
    plant.repotted = datetime.datetime.now()
    notifier = Notifier([plant])

    assert notifier.check_tasks_today() is None, "No notifications should be due if all tasks are up to date"
    assert len(notifier.list_notifications) == 0, "Notification list should remain empty"

def test_single_plant_multiple_notifications():
    """
    Test a single plant with multiple overdue tasks.
    """
    plant = Plant(425, 1, "flowerus_mapelus", "flowering-maple",
                 "default", datetime.timedelta(days=3),
                 ["full sun", "part shade"]
                 )
    plant.watered = [datetime.datetime.now() - datetime.timedelta(days=7)]
    plant.nutrition = [datetime.datetime.now() - datetime.timedelta(days=40)]
    plant.repotted = datetime.datetime.now() - datetime.timedelta(days=400)
    notifier = Notifier([plant])

    notifications = notifier.check_tasks_today()
    assert notifications is not None, "Notifications should be generated for overdue tasks"
    assert len(notifications) == 3, "Expected 3 notifications (watering, nutrition, repotting)"
    assert notifications[0].notification_type == Type_of_action.WATERING, "First notification should be for watering"
    assert notifications[1].notification_type == Type_of_action.NUTRITION, "Second notification should be for nutrition"
    assert notifications[2].notification_type == Type_of_action.REPOTTING, "Third notification should be for repotting"

def test_plant_with_no_recorded_tasks():
    """
    Test behavior when a plant has no watering, nutrition, or repotting history.
    """
    plant = Plant(435, 2, "sansevieria", "sansevieria",
                 "default", datetime.timedelta(days=10),
                 ["full sun", "part shade"]
                 )
    plant.watered = []
    plant.nutrition = []
    plant.repotted = None

    notifier = Notifier([plant])
    notifications = notifier.check_tasks_today()

    assert notifications is None, "No notifications should be generated if plant has no history"
    assert len(notifier.list_notifications) == 0, "Notification list should remain empty"


def test_sorting():
    (not1, not2, not3, not4, not5, not6, not7, not8, not9,
     notifications, notifications2, notifier1, notifier2) = create_notifications()
    sort_by_type = notifier1.sort_by_type()

    assert sort_by_type == [not1, not2, not3, not4, not5, not6, not7, not8, not9], "Unsuccesfully sorted notifications by type"

    sort_by_weight = notifier1.sort_by_weight()

    assert sort_by_weight == [not7, not8, not9, not1, not4, not2, not5, not6, not3], "Unsuccesfully sorted notifications by weight"
    #
    sort_by_date = notifier1.sort_by_date()

    assert sort_by_date == [not7, not8, not9, not1, not4, not2, not5, not6, not3], "Unsuccesfully sorted by date"


















