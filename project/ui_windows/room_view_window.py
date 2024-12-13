from __future__ import annotations
from typing import TYPE_CHECKING
from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Slot

from project.classes.spot_notification import Spot
from project.ui.room_view import Ui_Room_View
from project.ui_windows.add_spot_window import AddSpotWindow
from project.ui_windows.add_plant_window import AddPlantWindow
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
        self.refresh_list()
        self.ui.add_spot.clicked.connect(self.add_spot)
        self.ui.delete_room.clicked.connect(self.delete_room)
        self.ui.delete_spot.clicked.connect(self.delete_spot)
        self.ui.add_plant.clicked.connect(self.add_plant)
        self.ui.open_spot.clicked.connect(self.open_plant_view)

    @Slot()
    def open_plant_view(self):
        spot_id = self.ui.spot_list.selectedItems()[0].text()
        selected_spot = self.get_spot(spot_id)
        self.plant_view = PlantViewWindow(selected_spot, self.main_menu.userdata)
        self.plant_view.show()


    @Slot()
    def add_spot(self):
        """
        Open add spot window
        """
        self.add_spot_window = AddSpotWindow(self, self.main_menu)
        self.add_spot_window.show()


    @Slot()
    def delete_spot(self):
        """
        Delete the selected spot
        """
        spot_id = self.ui.spot_list.selectedItems()[0].text()
        selected_spot = self.get_spot(spot_id)
        if selected_spot:
            self.main_menu.userdata.delete_spot(selected_spot)
        self.refresh_list()

    @Slot()
    def add_plant(self):
        spot = self.get_spot(self.ui.spot_list.selectedItems()[0].text())
        if spot.assigned_plant is None:
            self.add_plant_window = AddPlantWindow(spot, self.main_menu.userdata)
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