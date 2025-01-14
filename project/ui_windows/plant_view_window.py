from __future__ import annotations

import os
import sys
from shutil import copyfile
from typing import TYPE_CHECKING
import datetime
from PySide6.QtCore import Slot, QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QMainWindow, QFileDialog, QDialog

from project.classes.public_methods import sunlight_to_string, get_sun_icon_path, string_to_health
from project.ui.plant_view import Ui_PlantViewWindow
from project.ui_windows.add_plant_window import AddPlantWindow
import images_rc
from project.ui_windows.confirmation_window import ConfirmationWindow

if TYPE_CHECKING:
    from project.classes.spot_notification import Spot
    from project.classes.userdata import UserData

class PlantViewWindow(QMainWindow):
    """
    This window shows all the spot details and if a plant is on the spot,
    also the plant details. The plantcare actions can be done here by
    interacting with the buttons and the plants health can be seen by
    looking at the plant icon.
    """
    def __init__(self, spot: Spot, userdata: UserData, parent: QDialog = None) -> None:
        """
        First the spot data is added, then it checks if a plant is assigned
        before setting the appropriate plant details and enabling the buttons.
        """
        super().__init__()
        self.ui = Ui_PlantViewWindow()
        self.ui.setupUi(self)
        self.spot = spot
        self.plant = self.spot.assigned_plant
        self.userdata = userdata
        self.parent = parent
        self.setWindowIcon(QIcon(":/Plantfolio_logo_small.png"))

        #setup icons
        icon = QIcon()
        icon.addFile(":/water.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.water_plant.setIcon(icon)
        icon1 = QIcon()
        icon1.addFile(":/nutrition.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.feed_plant.setIcon(icon1)
        icon2 = QIcon()
        icon2.addFile(":/empty_pot.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        self.ui.add_delete_image.clicked.connect(self.add_delete_image)



    def plant_or_no_plant(self):
        """
        Enables or disables objects according to if there is a plant on the spot or not
        """
        #setting plant text
        self.plant = self.spot.assigned_plant
        if self.plant:
            self.ui.plant_health_text.setText(f"Plant is {self.plant.health.value.replace("_"," ")}.")
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
            self.ui.last_nutrition.setText(f"Last received nutrition on {self.plant.nutrition[-1].strftime('%d/%m/%Y')}")
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
        if self.plant:
            ad_im_txt = "Add image" if self.plant.custom_icon is None else "Delete image"
            self.ui.add_delete_image.setText(ad_im_txt)
        self.ui.add_delete_image.setEnabled(self.plant is not None)

        self.set_plant_icon()
        self.set_preff_sun_icon()



    def set_plant_icon(self):
        if self.plant:
            if not self.plant.custom_icon:
                self.ui.plant_icon.setPixmap(
                    QPixmap(f":/{self.plant.icon_type}_{self.plant.health.value}.png"))
            if self.plant.custom_icon:
                if getattr(sys, 'frozen', False):
                    image_path = os.path.join(os.getenv('APPDATA'), "Plantfolio", "custom_pictures",
                                              self.plant.custom_icon)
                else:
                    image_path = os.path.join("project", "custom_pictures", self.plant.custom_icon)
                self.ui.plant_icon.setPixmap(QPixmap(image_path))
        else:
            self.ui.plant_icon.setPixmap(
                QPixmap(f":/empty_pot.png"))

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
            self.ui.plant_health_text.setText(f"Plant is {self.plant.health.value.replace("_"," ")}.")
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
            confirmation = ConfirmationWindow(f"Are you sure you want to delete {self.plant.personal_name}?")
            if confirmation.exec():
                self.userdata.delete_plant(self.plant)
                self.plant_or_no_plant()
        else:
            add_plant_window = AddPlantWindow(self.spot, self.userdata, self)
            add_plant_window.exec()
        if self.parent.__class__.__name__ == "RoomViewWindow":
            self.parent.handle_item_select()
        else:
            print(self.parent.__class__.__name__)

    @Slot()
    def add_delete_image(self):
        """
        Opens window to add custom image or deletes it, depending on if the plant has one assigned already
        """
        if self.plant.custom_icon:
            confirmation = ConfirmationWindow(f"Are you sure you want to delete this image?")
            if confirmation.exec():
                if getattr(sys, 'frozen', False):
                    image_path = os.path.join(os.getenv('APPDATA'), "Plantfolio", "custom_pictures", self.plant.custom_icon)
                else:
                    image_path = os.path.join("project", "custom_pictures", self.plant.custom_icon)
                os.remove(image_path)
                self.plant.custom_icon = None
        elif not self.plant.custom_icon:
            fname = QFileDialog.getOpenFileName(
                self,
                "Select custom image",
                f"C:/Users/{os.getlogin()}/Pictures/",
                "Image files (*.jpg *.jpeg *.png)",
            )
            if fname[0]:
                old_path = fname[0]
                if getattr(sys, 'frozen', False):
                    directory = os.path.join(os.getenv('APPDATA'), "Plantfolio", "custom_pictures")
                else:
                    directory = os.path.abspath(os.path.join("project", "custom_pictures"))
                try:
                    os.mkdir(os.path.abspath(directory))
                except FileExistsError:
                    pass
                new_path = os.path.join(directory, f"{self.plant.personal_id}.{old_path.split(".")[-1]}")
                copyfile(old_path, new_path)
                self.plant.custom_icon = f"{self.plant.personal_id}.{old_path.split(".")[-1]}"
        self.plant_or_no_plant()
