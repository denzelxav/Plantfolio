from __future__ import annotations
from typing import TYPE_CHECKING
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QListWidgetItem
from PySide6.QtCore import Slot

from project.classes.spot_notification import Spot
from project.ui.add_plant import Ui_AddPlantWindow
from project.classes.plant import list_all_plants, plant_from_database

if TYPE_CHECKING:
    from project.classes.userdata import UserData
    from project.ui_windows.plant_view_window import PlantViewWindow

class AddPlantWindow(QDialog):
    def __init__(self, spot: Spot, userdata: UserData, parent: PlantViewWindow | None =None):
        super().__init__()
        self.ui = Ui_AddPlantWindow()
        self.ui.setupUi(self)
        self.spot = spot
        self.userdata = userdata
        self.parent_window = parent

        for plant_data in list_all_plants():
            self.ui.all_plants_list.addItem(f"{plant_data[0]}: {plant_data[1]}, {plant_data[2]}")

        icons = [("./project/art/all plants/plant_1_healthy.png", "plant_1"),
                 ("./project/art/all plants/plant_2_healthy.png", "plant_2"),
                 ("./project/art/all plants/plant_3_healthy.png", "plant_3")]

        for icon_path, icon_name in icons:
            self.ui.icon_list.addItem(QListWidgetItem(QIcon(icon_path), icon_name))

        self.ui.search_bar.textChanged.connect(self.filter_search)
        self.ui.confirm_plant.accepted.connect(self.add_plant)
        self.ui.confirm_plant.rejected.connect(self.reject)


    @Slot()
    def filter_search(self):
        search = self.ui.search_bar.text().lower()
        for i in range(self.ui.all_plants_list.count()):
            item = self.ui.all_plants_list.item(i)
            item.setHidden(search not in item.text().lower())

    @Slot()
    def add_plant(self):
        plant_id = self.ui.all_plants_list.selectedItems()[0].text().split(":")[0]
        plant = plant_from_database(plant_id)
        plant_name = self.ui.name_input.text()
        plant.personal_name = plant_name
        plant.icon_type = self.ui.icon_list.selectedItems()[0].text()
        self.userdata.add_plant(plant, self.spot)
        if self.parent_window:
            self.parent_window.plant_or_no_plant()
