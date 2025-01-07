"""The main application window"""

from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QMainWindow

from project.classes.userdata import UserData
from project.classes.recommender import Recommender
from project.ui.output import Ui_MainMenu
from project.ui_windows.add_room_window import AddRoomWindow
from project.ui_windows.room_view_window import RoomViewWindow
from project.ui_windows.all_plants_window import AllPlantsWindow
from project.ui_windows.recommendations_window import RecommendationsWindow
from project.classes.save_and_load_userdata import save_user_data
from project.ui_windows.notifier_window import NotifierWindow
from project.classes.notifier import Notifier



import images_qr


class MainMenu(QMainWindow):
    """Example application"""

    def __init__(self, userdata: UserData) -> None:
        super().__init__()
        # Create a file with pyside6-uic project/ui/app.ui -o project/ui/output.py
        self.userdata = userdata
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        self.ui.PlantFolio_Icon.setPixmap(QPixmap(u":/Plantfolio_logo.png"))
        self.setWindowIcon(QIcon(":/Plantfolio_logo_small.png"))

        #buttons
        self.ui.add_room.clicked.connect(self.add_room)
        self.ui.water_all.clicked.connect(self.userdata.water_all)
        self.ui.open_room.clicked.connect(self.open_room)
        self.ui.all_plants.clicked.connect(self.open_all_plants)
        self.ui.save_button.clicked.connect(self.save)
        self.ui.open_recommender.clicked.connect(self.open_recommender)

        self.refresh_rooms()

        self.update_notifications()
        self.ui.refresh_notifications.clicked.connect(self.update_notifications)
        self.ui.sort_notifications_by.currentIndexChanged.connect(self.handle_sort_change)
        self.ui.open_notifier.clicked.connect(self.open_notifier)

    @Slot()
    def add_room(self) -> None:
        """
        Opens AddRoomWindow that lets the user add a room
        """
        self.add_room_window = AddRoomWindow(self)
        self.add_room_window.show()

    @Slot()
    def open_room(self) -> None:
        """
        Opens RoomViewWindow that show the spots a room contains.
        """
        room_name = self.ui.room_list.selectedItems()[0].text()
        self.room_view_window = RoomViewWindow(room_name , self)
        self.room_view_window.show()

    @Slot()
    def save(self):
        save_user_data(self.userdata)

    def update_notifications(self):
        """
        Refreshes the notifications in the notification window
        """
        self.ui.Notification_list.clear()
        notifications = self.notifier.check_tasks_today()
        if notifications:
            for notification in notifications:
                self.ui.Notification_list.addItems(f"{notification.personal_id_plant}, "
                                                   f"{notification.notification_type}")


    def delete_room(self, room: RoomViewWindow) -> None:
        """
        Deletes the selected room that doesn't contain any spots.
        """
        room_name = room.room_name
        self.userdata.delete_room(room_name)
        room.close()
        self.refresh_rooms()

    @Slot()
    def open_notifier(self):
        """
        Opens the notification window
        """
        self.notifier_window = NotifierWindow(self.notifier)
        self.notifier_window.show()

    def handle_sort_change(self, index):
        """
        Handle the change in notification window based
        on type of sorting
        """
        selected_option = self.ui.sort_notifications_by.itemText(index)
        if selected_option == "day":
            self.ui.Notification_list.clear()
            notifications = self.notifier.sort_by_date()
            for notification in notifications:
                self.ui.Notification_list.addItems(f"{notification.personal_id_plant}, "
                                                   f"{notification.notification_type}")
        elif selected_option == "weight":
            self.ui.Notification_list.clear()
            notifications = self.notifier.sort_by_weight()
            for notification in notifications:
                self.ui.Notification_list.addItems(f"{notification.personal_id_plant}, "
                                                   f"{notification.notification_type}")
        elif selected_option == "type":
            self.ui.Notification_list.clear()
            notifications = self.notifier.sort_by_type()
            for notification in notifications:
                self.ui.Notification_list.addItems(f"{notification.personal_id_plant}, "
                                                   f"{notification.notification_type}")

    @Slot()
    def open_all_plants(self) -> None:
        """
        Opens all plants window
        """
        self.all_plants_window = AllPlantsWindow(self.userdata)
        self.all_plants_window.show()

    def refresh_rooms(self) -> None:
        """
        Clears rooms from lists and re adds rooms from userdata
        """
        self.ui.room_list.clear()
        for room in self.userdata.rooms:
            self.ui.room_list.addItem(room)

    @Slot()
    def open_recommender(self) -> None:
        """
        Opens RecommendationsWindow that lets the user see his recommendations
        """
        self.recommendations_window = RecommendationsWindow(self.recommender, self.userdata)
        self.recommendations_window.show()
