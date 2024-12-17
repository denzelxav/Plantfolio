"""Main method for starting the application"""

import sys

from PySide6.QtWidgets import QApplication

from project.classes.userdata import UserData
from project.classes.recommender import Recommender
from project.ui_windows.main_menu import MainMenu

if __name__ == "__main__":
    app = QApplication(sys.argv)
    userdata = UserData()
    recommender = Recommender(userdata)
    myApp = MainMenu(userdata, recommender)
    myApp.show()
    app.exec()
