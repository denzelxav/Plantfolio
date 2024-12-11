"""The main application"""

from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow

from project.classes.userdata import UserData
from project.ui.output import Ui_MainMenu
from project.ui_windows.add_room_window import AddRoomWindow



class MainMenu(QMainWindow):
    """Example application"""

    def __init__(self, userdata: UserData):
        super().__init__()
        # Create a file with pyside6-uic project/ui/app.ui -o project/ui/output.py
        self.userdata = userdata
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        self.ui.PlantFolio_Icon.setPixmap(QPixmap(u"./art/Plantfolio_logo.png"))

        #buttons
        self.ui.add_room.clicked.connect(self.add_room)


    @Slot()
    def add_room(self):
        self.add_room_window = AddRoomWindow(self)
        self.add_room_window.show()



    # @Slot()
    # def button_clicked(self):
    #     """Triggers if you click the button in the ui"""
    #     self.ui.label.setText("You CLICKED the BUTTON!!!")
    #     self.ui.label.setStyleSheet("QLabel {color: red; font-weight: bold;}")
