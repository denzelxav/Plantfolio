"""Main method for starting the application"""

import sys
from PySide6.QtWidgets import QApplication

from project.ui_windows.main_menu import MainMenu
from project.classes.save_and_load_userdata import load_user_data
from project.ui_windows.error_message_window import ErrorMessageWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        userdata = load_user_data()
    except FileNotFoundError as e:
        error_app = ErrorMessageWindow(e)
        error_app.exec()
    else:
        myApp = MainMenu(userdata)
        myApp.show()
        app.exec()
