"""The main application window"""

from PySide6.QtCore import Slot, QSemaphore
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QMainWindow

from project.classes.exceptions import ContainerNotEmpty, NothingSelected
from project.classes.userdata import UserData
from project.classes.recommender import Recommender
from project.ui.output import Ui_MainMenu
from project.ui_windows.add_room_window import AddRoomWindow
from project.ui_windows.confirmation_window import ConfirmationWindow
from project.ui_windows.error_message_window import ErrorMessageWindow
from project.ui_windows.room_view_window import RoomViewWindow
from project.ui_windows.all_plants_window import AllPlantsWindow
from project.ui_windows.recommendations_window import RecommendationsWindow
from project.classes.save_and_load_userdata import save_user_data
from project.ui_windows.notifier_window import NotifierWindow
from project.classes.notifier import Notifier

import images_rc


class MainMenu(QMainWindow):
    """
    The main application window from which all sub windows can be opened.
    Will save its userdata when closed
    """

    def __init__(self, userdata: UserData) -> None:
        super().__init__()
        # Create a file with pyside6-uic project/ui/app.ui -o project/ui/output.py
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)

        self.semaphore = QSemaphore(1)
        self.userdata = userdata
        self.notifier = Notifier(userdata.plants)
        self.recommender = Recommender(userdata)

        self.setWindowIcon(QIcon(":/Plantfolio_logo_small.png"))
        self.ui.PlantFolio_Icon.setPixmap(QPixmap(u":/Plantfolio_logo.png"))
        self.ui.notification_list_frame.setPixmap(QPixmap(u":/list_art.png"))
        self.ui.room_list_frame.setPixmap(QPixmap(u":/list_art.png"))

        #buttons

        self.update_notifications()
        self.ui.refresh_notifications.clicked.connect(self.update_notifications)
        self.ui.sort_notifications_by.currentIndexChanged.connect(self.handle_sort_change)
        self.ui.open_notifier.clicked.connect(self.open_notifier)

        self.ui.add_room.clicked.connect(self.add_room)
        self.ui.water_all.clicked.connect(self.water_all)
        self.ui.open_room.clicked.connect(self.open_room)
        self.ui.all_plants.clicked.connect(self.open_all_plants)
        self.ui.save_button.clicked.connect(self.save)
        self.ui.open_recommender.clicked.connect(self.open_recommender)

        self.refresh_rooms()



    @Slot()
    def add_room(self) -> None:
        """
        Opens AddRoomWindow that lets the user add a room
        """
        try:
            self.add_room_window = AddRoomWindow(self)
        except Exception as e:
            error_msg = ErrorMessageWindow(e)
            error_msg.exec()
        else:
            self.add_room_window.show()

    @Slot()
    def open_room(self) -> None:
        """
        Opens RoomViewWindow that show the spots a room contains.
        """
        try:
            selection = self.ui.room_list.selectedItems()
            if selection:
                room_name = selection[0].text()
            else:
                raise NothingSelected("Selection is empty")
        except NothingSelected:

            error_msg = ErrorMessageWindow("Please select a room.", "No room selected")
            error_msg.exec()
        else:
            self.room_view_window = RoomViewWindow(room_name , self)
            self.room_view_window.show()

    @Slot()
    def save(self):
        """
        Saves user data to json file.
        Located in %appdata%/Plantfolio/user_data.json when running executable.
        Located in ./project/userdata.json when run as python project.
        """
        try:
            save_user_data(self.userdata)
        except Exception as e:
            error_msg = ErrorMessageWindow(e)
            error_msg.exec()

    @Slot()
    def water_all(self):
        """
        Waters all plants and turns grey for 5 seconds
        """
        self.userdata.water_all()
        self.update_notifications()


    def update_notifications(self):
        """
        Refreshes the notifications in the notification window
        """
        self.ui.Notification_list.clear()
        notifications = self.notifier.check_tasks_today()
        if notifications:
            for notification in notifications:
                notification_input = f"{notification.plant_notification.personal_name}, "f"{notification.notification_type.name.lower()}"
                self.ui.Notification_list.addItem(notification_input)


    def delete_room(self, room: RoomViewWindow) -> None:
        """
        Deletes the selected room that doesn't contain any spots.
        """
        room_name = room.room_name
        confirm_deletion = ConfirmationWindow(f"Are you sure you want to delete {room_name}?")
        if confirm_deletion.exec():
            try:
                self.userdata.delete_room(room_name)
            except ContainerNotEmpty:
                error_msg = ErrorMessageWindow(
                    f"Room still contains {len(self.userdata.rooms[room_name])} spots. "
                               "Please remove all spots from the room before deleting",
                               "Room not empty")
                error_msg.exec()
            except Exception as e:
                error_msg = ErrorMessageWindow(e)
                error_msg.exec()


            else:
                room.close()
            finally:
                self.refresh_rooms()

    @Slot()
    def open_notifier(self):
        """
        Opens the notification window
        """
        try:
            self.notifier_window = NotifierWindow(self.notifier)
        except Exception as e:
            error_msg = ErrorMessageWindow(e)
            error_msg.exec()
        else:
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
                notification_input = f"{notification.plant_notification.personal_name}, "f"{notification.notification_type.name.lower()}"
                self.ui.Notification_list.addItem(notification_input)
        elif selected_option == "weight":
            self.ui.Notification_list.clear()
            notifications = self.notifier.sort_by_weight()
            for notification in notifications:
                notification_input = f"{notification.plant_notification.personal_name}, "f"{notification.notification_type.name.lower()}"
                self.ui.Notification_list.addItem(notification_input)
        elif selected_option == "type":
            self.ui.Notification_list.clear()
            notifications = self.notifier.sort_by_type()
            for notification in notifications:
                notification_input = f"{notification.plant_notification.personal_name}, "f"{notification.notification_type.name.lower()}"
                self.ui.Notification_list.addItem(notification_input)

    @Slot()
    def open_all_plants(self) -> None:
        """
        Opens all plants window
        """
        try:
            self.all_plants_window = AllPlantsWindow(self)
        except Exception as e:
            error_msg = ErrorMessageWindow(e)
            error_msg.exec()
        else:
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
        try:
            self.recommendations_window = RecommendationsWindow(self)
        except Exception as e:
            error_msg = ErrorMessageWindow(e)
            error_msg.exec()
        else:
            self.recommendations_window.show()

    def closeEvent(self, event):
       try:
           self.save()
       except Exception as e:
           error_msg = ErrorMessageWindow(e)
           error_msg.exec()
       else:
           event.accept()
