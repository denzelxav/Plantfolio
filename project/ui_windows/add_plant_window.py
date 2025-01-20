from __future__ import annotations
from typing import TYPE_CHECKING
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QDialog, QListWidgetItem
from PySide6.QtCore import Slot

from project.classes.exceptions import EmptyNameError
from project.classes.spot_notification import Spot
from project.ui.add_plant import Ui_AddPlantWindow
from project.classes.plant import list_all_plants_in_database, plant_from_database
from project.ui_windows.error_message_window import ErrorMessageWindow

if TYPE_CHECKING:
    from project.classes.userdata import UserData
    from project.ui_windows.plant_view_window import PlantViewWindow

class AddPlantWindow(QDialog):
    """
    Window from which you can add plants to a spot
    """
    def __init__(self, spot: Spot, userdata: UserData, parent: PlantViewWindow | None =None) -> None:
        super().__init__()
        self.ui = Ui_AddPlantWindow()
        self.ui.setupUi(self)
        self.spot = spot
        self.userdata = userdata
        self.parent_window = parent
        self.setWindowIcon(QIcon(":/Plantfolio_logo_small.png"))

        self.ui.icon_frame.setPixmap(QPixmap(u":/list_art.png"))
        self.ui.search_frame.setPixmap(QPixmap(u":/list_art.png"))
        self.ui.small_logo.setPixmap(QPixmap(u":/Plantfolio_logo_small.png"))

        for plant_data in list_all_plants_in_database():
            self.ui.all_plants_list.addItem(f"{plant_data[0]}: {plant_data[1]}, {plant_data[2]}")

        icons = [(":/plant_1_healthy.png", "plant_1"),
                 (":/plant_2_healthy.png", "plant_2"),
                 (":/plant_3_healthy.png", "plant_3")]

        for icon_path, icon_name in icons:
            self.ui.icon_list.addItem(QListWidgetItem(QIcon(icon_path), icon_name))

        self.ui.search_bar.textChanged.connect(self.filter_search)
        self.ui.confirm_plant.accepted.connect(self.add_plant)
        self.ui.confirm_plant.rejected.connect(self.reject)


    @Slot()
    def filter_search(self) -> None:
        """
        Hides items that do not correspond to the text in the search bar.
        """
        search = self.ui.search_bar.text().lower()
        for i in range(self.ui.all_plants_list.count()):
            item = self.ui.all_plants_list.item(i)
            item.setHidden(search not in item.text().lower())

    @Slot()
    def add_plant(self) -> None:
        """
        Adds the selected plant to the userdata, refreshes the plant view window
        and closes the AddPlantWindow.
        """
        plant_id = self.ui.all_plants_list.selectedItems()[0].text().split(":")[0]
        plant = plant_from_database(plant_id)
        plant_name = self.ui.name_input.text()
        plant.personal_name = plant_name
        plant.icon_type = self.ui.icon_list.selectedItems()[0].text()
        try:
            self.userdata.add_plant(plant, self.spot)
        except EmptyNameError:
            error_msg = ErrorMessageWindow("Please fill in plant name.", "Plant name is empty")
            error_msg.exec()
        if self.parent_window:
            self.parent_window.plant_or_no_plant()
