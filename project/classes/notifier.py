import datetime

from project.classes.spot_notification import Notification
from project.classes.enums import Type_of_action
from project.classes.plant import Plant

class Notifier:
    """
    Notifier object that hold information about the notifications for specific plant objects.
    - plants(list(Plant)): An user has a set of plants that it takes care of
    - list_notifications(list[Notifications]): A list of tasks that need to be done by the user
    """

    def __init__(self, plants: list[Plant]) -> None:
        self.plants = plants
        self.list_notifications: list[Notification] = []

    def check_tasks_today(self) -> list[Notification] | None:
        """
        Checks if any of the plants that the user has,
        needs to have water, nutrition or needs to be repotted
        """
        # Clear the list to avoid duplicates
        self.list_notifications.clear()

        for plant in self.plants:
            # Check if there is a watering entry
            if plant.watered:
                if plant.watered[-1] + plant.watering_frequency <= datetime.datetime.now():
                    weight: int = (datetime.datetime.now() -
                                   (plant.watered[-1] + plant.watering_frequency)).days + 1
                    self.list_notifications.append(Notification(weight,
                                                                plant.watered[-1] + plant.watering_frequency,
                                                                datetime.datetime.now(),
                                                                plant.core_id,
                                                                Type_of_action.WATERING,
                                                                plant
                                                                ))
            nutrition_frequency = datetime.timedelta(days=30)
            if plant.nutrition:
                if plant.nutrition[-1] + nutrition_frequency <= datetime.datetime.now():
                    weight: int = (datetime.datetime.now() -
                                   (plant.nutrition[-1] + nutrition_frequency)).days + 1
                    self.list_notifications.append(Notification(weight,
                                                                plant.nutrition[-1] + nutrition_frequency,
                                                                datetime.datetime.now(),
                                                                plant.core_id,
                                                                Type_of_action.NUTRITION,
                                                                plant
                                                                ))

            repotting_frequency: datetime = datetime.timedelta(days=365)
            if plant.repotted:
                if plant.repotted + repotting_frequency <= datetime.datetime.now():
                    weight = (datetime.datetime.now() -
                              (plant.repotted + repotting_frequency)).days + 1
                    self.list_notifications.append(Notification(weight,
                                                                plant.repotted + repotting_frequency,
                                                                datetime.datetime.now(),
                                                                plant.core_id,
                                                                Type_of_action.REPOTTING,
                                                                plant
                                                                ))

        # no tasks for today
        if len(self.list_notifications) == 0:
            return None
        else:
            return self.list_notifications


    def sort_by_weight(self) -> list[Notification]:
        """
        Sorts the notifications by weight in descending order
        """
        return sorted(self.list_notifications,
                      key=lambda notification: notification.weight, reverse=True)

    def sort_by_type(self) -> list[Notification]:
        """
        Sorts the notifications by notification type, so all the
        watering/nutrition/repotting notifications grouped
        together
        """
        return sorted(self.list_notifications,
                      key=lambda notification: notification.notification_type.value, reverse=False)

    def sort_by_date(self) -> list[Notification]:
        """
        Sort the notifications by original due date
        """
        return sorted(self.list_notifications,
                      key=lambda notification: notification.original_due_date, reverse=False)



