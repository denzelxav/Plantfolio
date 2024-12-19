import datetime
from project.classes.spot_notification import Notification
from project.classes.enums import Action
from project.classes.plant import Plant

class Notifier:
    """
    Notifier object that hold information about the notifications for specific plant objects.
    attributes:
    - plants(list(Plant)): An user has a set of plants that it takes care of
    - list_notifications(list[Notifications]): A list of tasks that need to be done by the user
    """

    def __init__(self, plants: list[Plant]) -> None:
        self.plants = plants
        self.all_notifications: list[Notification] = []

    def check_tasks_today(self) -> list[Notification] | None:
        """
        Checks if any of the plants that the user has,
        needs to have water, nutrition or needs to be repotted
        """
        # Clear the list to avoid duplicates
        self.all_notifications.clear()

        for plant in self.plants:
            # Check if there is a watering entry
            plant.list_notifications.clear()
            if plant.watered:
                if plant.watered[-1] + plant.watering_frequency <= datetime.datetime.now():
                    weight_watering: float = (datetime.datetime.now() -
                                   (plant.watered[-1] + plant.watering_frequency)).days + 1
                    notification = Notification(weight_watering,
                                                plant.watered[-1] + plant.watering_frequency,
                                                datetime.datetime.now(),
                                                plant.personal_id,
                                                Action.WATERING,
                                                plant,
                                                self
                                                )
                    self.all_notifications.append(notification)
                    plant.list_notifications.append(notification)
            nutrition_frequency = datetime.timedelta(days=30)
            if plant.nutrition:
                if plant.nutrition[-1] + nutrition_frequency <= datetime.datetime.now():
                    weight_nutrition: float = ((datetime.datetime.now() -
                                   (plant.nutrition[-1] + nutrition_frequency)).days + 1) / 2
                    notification = Notification(weight_nutrition,
                                                plant.nutrition[-1] + nutrition_frequency,
                                                datetime.datetime.now(),
                                                plant.personal_id,
                                                Action.NUTRITION,
                                                plant,
                                                self
                                                )
                    self.all_notifications.append(notification)
                    plant.list_notifications.append(notification)

            repotting_frequency = datetime.timedelta(days=365)
            if plant.repotted:
                if plant.repotted + repotting_frequency <= datetime.datetime.now():
                    weight_repotting: float = ((datetime.datetime.now() -
                              (plant.repotted + repotting_frequency)).days + 1) / 10
                    notification = Notification(weight_repotting,
                                                plant.repotted + repotting_frequency,
                                                datetime.datetime.now(),
                                                plant.personal_id,
                                                Action.REPOTTING,
                                                plant,
                                                self
                                                )
                    self.all_notifications.append(notification)
                    plant.list_notifications.append(notification)

        # no tasks for today
        if len(self.all_notifications) == 0:
            return None
        return self.all_notifications


    def sort_by_weight(self) -> list[Notification]:
        """
        Sorts the notifications by weight in descending order
        """
        return sorted(self.all_notifications,
                      key=lambda notification: notification.weight, reverse=True)

    def sort_by_type(self) -> list[Notification]:
        """
        Sorts the notifications by notification type, so all the
        watering/nutrition/repotting notifications grouped
        together
        """
        return sorted(self.all_notifications,
                      key=lambda notification: notification.notification_type.value, reverse=False)

    def sort_by_date(self) -> list[Notification]:
        """
        Sort the notifications by original due date
        """
        return sorted(self.all_notifications,
                      key=lambda notification: notification.original_due_date, reverse=False)

    def sort_by_plant(self) -> list[Notification]:
        """
        Sort the notifications by original plant
        """
        return sorted(self.all_notifications,
                      key=lambda notification: notification.personal_id_plant, reverse=False)
