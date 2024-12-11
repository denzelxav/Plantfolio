from __future__ import annotations
from typing import TYPE_CHECKING
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QListWidgetItem
from PySide6.QtCore import Slot

from project.classes.spot_notification import Spot
from project.ui.add_plant import Ui_AddPlantWindow
from project.classes.plant import list_all_plants, plant_from_database

if TYPE_CHECKING:
    from project.classes.userdata import UserData
    from project.ui_windows.room_view_window import RoomViewWindow

class AddPlantWindow(QDialog):
    def __init__(self, room: RoomViewWindow, spot: Spot, userdata: UserData):
        super().__init__()
        self.ui = Ui_AddPlantWindow()
        self.ui.setupUi(self)
        self.room = room
        self.spot = spot
        self.userdata = userdata

        for plant_data in list_all_plants():
            self.ui.all_plants_list.addItem(f"{plant_data[0]}: {plant_data[1]}, {plant_data[2]}")

        icons = [("./project/art/all plants/plant_1_healthy.png", "plant1"),
                 ("./project/art/all plants/plant_2_healthy.png", "plant2"),
                 ("./project/art/all plants/plant_3_healthy.png", "plant3")]

        for icon_path, icon_name in icons:
            self.ui.icon_list.addItem(QListWidgetItem(QIcon(icon_path), icon_name))

        self.ui.search_bar.textChanged.connect(self.filter_search)
        self.ui.confirm_plant.accepted.connect(self.add_plant)
        self.ui.confirm_plant.rejected.connect(self.reject)


    @Slot()
    def filter_search(self):
        print(1)
        search = self.ui.search_bar.text().lower()
        for i in range(self.ui.all_plants_list.count()):
            item = self.ui.all_plants_list.item(i)
            print(item.text())
            item.setHidden(search not in item.text().lower())

    @Slot()
    def add_plant(self):
        plant_id = self.ui.all_plants_list.selectedItems()[0].text().split(":")[0]
        plant = plant_from_database(plant_id)
        plant_name = self.ui.name_input.text()
        plant.personal_name = plant_name
        plant.icon_type = self.ui.icon_list.selectedItems()[0].text()
        print(plant.icon_type)
        print(plant)
        self.userdata.add_plant(plant, self.spot)
        print(self.spot)