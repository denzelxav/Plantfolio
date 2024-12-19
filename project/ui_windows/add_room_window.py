from __future__ import annotations
from typing import TYPE_CHECKING
from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QDialog, QMainWindow, QListWidgetItem
import images_qr

from project.ui.add_room import Ui_AddRoomWindow
if TYPE_CHECKING:
    from project.ui_windows.main_menu import MainMenu


class AddRoomWindow(QDialog):
    """
    Window for adding a new room.
    It takes the main_menu as an argument so it can refer back to it when adding the room.
    """
    def __init__(self, main_menu: MainMenu):
        super().__init__()
        self.ui = Ui_AddRoomWindow()
        self.ui.setupUi(self)
        self.main_menu = main_menu
        self.ui.house_image.setPixmap(QPixmap(u":/huisje.png"))
        self.setWindowIcon(QIcon(":/huisje.png"))

        #buttons
        self.ui.confirm_room.accepted.connect(self.add_room)
        self.ui.confirm_room.rejected.connect(self.reject)


    def add_room(self):
        room_name = self.ui.room_name_input.text()
        if room_name in self.main_menu.userdata.rooms:
            raise ValueError("Room already exists") # TODO
        else:
            self.main_menu.userdata.add_room(room_name)
            self.main_menu.refresh_rooms()

