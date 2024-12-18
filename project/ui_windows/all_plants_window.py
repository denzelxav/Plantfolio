from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QDialog
from datetime import datetime

from project.classes.userdata import UserData
from project.ui.all_plants import Ui_AllPlantsWindow


class AllPlantsWindow(QDialog):

    def __init__(self, userdata: UserData):
        super().__init__()
        self.userdata = userdata
        self.ui = Ui_AllPlantsWindow()
        self.ui.setupUi(self)

        self.refresh_list()

        #buttons
        self.ui.cancel_button.clicked.connect(self.reject)
        self.ui.select_plant_button.clicked.connect(self.select_plant)
        self.ui.water_all_button.clicked.connect(self.userdata.water_all)

        #labels
        self.ui.name_label.setHidden(True)
        self.ui.water_label.setHidden(True)
        self.ui.room_label.setHidden(True)
        self.ui.spot_label.setHidden(True)
        self.ui.species_label.setHidden(True)

        #combobox
        self.ui.sort_by.addItem('ID')
        self.ui.sort_by.addItem('Name')
        self.ui.sort_by.addItem('Room')
        self.ui.sort_by.addItem('Species')
        self.ui.sort_by.addItem('Last watered')

        self.ui.sort_by.currentIndexChanged.connect(self.sort_list)


    @Slot()
    def select_plant(self):
        plant_id = int(self.ui.select_plant.selectedItems()[0].text().split()[-1])
        selected_plant = self.get_plant(plant_id)
        self.ui.plant_icon.setPixmap(
            QPixmap(f"./project/art/all plants/{selected_plant.icon_type}_{selected_plant.health.value}.png"))
        
        self.ui.name_label.setText(f'{selected_plant.personal_name}')
        self.ui.water_label.setText(f'{selected_plant.watered[-1].date()}')
        room = self.get_room(selected_plant)
        self.ui.room_label.setText(f'{room}')
        self.ui.spot_label.setText(f'{selected_plant.spot.spot_id}')
        self.ui.species_label.setText(f'{selected_plant.scientific_name}')

        self.ui.name_label.setHidden(False)
        self.ui.water_label.setHidden(False)
        self.ui.room_label.setHidden(False)
        self.ui.spot_label.setHidden(False)
        self.ui.species_label.setHidden(False)

    @Slot()
    def sort_list(self):
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

    def get_plant(self, plant_id):
        for plant in self.userdata.plants:
            if plant.personal_id == plant_id:
                return plant
        raise ValueError(f"Plant {plant_id} does not exist")

    def get_room(self, plant):
        for room in self.userdata.rooms:
            if plant.spot in self.userdata.rooms[room]:
                return room
        raise IndexError(f"{plant} does not have a room")
    
    def refresh_list(self):
        self.ui.select_plant.clear()
        for plant in self.userdata.plants:
            self.ui.select_plant.addItem(f'{plant.personal_name} \t {plant.personal_id}')
