from project.classes.plant import Plant
from project.classes.enums import Action, Sunlight
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
    weight_watering: float = (datetime.datetime.now() -
                              (plant.watered[-1] + plant.watering_frequency)).days + 1
    if weight_watering >=10:

        return Notification(f"{weight_watering} (urgent)",
                            plant.watered[-1] + plant.watering_frequency,
                            datetime.datetime.now(),
                            plant.personal_id, Action.WATERING,
                            plant, notifier)
    else:
        return Notification(f"{weight_watering}",
                            plant.watered[-1] + plant.watering_frequency,
                            datetime.datetime.now(),
                            plant.personal_id, Action.WATERING,
                            plant, notifier)

def create_notification_nutrition(plant, notifier):
    nutrition_frequency = datetime.timedelta(days=30)
    weight_nutrition: float = ((datetime.datetime.now() -
                                (plant.nutrition[-1] + nutrition_frequency)).days + 1) / 2
    if weight_nutrition >= 10:
        return Notification(f"{weight_nutrition} (urgent)",
                                    plant.nutrition[-1] + nutrition_frequency,
                                    datetime.datetime.now(),
                                    plant.personal_id,
                                    Action.NUTRITION,
                                    plant,
                                    notifier
                                    )
    else:
        return Notification(f"{weight_nutrition}",
                                    plant.nutrition[-1] + nutrition_frequency,
                                    datetime.datetime.now(),
                                    plant.personal_id,
                                    Action.NUTRITION,
                                    plant,
                                    notifier
                                    )
def create_notification_repotting(plant, notifier):
    repotting_frequency = datetime.timedelta(days=365)
    weight_repotting: float = ((datetime.datetime.now() -
                                (plant.repotted + repotting_frequency)).days + 1) / 10
    if weight_repotting >= 30:
        return Notification(f"{weight_repotting} (urgent)",
                                    plant.repotted + repotting_frequency,
                                    datetime.datetime.now(),
                                    plant.personal_id,
                                    Action.REPOTTING,
                                    plant,
                                    notifier
                                    )
    else:
        return Notification(f"{weight_repotting}",
                                    plant.repotted + repotting_frequency,
                                    datetime.datetime.now(),
                                    plant.personal_id,
                                    Action.REPOTTING,
                                    plant,
                                    notifier
                                    )

def test_intialize_notifier():
    margin = datetime.timedelta(seconds=5)
    maple = create_plant1()
    assert maple.list_notifications == [], "Plant object should be initialized with an empty list"
    notifier = Notifier([maple])
    assert notifier.check_tasks_today() is None, "There should be no task yet when you inialize a plant"
    assert datetime.datetime.now() - margin <= maple.watered[-1] <= datetime.datetime.now() + margin, \
        ("Last watering time should correspond "
        "with creation date of the plant")
    assert datetime.datetime.now() - margin <= maple.nutrition[-1] <= datetime.datetime.now() + margin,\
        ("Last nutrition time should correspond "
                                                          "with creation date of the plant")
    assert datetime.datetime.now() - margin <= maple.repotted <= datetime.datetime.now() + margin, \
        ("Last repotting time should correspond "
        "with creation date of the plant")

def test_watering_notification():
    # Define the margin for comparisons
    margin = datetime.timedelta(seconds=5)
    now = datetime.datetime.now()

    # Create the plant and notifier
    sansevieria = create_plant2()
    sansevieria.watered = [now - datetime.timedelta(days=30)]
    notifier = Notifier([sansevieria])

    # Expected notification
    expected_notification = create_notification_watering(sansevieria, notifier)

    # Check tasks today
    tasks_today = notifier.check_tasks_today()
    assert tasks_today is not None, "No notifications were generated"
    assert len(tasks_today) == 1, "There should be exactly one notification"
    notification = tasks_today[0]

    # Validate the notification's attributes
    assert notification.notification_type == expected_notification.notification_type, \
        "Notification type mismatch"
    assert notification.plant_notification == expected_notification.plant_notification, \
        "Plant mismatch in notification"
    assert notification.weight == expected_notification.weight, \
        "Notification weight mismatch"
    assert notification.personal_id_plant == expected_notification.personal_id_plant, \
        "Plant personal ID mismatch in notification"
    assert notification.original_due_date == expected_notification.original_due_date, \
        "Original due date mismatch in notification"
    assert now - margin <= notification.time_sent <= now + margin, \
        "Notification time_sent is outside the allowed margin"

    # Validate Sansevieria's list_notifications
    assert len(sansevieria.list_notifications) == 1, "Sansevieria should have exactly one notification"
    list_notification = sansevieria.list_notifications[0]

    assert list_notification.notification_type == expected_notification.notification_type, \
        "Notification type mismatch in Sansevieria's list"
    assert list_notification.plant_notification == expected_notification.plant_notification, \
        "Plant mismatch in Sansevieria's list"
    assert list_notification.weight == expected_notification.weight, \
        "Notification weight mismatch in Sansevieria's list"
    assert list_notification.personal_id_plant == expected_notification.personal_id_plant, \
        "Plant personal ID mismatch in Sansevieria's list"
    assert list_notification.original_due_date == expected_notification.original_due_date, \
        "Original due date mismatch in Sansevieria's list"
    assert now - margin <= list_notification.time_sent <= now + margin, \
        "Notification time_sent is outside the allowed margin in Sansevieria's list"

    # Validate notifier's all_notifications
    assert len(notifier.all_notifications) == 1, "Notifier should have exactly one notification"
    all_notification = notifier.all_notifications[0]

    assert all_notification.notification_type == expected_notification.notification_type, \
        "Notification type mismatch in notifier's all_notifications"
    assert all_notification.plant_notification == expected_notification.plant_notification, \
        "Plant mismatch in notifier's all_notifications"
    assert all_notification.weight == expected_notification.weight, \
        "Notification weight mismatch in notifier's all_notifications"
    assert all_notification.personal_id_plant == expected_notification.personal_id_plant, \
        "Plant personal ID mismatch in notifier's all_notifications"
    assert all_notification.original_due_date == expected_notification.original_due_date, \
        "Original due date mismatch in notifier's all_notifications"
    assert now - margin <= all_notification.time_sent <= now + margin, \
        "Notification time_sent is outside the allowed margin in notifier's all_notifications"

    # Water the plant and validate empty lists
    sansevieria.water_plant()
    assert sansevieria.list_notifications == [], "The list should be empty after watering the plant"
    assert notifier.all_notifications == [], "The notifier's notifications list should be empty after watering the plant"
    assert notifier.check_tasks_today() is None, "After watering the plant there should be no new notifications"

def test_nutrition_notification():
    # Define the margin for comparisons
    margin = datetime.timedelta(seconds=5)
    now = datetime.datetime.now()

    # Create the plant and notifier
    sansevieria = create_plant2()
    sansevieria.nutrition = [now - datetime.timedelta(days=47)]
    notifier = Notifier([sansevieria])

    # Expected notification
    expected_notification = create_notification_nutrition(sansevieria, notifier)

    # Check tasks today
    tasks_today = notifier.check_tasks_today()
    assert tasks_today is not None, "No notifications were generated"
    assert len(tasks_today) == 1, "There should be exactly one notification"
    notification = tasks_today[0]

    # Validate the notification's attributes
    assert notification.notification_type == expected_notification.notification_type, \
        "Notification type mismatch"
    assert notification.plant_notification == expected_notification.plant_notification, \
        "Plant mismatch in notification"
    assert notification.weight == expected_notification.weight, \
        "Notification weight mismatch"
    assert notification.personal_id_plant == expected_notification.personal_id_plant, \
        "Plant personal ID mismatch in notification"
    assert notification.original_due_date == expected_notification.original_due_date, \
        "Original due date mismatch in notification"
    assert now - margin <= notification.time_sent <= now + margin, \
        "Notification time_sent is outside the allowed margin"

    # Validate Sansevieria's list_notifications
    assert len(sansevieria.list_notifications) == 1, "Sansevieria should have exactly one notification"
    list_notification = sansevieria.list_notifications[0]

    assert list_notification.notification_type == expected_notification.notification_type, \
        "Notification type mismatch in Sansevieria's list"
    assert list_notification.plant_notification == expected_notification.plant_notification, \
        "Plant mismatch in Sansevieria's list"
    assert list_notification.weight == expected_notification.weight, \
        "Notification weight mismatch in Sansevieria's list"
    assert list_notification.personal_id_plant == expected_notification.personal_id_plant, \
        "Plant personal ID mismatch in Sansevieria's list"
    assert list_notification.original_due_date == expected_notification.original_due_date, \
        "Original due date mismatch in Sansevieria's list"
    assert now - margin <= list_notification.time_sent <= now + margin, \
        "Notification time_sent is outside the allowed margin in Sansevieria's list"

    # Validate notifier's all_notifications
    assert len(notifier.all_notifications) == 1, "Notifier should have exactly one notification"
    all_notification = notifier.all_notifications[0]

    assert all_notification.notification_type == expected_notification.notification_type, \
        "Notification type mismatch in notifier's all_notifications"
    assert all_notification.plant_notification == expected_notification.plant_notification, \
        "Plant mismatch in notifier's all_notifications"
    assert all_notification.weight == expected_notification.weight, \
        "Notification weight mismatch in notifier's all_notifications"
    assert all_notification.personal_id_plant == expected_notification.personal_id_plant, \
        "Plant personal ID mismatch in notifier's all_notifications"
    assert all_notification.original_due_date == expected_notification.original_due_date, \
        "Original due date mismatch in notifier's all_notifications"
    assert now - margin <= all_notification.time_sent <= now + margin, \
        "Notification time_sent is outside the allowed margin in notifier's all_notifications"

    # Feed the plant and validate empty lists
    sansevieria.give_nutrition()
    assert sansevieria.list_notifications == [], "The list should be empty after feeding the plant"
    assert notifier.all_notifications == [], "The notifier's notifications list should be empty after feeding the plant"
    assert notifier.check_tasks_today() is None, "After feeding the plant there should be no new notifications"


# def test_repot_notification():
#     sansevieria = create_plant2()
#     sansevieria.repotted = datetime.datetime(2023, 11, 15, 12, 6)
#     notifier = Notifier([sansevieria])
#     assert notifier.check_tasks_today() == [create_notification_repotting(sansevieria, notifier)], ("Notification was uncorrectly "
#                                                                                                     "added to the list")
#     assert sansevieria.list_notifications == [create_notification_repotting(sansevieria, notifier)], ("Notification was "
#                                                                                                       "uncorrectly added to the list")
#     assert notifier.all_notifications == [create_notification_repotting(sansevieria, notifier)], ("Notification was "
#                                                                                                   "uncorrectly added to the list")
#
#     sansevieria.repot_plant()
#     assert sansevieria.list_notifications == [], "The list should be empty after repotting the plant"
#     assert notifier.all_notifications == [], "The list should be empty after repotting the plant"
#     assert notifier.check_tasks_today() is None, "After feeding the plant there should be no new Notifications"

def test_repot_notification():
    # Define the margin for comparisons
    margin = datetime.timedelta(seconds=5)
    now = datetime.datetime.now()

    # Create the plant and notifier
    sansevieria = create_plant2()
    sansevieria.repotted = now - datetime.timedelta(days=402)
    notifier = Notifier([sansevieria])

    # Expected notification
    expected_notification = create_notification_repotting(sansevieria, notifier)

    # Check tasks today
    tasks_today = notifier.check_tasks_today()
    assert tasks_today is not None, "No notifications were generated"
    assert len(tasks_today) == 1, "There should be exactly one notification"
    notification = tasks_today[0]

    # Validate the notification's attributes
    assert notification.notification_type == expected_notification.notification_type, \
        "Notification type mismatch"
    assert notification.plant_notification == expected_notification.plant_notification, \
        "Plant mismatch in notification"
    assert notification.weight == expected_notification.weight, \
        "Notification weight mismatch"
    assert notification.personal_id_plant == expected_notification.personal_id_plant, \
        "Plant personal ID mismatch in notification"
    assert notification.original_due_date == expected_notification.original_due_date, \
        "Original due date mismatch in notification"
    assert now - margin <= notification.time_sent <= now + margin, \
        "Notification time_sent is outside the allowed margin"

    # Validate Sansevieria's list_notifications
    assert len(sansevieria.list_notifications) == 1, "Sansevieria should have exactly one notification"
    list_notification = sansevieria.list_notifications[0]

    assert list_notification.notification_type == expected_notification.notification_type, \
        "Notification type mismatch in Sansevieria's list"
    assert list_notification.plant_notification == expected_notification.plant_notification, \
        "Plant mismatch in Sansevieria's list"
    assert list_notification.weight == expected_notification.weight, \
        "Notification weight mismatch in Sansevieria's list"
    assert list_notification.personal_id_plant == expected_notification.personal_id_plant, \
        "Plant personal ID mismatch in Sansevieria's list"
    assert list_notification.original_due_date == expected_notification.original_due_date, \
        "Original due date mismatch in Sansevieria's list"
    assert now - margin <= list_notification.time_sent <= now + margin, \
        "Notification time_sent is outside the allowed margin in Sansevieria's list"

    # Validate notifier's all_notifications
    assert len(notifier.all_notifications) == 1, "Notifier should have exactly one notification"
    all_notification = notifier.all_notifications[0]

    assert all_notification.notification_type == expected_notification.notification_type, \
        "Notification type mismatch in notifier's all_notifications"
    assert all_notification.plant_notification == expected_notification.plant_notification, \
        "Plant mismatch in notifier's all_notifications"
    assert all_notification.weight == expected_notification.weight, \
        "Notification weight mismatch in notifier's all_notifications"
    assert all_notification.personal_id_plant == expected_notification.personal_id_plant, \
        "Plant personal ID mismatch in notifier's all_notifications"
    assert all_notification.original_due_date == expected_notification.original_due_date, \
        "Original due date mismatch in notifier's all_notifications"
    assert now - margin <= all_notification.time_sent <= now + margin, \
        "Notification time_sent is outside the allowed margin in notifier's all_notifications"

    # Repot the plant and validate empty lists
    sansevieria.repot_plant()
    assert sansevieria.list_notifications == [], "The list should be empty after repotting the plant"
    assert notifier.all_notifications == [], "The notifier's notifications list should be empty after repotting the plant"
    assert notifier.check_tasks_today() is None, "After repotting the plant there should be no new notifications"

# def test_multiple_plants_same_task():
#     maple = create_plant1()
#     sansevieria = create_plant2()
#
#     maple.watered = [datetime.datetime(2024, 11, 22)]
#     sansevieria.watered = [datetime.datetime(2024, 11, 20)]
#
#     notifier = Notifier([maple, sansevieria])
#
#     assert len(notifier.check_tasks_today()) == 2, "There should be 2 notifications"
#     assert maple.list_notifications == [create_notification_watering(maple, notifier)]
#     assert sansevieria.list_notifications == [create_notification_watering(sansevieria, notifier)]

def test_multiple_plants_same_task():
    # Define the margin for comparisons
    margin = datetime.timedelta(seconds=5)
    now = datetime.datetime.now()

    # Create the plants and set their watering times
    maple = create_plant1()
    sansevieria = create_plant2()

    maple.watered = [now - datetime.timedelta(days=30)]
    sansevieria.watered = [now - datetime.timedelta(days=32)]

    # Create the notifier
    notifier = Notifier([maple, sansevieria])

    # Expected notifications
    expected_notification_maple = create_notification_watering(maple, notifier)
    expected_notification_sansevieria = create_notification_watering(sansevieria, notifier)

    # Check tasks today
    tasks_today = notifier.check_tasks_today()
    assert tasks_today is not None, "No notifications were generated"
    assert len(tasks_today) == 2, "There should be exactly two notifications"

    # Check notification for Maple
    notification_maple = tasks_today[0]
    assert notification_maple.notification_type == expected_notification_maple.notification_type, \
        "Notification type mismatch for Maple"
    assert notification_maple.plant_notification == expected_notification_maple.plant_notification, \
        "Plant mismatch for Maple"
    assert notification_maple.weight == expected_notification_maple.weight, \
        "Notification weight mismatch for Maple"
    assert notification_maple.personal_id_plant == expected_notification_maple.personal_id_plant, \
        "Plant personal ID mismatch for Maple"
    assert notification_maple.original_due_date == expected_notification_maple.original_due_date, \
        "Original due date mismatch for Maple"
    assert now - margin <= notification_maple.time_sent <= now + margin, \
        "Notification time_sent is outside the allowed margin for Maple"

    # Check notification for Sansevieria
    notification_sansevieria = tasks_today[1]
    assert notification_sansevieria.notification_type == expected_notification_sansevieria.notification_type, \
        "Notification type mismatch for Sansevieria"
    assert notification_sansevieria.plant_notification == expected_notification_sansevieria.plant_notification, \
        "Plant mismatch for Sansevieria"
    assert notification_sansevieria.weight == expected_notification_sansevieria.weight, \
        "Notification weight mismatch for Sansevieria"
    assert notification_sansevieria.personal_id_plant == expected_notification_sansevieria.personal_id_plant, \
        "Plant personal ID mismatch for Sansevieria"
    assert notification_sansevieria.original_due_date == expected_notification_sansevieria.original_due_date, \
        "Original due date mismatch for Sansevieria"
    assert now - margin <= notification_sansevieria.time_sent <= now + margin, \
        "Notification time_sent is outside the allowed margin for Sansevieria"

    # Validate the list_notifications for each plant
    assert len(maple.list_notifications) == 1, "Maple should have exactly one notification"
    list_notification_maple = maple.list_notifications[0]
    assert list_notification_maple.notification_type == expected_notification_maple.notification_type, \
        "Notification type mismatch in Maple's list"
    assert list_notification_maple.plant_notification == expected_notification_maple.plant_notification, \
        "Plant mismatch in Maple's list"
    assert list_notification_maple.weight == expected_notification_maple.weight, \
        "Notification weight mismatch in Maple's list"
    assert list_notification_maple.personal_id_plant == expected_notification_maple.personal_id_plant, \
        "Plant personal ID mismatch in Maple's list"
    assert list_notification_maple.original_due_date == expected_notification_maple.original_due_date, \
        "Original due date mismatch in Maple's list"
    assert now - margin <= list_notification_maple.time_sent <= now + margin, \
        "Notification time_sent is outside the allowed margin in Maple's list"

    assert len(sansevieria.list_notifications) == 1, "Sansevieria should have exactly one notification"
    list_notification_sansevieria = sansevieria.list_notifications[0]
    assert list_notification_sansevieria.notification_type == expected_notification_sansevieria.notification_type, \
        "Notification type mismatch in Sansevieria's list"
    assert list_notification_sansevieria.plant_notification == expected_notification_sansevieria.plant_notification, \
        "Plant mismatch in Sansevieria's list"
    assert list_notification_sansevieria.weight == expected_notification_sansevieria.weight, \
        "Notification weight mismatch in Sansevieria's list"
    assert list_notification_sansevieria.personal_id_plant == expected_notification_sansevieria.personal_id_plant, \
        "Plant personal ID mismatch in Sansevieria's list"
    assert list_notification_sansevieria.original_due_date == expected_notification_sansevieria.original_due_date, \
        "Original due date mismatch in Sansevieria's list"
    assert now - margin <= list_notification_sansevieria.time_sent <= now + margin, \
        "Notification time_sent is outside the allowed margin in Sansevieria's list"

    # Validate the all_notifications list in the notifier
    assert len(notifier.all_notifications) == 2, "Notifier should have exactly two notifications"
    all_notification_maple = notifier.all_notifications[0]
    all_notification_sansevieria = notifier.all_notifications[1]

    assert all_notification_maple.notification_type == expected_notification_maple.notification_type, \
        "Notification type mismatch in notifier's all_notifications (Maple)"
    assert all_notification_maple.plant_notification == expected_notification_maple.plant_notification, \
        "Plant mismatch in notifier's all_notifications (Maple)"
    assert all_notification_maple.weight == expected_notification_maple.weight, \
        "Notification weight mismatch in notifier's all_notifications (Maple)"
    assert all_notification_maple.personal_id_plant == expected_notification_maple.personal_id_plant, \
        "Plant personal ID mismatch in notifier's all_notifications (Maple)"
    assert all_notification_maple.original_due_date == expected_notification_maple.original_due_date, \
        "Original due date mismatch in notifier's all_notifications (Maple)"
    assert now - margin <= all_notification_maple.time_sent <= now + margin, \
        "Notification time_sent is outside the allowed margin in notifier's all_notifications (Maple)"

    assert all_notification_sansevieria.notification_type == expected_notification_sansevieria.notification_type, \
        "Notification type mismatch in notifier's all_notifications (Sansevieria)"
    assert all_notification_sansevieria.plant_notification == expected_notification_sansevieria.plant_notification, \
        "Plant mismatch in notifier's all_notifications (Sansevieria)"
    assert all_notification_sansevieria.weight == expected_notification_sansevieria.weight, \
        "Notification weight mismatch in notifier's all_notifications (Sansevieria)"
    assert all_notification_sansevieria.personal_id_plant == expected_notification_sansevieria.personal_id_plant, \
        "Plant personal ID mismatch in notifier's all_notifications (Sansevieria)"
    assert all_notification_sansevieria.original_due_date == expected_notification_sansevieria.original_due_date, \
        "Original due date mismatch in notifier's all_notifications (Sansevieria)"
    assert now - margin <= all_notification_sansevieria.time_sent <= now + margin, \
        "Notification time_sent is outside the allowed margin in notifier's all_notifications (Sansevieria)"


def test_no_notifications_when_up_to_date():
    maple = create_plant1()
    sansevieria = create_plant2()

    # Set the plants' last actions as recent enough to avoid triggering notifications
    maple.watered = [datetime.datetime.now() - datetime.timedelta(days=1)]
    sansevieria.watered = [datetime.datetime.now() - datetime.timedelta(days=4)]

    notifier = Notifier([maple, sansevieria])

    assert notifier.check_tasks_today() is None, "There should be no notifications when tasks are up to date"
    assert maple.list_notifications == [], "Maple should have no notifications"
    assert sansevieria.list_notifications == [], "Sansevieria should have no notifications"


def test_all_plants_all_notifications():
    # Define the margin for comparisons
    margin = datetime.timedelta(seconds=5)

    # Capture the current time once for consistent assertions
    now = datetime.datetime.now()

    # Create all three plants
    maple = create_plant1()
    sansevieria = create_plant2()
    strelitzia = create_plant3()


    # Set up their watering, nutrition, and repotting dates to make sure all notifications are generated
    maple.watered = [now - datetime.timedelta(days=31)]
    sansevieria.watered = [now - datetime.timedelta(days=36)]
    strelitzia.watered = [now - datetime.timedelta(days=33)]

    maple.nutrition = [now - datetime.timedelta(days=57)]
    sansevieria.nutrition = [now - datetime.timedelta(days=42)]
    strelitzia.nutrition = [now - datetime.timedelta(days=46)]

    maple.repotted = now - datetime.timedelta(days=400)
    sansevieria.repotted = now - datetime.timedelta(days=405)
    strelitzia.repotted = now - datetime.timedelta(days=414)

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

    # # Assert that the notifications are generated correctly
    # assert notifier.check_tasks_today() == expected_notifications, "Notifications for all plants are not correct"

    # Validate each notification
    for notification, expected in zip(notifier.check_tasks_today(), expected_notifications):
        assert notification.notification_type == expected.notification_type, "Notification type mismatch"
        assert notification.plant_notification == expected.plant_notification, "Notification plant mismatch"
        assert now - margin <= notification.time_sent <= now + margin, "Notification time_sent is outside the margin"

    # Assert that each plant has all its notifications in its own list
    for notification, expected in zip(maple.list_notifications, [
        create_notification_watering(maple, notifier),
        create_notification_nutrition(maple, notifier),
        create_notification_repotting(maple, notifier)
    ]):
        assert notification.notification_type == expected.notification_type, "Notification type mismatch in Maple's notifications"
        assert notification.plant_notification == expected.plant_notification, "Notification plant mismatch in Maple's notifications"
        assert now - margin <= notification.time_sent <= now + margin, "Notification time_sent is outside the margin in Maple's notifications"

    for notification, expected in zip(sansevieria.list_notifications, [
        create_notification_watering(sansevieria, notifier),
        create_notification_nutrition(sansevieria, notifier),
        create_notification_repotting(sansevieria, notifier)
    ]):
        assert notification.notification_type == expected.notification_type, "Notification type mismatch in Sansevieria's notifications"
        assert notification.plant_notification == expected.plant_notification, "Notification plant mismatch in Sansevieria's notifications"
        assert now - margin <= notification.time_sent <= now + margin, "Notification time_sent is outside the margin in Sansevieria's notifications"

    for notification, expected in zip(strelitzia.list_notifications, [
        create_notification_watering(strelitzia, notifier),
        create_notification_nutrition(strelitzia, notifier),
        create_notification_repotting(strelitzia, notifier)
    ]):
        assert notification.notification_type == expected.notification_type, "Notification type mismatch in Strelitzia's notifications"
        assert notification.plant_notification == expected.plant_notification, "Notification plant mismatch in Strelitzia's notifications"
        assert now - margin <= notification.time_sent <= now + margin, "Notification time_sent is outside the margin in Strelitzia's notifications"
