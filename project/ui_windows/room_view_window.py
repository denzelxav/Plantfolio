from __future__ import annotations
from typing import TYPE_CHECKING
from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog

from project.ui.room_view import Ui_Room_View
if TYPE_CHECKING:
    from project.ui_windows.main_menu import MainMenu


class RoomViewWindow(QDialog):
    def __init__(self, room_name: str, main_menu: MainMenu):
        super().__init__()
        self.ui = Ui_Room_View()
        self.ui.setupUi(self)
        self.main_menu = main_menu
        self.setWindowTitle(room_name)
        for spot in self.main_menu.userdata.rooms[room_name]:
            self.ui.spot_list.addItem(spot)