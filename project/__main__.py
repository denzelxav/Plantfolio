"""Main method for starting the application"""

import sys

from PySide6.QtWidgets import QApplication
from project.classes.userdata import UserData
from project.ui_windows.main_menu import MainMenu
from project.classes.save_and_load_userdata import load_user_data

if __name__ == "__main__":
    app = QApplication(sys.argv)
    userdata = load_user_data("./project/user_data.json")
    print(userdata.plants)
    myApp = MainMenu(userdata)
    myApp.show()
    app.exec()
