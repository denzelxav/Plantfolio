from __future__ import annotations
from typing import TYPE_CHECKING
from PySide6 import QtWidgets
from PySide6.QtCore import Slot, QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QMainWindow

from project.classes.enums import Sunlight
from project.classes.public_methods import sunlight_to_string, get_sun_icon_path, health_to_string, string_to_health
from project.ui.plant_view import Ui_PlantViewWindow

if TYPE_CHECKING:
    from project.classes.userdata import UserData
    from project.ui_windows.room_view_window import RoomViewWindow
    from project.classes.spot_notification import Spot

class PlantViewWindow(QMainWindow):
    def __init__(self, spot: Spot):
        super().__init__()
        self.ui = Ui_PlantViewWindow()
        self.ui.setupUi(self)
        self.spot = spot
        self.plant = self.spot.assigned_plant


        icon = QIcon()
        icon.addFile(u"./project/art/water.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.water_plant.setIcon(icon)
        icon1 = QIcon()
        icon1.addFile(u"./project/art/nutrition.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.feed_plant.setIcon(icon1)
        self.set_plant_icon()
        self.set_spot_sun_icon()
        self.set_preff_sun_icon()

        self.ui.plant_health_text.setText(f"Plant is {health_to_string(self.plant.health)}.")
        self.ui.plant_name.setText(f"name: {self.plant.personal_name}")
        self.ui.scientific_name.setText(f"scientific name: {self.plant.scientific_name}")
        preff_sun_text = f"prefers {sunlight_to_string(self.plant.preff_sunlight[0])}"
        if len(self.plant.preff_sunlight) > 1:
            for sunlight in self.plant.preff_sunlight[1:-1]:
                preff_sun_text += f", {sunlight_to_string(sunlight)}"
            preff_sun_text += f" or {sunlight_to_string(self.plant.preff_sunlight[-1])}"
        self.ui.preff_sunlight_text.setText(preff_sun_text)
        self.ui.spot_id = f"spot name: {self.spot.spot_id}"
        self.ui.spot_sunlight = f"sunlight status:{sunlight_to_string(spot.light_level)}"

        #buttons
        self.ui.manual_health.setChecked(self.plant.manual_health)
        self.ui.health_setter.setEnabled(self.ui.manual_health.isChecked())
        self.ui.manual_health.stateChanged.connect(self.handle_manual_health)
        self.ui.health_setter.currentTextChanged.connect(self.handle_health_setter)


    def set_plant_icon(self):
        self.ui.plant_icon.setPixmap(
            QPixmap(f"./project/art/all plants/{self.plant.icon_type}_{self.plant.health.value}.png"))

    def set_preff_sun_icon(self):
        """
        sets the preferred sunlight icon to the most sunny of the list
        """
        preff_sun = max((sunlight for sunlight in self.plant.preff_sunlight), key=lambda sunlight: sunlight.value)
        self.ui.preff_sunlight_icon.setPixmap(QPixmap(get_sun_icon_path(preff_sun)))

    def set_spot_sun_icon(self):
        """
        Sets the sunlight icon the plant gets
        """
        self.ui.sun_status.setPixmap(QPixmap(get_sun_icon_path(self.spot.light_level)))


    @Slot()
    def handle_manual_health(self):
        self.plant.manual_health = self.ui.manual_health.isChecked()
        self.ui.health_setter.setEnabled(self.plant.manual_health)
        self.set_plant_icon()
        self.ui.plant_health_text.setText(f"Plant is {health_to_string(self.plant.health)}.")

    @Slot()
    def handle_health_setter(self):
        self.plant.health = string_to_health(self.ui.health_setter.currentText())
        self.ui.plant_health_text.setText(f"Plant is {health_to_string(self.plant.health)}.")
        self.set_plant_icon()