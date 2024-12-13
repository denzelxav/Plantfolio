from __future__ import annotations
from typing import TYPE_CHECKING
import datetime
from PySide6.QtCore import Slot, QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QMainWindow

from project.classes.public_methods import sunlight_to_string, get_sun_icon_path, health_to_string, string_to_health
from project.ui.plant_view import Ui_PlantViewWindow
from project.ui_windows.add_plant_window import AddPlantWindow

if TYPE_CHECKING:
    from project.classes.spot_notification import Spot
    from project.classes.userdata import UserData

class PlantViewWindow(QMainWindow):
    def __init__(self, spot: Spot, userdata: UserData):
        super().__init__()
        self.ui = Ui_PlantViewWindow()
        self.ui.setupUi(self)
        self.spot = spot
        self.plant = self.spot.assigned_plant
        self.userdata = userdata

        #setup icons
        icon = QIcon()
        icon.addFile(u"./project/art/water.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.water_plant.setIcon(icon)
        icon1 = QIcon()
        icon1.addFile(u"./project/art/nutrition.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.feed_plant.setIcon(icon1)
        icon2 = QIcon()
        icon2.addFile(u"./project/art/empty_pot.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.repot_plant.setIcon(icon2)
        self.set_plant_icon()
        self.set_spot_sun_icon()
        self.set_preff_sun_icon()

        self.plant_or_no_plant()


        #setup spot info
        self.ui.spot_id.setText(f"Spot name: {self.spot.spot_id}")
        self.ui.spot_sunlight.setText(f"light level: {sunlight_to_string(spot.light_level)}")
        self.ui.humidity.setText(f"humidity: {self.spot.humidity}%")
        self.ui.temperature.setText(f"temperature: {self.spot.temperature}°C")



        #buttons
        self.ui.health_setter.setEnabled(self.ui.manual_health.isChecked())
        self.ui.manual_health.stateChanged.connect(self.handle_manual_health)
        self.ui.health_setter.currentTextChanged.connect(self.handle_health_setter)
        self.ui.water_plant.clicked.connect(self.water_plant)
        self.ui.feed_plant.clicked.connect(self.feed_plant)
        self.ui.repot_plant.clicked.connect(self.repot_plant)
        self.ui.add_delete_plant.clicked.connect(self.add_delete_plant)



    def plant_or_no_plant(self):
        """
        Enables or disables objects according to if there is a plant on the spot or not
        """
        #setting plant text
        self.plant = self.spot.assigned_plant
        if self.plant:
            self.ui.plant_health_text.setText(f"Plant is {health_to_string(self.plant.health)}.")
            self.ui.plant_name.setText(f"name: {self.plant.personal_name}")
            self.ui.scientific_name.setText(f"scientific name: {self.plant.scientific_name}")
            preff_sun_text = f"prefers {sunlight_to_string(self.plant.preff_sunlight[0])}"
            if len(self.plant.preff_sunlight) > 1:
                for sunlight in self.plant.preff_sunlight[1:-1]:
                    preff_sun_text += f", {sunlight_to_string(sunlight)}"
                preff_sun_text += f" or {sunlight_to_string(self.plant.preff_sunlight[-1])}"
            self.ui.preff_sunlight_text.setText(preff_sun_text)
            self.ui.water_frequency_text.setText(f"Water this plant every {self.plant.watering_frequency.days} days")
            self.ui.last_repotted.setText(f"Last repotted at {self.plant.repotted}")
            self.ui.manual_health.setChecked(self.plant.manual_health)
            self.refresh_water_log()

            self.ui.note_text.setText(self.plant.notes)
            self.ui.note_text.textChanged.connect(self.handle_note_text)

        #enabling or disabling text
        add_or_delete_text = "Delete" if self.plant else "Add"
        self.ui.add_delete_plant.setText(f"{add_or_delete_text} plant")
        self.ui.plant_health_text.setHidden(self.plant is None)
        self.ui.plant_name.setHidden(self.plant is None)
        self.ui.scientific_name.setHidden(self.plant is None)
        self.ui.preff_sunlight_text.setHidden(self.plant is None)
        self.ui.water_frequency_text.setHidden(self.plant is None)
        self.ui.last_nutrition.setHidden(self.plant is None)
        if self.plant and self.plant.nutrition:
            self.ui.last_nutrition.setText(f"{self.plant.nutrition[-1].strftime(" % d / % m / % Y")}")
        else:
            self.ui.last_nutrition.setText("Plant hasn't received nutrition yet")
        self.ui.last_repotted.setHidden(self.plant is None)
        self.ui.note_text.setHidden(self.plant is None)
        self.ui.notes_header.setHidden(self.plant is None)
        self.ui.water_log_header.setHidden(self.plant is None)
        self.ui.water_log_list.setHidden(self.plant is None)

        #buttons
        self.ui.water_plant.setEnabled(self.plant is not None)
        self.ui.feed_plant.setEnabled(self.plant is not None)
        self.ui.repot_plant.setEnabled(self.plant is not None)
        self.ui.manual_health.setEnabled(self.plant is not None)

        self.set_plant_icon()
        self.set_preff_sun_icon()



    def set_plant_icon(self):
        if self.plant:
            self.ui.plant_icon.setPixmap(
                QPixmap(f"./project/art/all plants/{self.plant.icon_type}_{self.plant.health.value}.png"))
        else:
            self.ui.plant_icon.setPixmap(
                QPixmap(f"./project/art/empty_pot.png"))

    def set_preff_sun_icon(self):
        """
        sets the preferred sunlight icon to the most sunny of the list
        """
        self.ui.preff_sunlight_icon.setHidden(self.plant is None)
        if self.plant:
            preff_sun = max((sunlight for sunlight in self.plant.preff_sunlight), key=lambda sunlight: sunlight.value)
            self.ui.preff_sunlight_icon.setPixmap(QPixmap(get_sun_icon_path(preff_sun)))

    def set_spot_sun_icon(self):
        """
        Sets the sunlight icon the plant gets
        """
        self.ui.sun_status.setPixmap(QPixmap(get_sun_icon_path(self.spot.light_level)))

    def refresh_water_log(self):
        """
        Refreshes water log list
        """
        self.ui.water_log_list.clear()
        for entry in self.plant.watered:
            self.ui.water_log_list.addItem(entry.strftime('%d/%m/%Y'))

    def refresh_health(self):
        if self.plant:
            self.ui.plant_health_text.setText(f"Plant is {health_to_string(self.plant.health)}.")
            self.set_plant_icon()
        else:
            self.ui.plant_health_text.setText("Select a plant")

    @Slot()
    def handle_manual_health(self):
        self.ui.manual_health.setEnabled(self.plant is not None)
        self.plant.manual_health = self.ui.manual_health.isChecked()
        self.ui.health_setter.setEnabled(self.plant is not None and self.plant.manual_health)
        self.refresh_health()

    @Slot()
    def handle_health_setter(self):
        self.plant.health = string_to_health(self.ui.health_setter.currentText())
        self.refresh_health()

    @Slot()
    def water_plant(self):
        self.plant.water_plant()
        self.refresh_water_log()
        self.refresh_health()

    @Slot()
    def feed_plant(self):
        self.plant.give_nutrition()
        self.ui.last_nutrition.setText(self.plant.nutrition[-1].strftime("%d/%m/%Y"))
        self.refresh_health()

    @Slot()
    def repot_plant(self):
        self.plant.repotted = datetime.datetime.now()
        self.ui.last_repotted.setText(f"last repotted at {self.plant.repotted.strftime('%d/%m/%Y')}")


    @Slot()
    def handle_note_text(self):
        self.plant.notes = self.ui.note_text.toPlainText()

    @Slot()
    def add_delete_plant(self):
        if self.plant:
            self.userdata.delete_plant(self.plant)
            self.plant_or_no_plant()
        else:
            self.add_plant_window = AddPlantWindow(self.spot, self.userdata, self)
            self.add_plant_window.show()

