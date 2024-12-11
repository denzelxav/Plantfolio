from __future__ import annotations
from typing import TYPE_CHECKING
from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog

from project.ui.room_view import Ui_Room_View
from project.ui_windows.add_spot_window import AddSpotWindow
if TYPE_CHECKING:
    from project.ui_windows.main_menu import MainMenu


class RoomViewWindow(QDialog):
    def __init__(self, room_name: str, main_menu: MainMenu):
        super().__init__()
        self.ui = Ui_Room_View()
        self.ui.setupUi(self)
        self.main_menu = main_menu
        self.setWindowTitle(room_name)
        self.room_name = room_name
        self.refresh_list()
        self.ui.add_spot.clicked.connect(self.add_spot)

    def add_spot(self):
        self.add_spot_window = AddSpotWindow(self, self.main_menu)
        self.add_spot_window.show()

    def refresh_list(self):
        self.ui.spot_list.clear()
        for spot in self.main_menu.userdata.rooms[self.room_name]:
            self.ui.spot_list.addItem(spot.spot_id)