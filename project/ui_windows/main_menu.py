"""The main application"""

from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QMainWindow

from project.classes.userdata import UserData
from project.ui.output import Ui_MainMenu
from project.ui_windows.add_room_window import AddRoomWindow
from project.ui_windows.room_view_window import RoomViewWindow



class MainMenu(QMainWindow):
    """Example application"""

    def __init__(self, userdata: UserData):
        super().__init__()
        # Create a file with pyside6-uic project/ui/app.ui -o project/ui/output.py
        self.userdata = userdata
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        self.ui.PlantFolio_Icon.setPixmap(QPixmap(u"./art/Plantfolio_logo.png"))
        self.setWindowIcon(QIcon("./art/Plantfolio_logo_small.png"))

        #buttons
        self.ui.add_room.clicked.connect(self.add_room)
        self.ui.water_all.clicked.connect(self.userdata.water_all)
        self.ui.open_room.clicked.connect(self.open_room)


    @Slot()
    def add_room(self):
        self.add_room_window = AddRoomWindow(self)
        self.add_room_window.show()

    @Slot()
    def open_room(self):
        room_name = self.ui.room_list.selectedItems()[0].text()
        self.add_room_window = RoomViewWindow(room_name , self)
        self.add_room_window.show()



    # @Slot()python
    # def button_clicked(self):
    #     """Triggers if you click the button in the ui"""
    #     self.ui.label.setText("You CLICKED the BUTTON!!!")
    #     self.ui.label.setStyleSheet("QLabel {color: red; font-weight: bold;}")
