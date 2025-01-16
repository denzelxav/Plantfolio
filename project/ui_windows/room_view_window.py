from __future__ import annotations
from typing import TYPE_CHECKING
from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Slot, QSemaphore
from PySide6.QtGui import QIcon, QPixmap

import images_rc
from project.classes.exceptions import ContainerNotEmpty
from project.classes.spot_notification import Spot
from project.ui.room_view import Ui_Room_View
from project.ui_windows.add_spot_window import AddSpotWindow
from project.ui_windows.add_plant_window import AddPlantWindow
from project.ui_windows.error_message_window import ErrorMessageWindow
from project.ui_windows.plant_view_window import PlantViewWindow
if TYPE_CHECKING:
    from project.classes.userdata import UserData
    from project.ui_windows.main_menu import MainMenu


class RoomViewWindow(QDialog):
    """
    Window showing all spots in room
    """
    def __init__(self, room_name: str, parent: MainMenu) -> None:
        super().__init__()
        self.ui = Ui_Room_View()
        self.ui.setupUi(self)

        self.main_menu = parent
        self.semaphore: QSemaphore = parent.semaphore
        self.userdata: UserData = parent.userdata

        self.room_name = room_name

        self.setWindowTitle(room_name)
        self.ui.room_view_frame.setPixmap(QPixmap(u":/list_art.png"))
        self.ui.house_image.setPixmap(QPixmap(u":/huisje.png"))

        self.refresh_list()
        self.ui.add_spot.clicked.connect(self.add_spot)
        self.ui.delete_room.clicked.connect(self.delete_room)
        self.ui.delete_spot.clicked.connect(self.delete_spot)
        self.ui.add_plant.clicked.connect(self.add_plant)
        self.ui.open_spot.clicked.connect(self.open_plant_view)
        self.setWindowIcon(QIcon(":/huisje.png"))

    @Slot()
    def open_plant_view(self):
        spot_id = self.ui.spot_list.selectedItems()[0].text()
        selected_spot = self.get_spot(spot_id)
        self.plant_view = PlantViewWindow(selected_spot, self)
        self.plant_view.show()


    @Slot()
    def add_spot(self):
        """
        Open add spot window
        """
        try:
            self.add_spot_window = AddSpotWindow(self, self.main_menu)
        except Exception as e:
            error_msg = ErrorMessageWindow(e)
            error_msg.exec()
        else:
            self.add_spot_window.show()


    @Slot()
    def delete_spot(self):
        """
        Delete the selected spot
        """
        selection= self.ui.spot_list.selectedItems()
        if selection:
            spot_id = selection[0].text()
            try:
                selected_spot = self.get_spot(spot_id)
            except ValueError as e:
                error_msg = ErrorMessageWindow(e)
                error_msg.exec()
            else:
                if selected_spot:
                    try:
                        self.main_menu.userdata.delete_spot(selected_spot)
                    except ContainerNotEmpty:
                        error_msg = ErrorMessageWindow(
                            f"Spot {selected_spot} is not not empty. "
                            f"Please delete plant first before deleting spot.",
                            "Spot not empty")
                        error_msg.exec()
        else:
            error_msg = ErrorMessageWindow("Please select a spot to delete", "No spot selected")
            error_msg.exec()
        self.refresh_list()

    @Slot()
    def add_plant(self):
        spot = self.get_spot(self.ui.spot_list.selectedItems()[0].text())
        if spot.assigned_plant is None:
            self.add_plant_window = AddPlantWindow(spot, self)
            self.add_plant_window.show()

    @Slot()
    def delete_room(self):
        """
        delete the room that this roomviewwindow corresponds to.
        """
        self.main_menu.delete_room(self)

    def refresh_list(self):
        """
        refreshes spot list
        """
        self.ui.spot_list.clear()
        for spot in self.main_menu.userdata.rooms[self.room_name]:
            self.ui.spot_list.addItem(spot.spot_id)

    def get_spot(self, spot_id: str) -> Spot:
        """
        Returns spot object from userdata based on the spot id.
        """
        for spot in self.main_menu.userdata.rooms[self.room_name]:
            if spot.spot_id == spot_id:
                return spot
        raise ValueError(f"Spot {spot_id} does not exist")