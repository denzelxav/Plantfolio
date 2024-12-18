from __future__ import annotations
from typing import TYPE_CHECKING
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QDialog

import images_qr
from project.classes.public_methods import string_to_sunlight
from project.classes.spot_notification import Spot
from project.ui.add_spot import Ui_AddSpotWindow
if TYPE_CHECKING:
    from project.ui_windows.main_menu import MainMenu
    from project.ui_windows.room_view_window import RoomViewWindow

class AddSpotWindow(QDialog):
    def __init__(self, room: RoomViewWindow, main_menu:MainMenu):
        super().__init__()
        self.ui = Ui_AddSpotWindow()
        self.ui.setupUi(self)
        self.ui.empty_pot_image.setPixmap(QPixmap(":/empty_pot.png"))
        self.room = room
        self.main_menu = main_menu
        self.setWindowIcon(QIcon(":/Plantfolio_logo_small.png"))

        #buttons
        self.ui.confirm_spot.accepted.connect(self.add_spot)
        self.ui.confirm_spot.rejected.connect(self.reject)

    def add_spot(self):
        spot_name = self.ui.Spot_Name_input.text()
        light_level = string_to_sunlight(self.ui.sunlight_input.currentText())
        humidity = self.ui.humidity_input.text()
        temperature = self.ui.temperature_input.value()

        spot = Spot(spot_name, light_level, humidity, None, temperature)

        self.main_menu.userdata.add_spot(spot, self.room.room_name)
        self.room.refresh_list()