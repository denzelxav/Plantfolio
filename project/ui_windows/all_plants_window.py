from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QDialog

from project.classes.userdata import UserData
from project.ui.all_plants import Ui_AllPlantsWindow

class AllPlantsWindow(QDialog):

    def __init__(self, userdata: UserData):
        super().__init__()
        self.userdata = userdata
        self.ui = Ui_AllPlantsWindow()
        self.ui.setupUi(self)
        self.ui.plant_icon.setPixmap(QPixmap(u"./project/art/plant_3_healthy.png"))

        #buttons
        self.ui.cancel_button.clicked.connect(self.reject)
        self.ui.select_plant_button.clicked.connect(self.select_plant)

        for plant in self.userdata.plants:
            self.ui.select_plant.addItem(plant.personal_name)

    @Slot()
    def select_plant(self):
        self.ui.select_plant.addItem('did a thing')









