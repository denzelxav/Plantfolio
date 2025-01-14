from __future__ import annotations
from typing import TYPE_CHECKING
from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog, QListWidgetItem
from PySide6.QtCore import Slot
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
    from project.ui_windows.main_menu import MainMenu


class RoomViewWindow(QDialog):
    """
    Window showing all spots in room
    """
    def __init__(self, room_name: str, main_menu: MainMenu):
        super().__init__()
        self.ui = Ui_Room_View()
        self.ui.setupUi(self)
        self.main_menu = main_menu
        self.setWindowTitle(room_name)
        self.room_name = room_name

        self.ui.room_view_frame.setPixmap(QPixmap(u":/list_art.png"))
        self.ui.house_image.setPixmap(QPixmap(u":/huisje.png"))

        self.refresh_list()
        self.ui.add_spot.clicked.connect(self.add_spot)
        self.ui.delete_room.clicked.connect(self.delete_room)
        self.ui.delete_spot.clicked.connect(self.delete_spot)
        self.ui.add_plant.clicked.connect(self.add_plant)
        self.ui.open_spot.clicked.connect(self.open_plant_view)
        self.ui.spot_list.itemDoubleClicked.connect(self.open_plant_view)
        self.ui.spot_list.itemSelectionChanged.connect(self.handle_item_select)
        self.setWindowIcon(QIcon(":/huisje.png"))

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
    def delete_room(self):
        """
        delete the room that this roomviewwindow corresponds to.
        """
        self.main_menu.delete_room(self)


    @Slot()
    def delete_spot(self):
        """
        Delete the selected spot
        """
        selection= self.ui.spot_list.selectedItems()
        if selection:
            selected_spot = selection[0].data(3)
            try:
                self.main_menu.userdata.delete_spot(selected_spot)
            except ContainerNotEmpty:
                error_msg = ErrorMessageWindow(
                    f"Spot {selected_spot.spot_id} is not not empty. "
                    f"Please delete plant first before deleting spot.",
                    "Spot not empty")
                error_msg.exec()
        self.refresh_list()

    @Slot()
    def add_plant(self):
        """
        Adds a plant to the currently selected  spot
        """
        selection = self.ui.spot_list.selectedItems()
        if selection:
            spot = selection[0].data(3)
            if spot.assigned_plant is None:
                self.add_plant_window = AddPlantWindow(spot, self.main_menu.userdata)
                self.add_plant_window.show()

    @Slot()
    def open_plant_view(self):
        selection = self.ui.spot_list.selectedItems()
        if selection:
            selected_spot = selection[0].data(3)
            self.plant_view = PlantViewWindow(selected_spot, self.main_menu.userdata, self)
            self.plant_view.show()

    @Slot()
    def handle_item_select(self):
        selection = self.ui.spot_list.selectedItems()
        if selection:
            spot = selection[0].data(3)
            self.ui.add_plant.setEnabled(spot.assigned_plant is None)

    def refresh_list(self):
        """
        refreshes spot list
        """
        self.ui.spot_list.clear()
        for spot in self.main_menu.userdata.rooms[self.room_name]:
            item = QListWidgetItem(spot.spot_id)
            item.setData(3, spot)
            self.ui.spot_list.addItem(item)
