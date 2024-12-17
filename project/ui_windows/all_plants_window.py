from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QDialog, QListWidgetItem
from datetime import datetime

from project.classes.userdata import UserData
from project.ui.all_plants import Ui_AllPlantsWindow
from project.ui_windows.plant_view_window import PlantViewWindow
from project.classes.plant import Plant


class AllPlantsWindow(QDialog):

    """
    Window showing an overview of all the plants the user owns. 
    These can be sorted on different attributes.
    """

    def __init__(self, userdata: UserData):
        super().__init__()
        self.userdata = userdata
        self.ui = Ui_AllPlantsWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("./project/art/Plantfolio_logo_small.png"))

        self.refresh_list()

        #buttons
        self.ui.cancel_button.clicked.connect(self.reject)
        self.ui.select_plant_button.clicked.connect(self.select_plant)
        self.ui.water_all_button.clicked.connect(self.userdata.water_all)

        #combobox
        self.ui.sort_by.addItem('ID')
        self.ui.sort_by.addItem('Name')
        self.ui.sort_by.addItem('Room')
        self.ui.sort_by.addItem('Species')
        self.ui.sort_by.addItem('Last watered')

        self.ui.sort_by.currentIndexChanged.connect(self.sort_list)

    @Slot()
    def select_plant(self) -> None:
        """
        Opens the plant view window for a selected plant
        """
        plant_id = int(self.ui.select_plant.selectedItems()[0].text().split('\t')[1])
        selected_plant = self.get_plant(plant_id)
        if selected_plant.spot:
            selected_spot = selected_plant.spot
            self.plant_view = PlantViewWindow(selected_spot, self.userdata)
            self.plant_view.show()

    @Slot()
    def sort_list(self) ->  None:
        """
        Sorts the list of plants on a specific attribute
        """
        crit = self.ui.sort_by.currentText()
        if crit == 'ID':
            self.userdata.plants.sort(key = lambda plant: plant.personal_id)
        elif crit == 'Name':
            self.userdata.plants.sort(key = lambda plant: plant.personal_name)
        elif crit == 'Room':
            self.userdata.plants.sort(key = lambda plant: self.get_room(plant))
        elif crit == 'Species':
            self.userdata.plants.sort(key = lambda plant: plant.scientific_name)
        elif crit == 'Last watered':
            self.userdata.plants.sort(key = lambda plant: plant.watered[-1])
        self.refresh_list()

    def get_plant(self, plant_id: int) -> Plant:
        """
        Retrieves the plant object based on the ID
        """
        for plant in self.userdata.plants:
            if plant.personal_id == plant_id:
                return plant
        raise ValueError(f"Plant {plant_id} does not exist")

    def get_room(self, plant: Plant) -> str:
        """
        Retrieves the room a plant is located in
        """
        for room in self.userdata.rooms:
            if plant.spot in self.userdata.rooms[room]:
                return room
        raise IndexError(f"{plant} does not have a room")
    
    def refresh_list(self) -> None:
        """
        Refreshes the list of plants
        """
        self.ui.select_plant.clear()
        for plant in self.userdata.plants:
            item_txt = f'{plant.personal_name} \t {plant.personal_id} \t {self.get_room(plant)} \t {plant.scientific_name} \t {plant.watered[-1].date()}'
            icon  = QIcon(f"./project/art/all plants/{plant.icon_type}_{plant.health.value}.png")
            self.ui.select_plant.addItem(QListWidgetItem(icon, item_txt))
