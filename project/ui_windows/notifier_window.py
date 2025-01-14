from __future__ import annotations
from typing import TYPE_CHECKING
from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QDialog, QMainWindow, QListWidgetItem
import images_qr
from project.classes.spot_notification import Notification

from project.ui.notifier_window_ui import Ui_Notifier_window
if TYPE_CHECKING:
    from project.classes.notifier import Notifier

class NotifierWindow(QMainWindow):
    """
    Window in which you can individually inspect notification
    on all their properties like name, type, weight, orginal_due_date
    """
    def __init__(self, notifier: Notifier):
        super().__init__()
        self.ui = Ui_Notifier_window()
        self.ui.setupUi(self)
        self.notifier = notifier

        # Initialize a placeholder to store notifications
        self.notifications_list: list[Notification] = []

        # set icons
        self.ui.Id_icon.setPixmap(QPixmap(u":/id.png"))
        self.ui.Type_notification_icon.setPixmap(QPixmap(u":/type_notification.png"))
        self.ui.Weight_icon.setPixmap(QPixmap(u":/weight.png"))
        self.ui.Date_icon.setPixmap(QPixmap(u":/date.png"))

        # Initialize the combobox with notifications
        self.refresh_notifications_combobox()
        self.ui.Notifications.currentIndexChanged.connect(self.handle_sort_change)

    def refresh_notifications_combobox(self):
        """
        Fills the combobox with the notifications
        """
        # Fetch the list of notifications
        self.notifications_list = self.notifier.check_tasks_today()

        # Clear the existing items in the QComboBox
        self.ui.Notifications.clear()

        # Add the new notifications to the QComboBox
        if self.notifications_list:
            for notification in self.notifications_list:
                notification_input = f"{notification.plant_notification.personal_name}, "f"{notification.notification_type.name.lower()}"
                self.ui.Notifications.addItem(notification_input)

        # Set up the notification info for the first item (if available)
        if self.notifications_list:
                self.display_notification_info(self.notifications_list[0])

    def handle_sort_change(self, index):
        """
        Handle the change in the selected notification.
        """
        if 0 <= index < len(self.notifications_list):
            selected_notification = self.notifications_list[index]
            self.display_notification_info(selected_notification)

    def display_notification_info(self, notification):
        """
        Update the labels with information about the selected notification.
        """
        self.ui.personal_id_plant.setText(f"Plant: {notification.plant_notification.personal_name}")
        self.ui.notification_type.setText(f"Type of Notification: {notification.notification_type.name.lower()}")
        self.ui.weight.setText(f"Weight: {notification.weight}")
        self.ui.original_due_date.setText(f"Original due date: {notification.original_due_date.date()}")
