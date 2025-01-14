from __future__ import annotations
from typing import TYPE_CHECKING
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Slot

import images_rc
from project.classes.exceptions import NameTakenError
from project.classes.public_methods import string_to_sunlight
from project.classes.spot_notification import Spot
from project.ui.add_spot import Ui_AddSpotWindow
from project.ui_windows.error_message_window import ErrorMessageWindow

if TYPE_CHECKING:
    from project.ui_windows.main_menu import MainMenu
    from project.ui_windows.room_view_window import RoomViewWindow

class AddSpotWindow(QDialog):
    def __init__(self, room: RoomViewWindow, main_menu:MainMenu):
        super().__init__()
        self.ui = Ui_AddSpotWindow()
        self.ui.setupUi(self)
        self.ui.sun_image.setPixmap(QPixmap(":/full_sun.png"))
        self.room = room
        self.main_menu = main_menu
        self.setWindowIcon(QIcon(":/Plantfolio_logo_small.png"))

        #buttons
        self.ui.add_spot_button.clicked.connect(self.add_spot)
        self.ui.cancel_button.clicked.connect(self.reject)

    @Slot()
    def add_spot(self):
        spot_name = self.ui.Spot_Name_input.text()
        light_level = string_to_sunlight(self.ui.sunlight_input.currentText())
        humidity = self.ui.humidity_input.text()
        temperature = self.ui.temperature_input.value()

        spot = Spot(spot_name, light_level, humidity, None, temperature, self.room.room_name)
        try:
            self.main_menu.userdata.add_spot(spot)
        except NameTakenError:
            error_msg = ErrorMessageWindow(f"spot named {spot_name} already exists, please choose another name", "Name taken")
            error_msg.exec()
        else:
            self.close()
        finally:
            self.room.refresh_list()