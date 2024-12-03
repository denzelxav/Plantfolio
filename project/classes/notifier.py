from project.classes.spot_notification import Notification


class Notifier
    def __init__(self, list[Notification]) -> None:
        self.list_notifications = list[Notification]

    def sort_by_weight(self) -> list[Notification]:
        copy_notifications = self.list_notifications.copy()
        sorted_by_weight = []
        for _ in range(len(copy_notifications)):
            sorted_by_weight.append(copy_notifications.pop(copy_notifications.index(max(copy_notifications))))
        return sorted_by_weight

    def sort_by_type(self) -> list[Notification]:
        pass

    def sort_by_date(self) -> list[Notification]:
        pass

    def refresh_notifications(self) -> list[Notification]:
        pass

