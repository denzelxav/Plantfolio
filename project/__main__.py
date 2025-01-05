"""Main method for starting the application"""
from __future__ import annotations

import sys
from typing import TYPE_CHECKING
from PySide6.QtWidgets import QApplication
from project.classes.userdata import UserData
from project.ui_windows.main_menu import MainMenu
if TYPE_CHECKING:
    from project.classes.notifier import Notifier
    from project.classes.plant import Plant


if __name__ == "__main__":
    app = QApplication(sys.argv)
    plants: list[Plant] = []
    myApp = MainMenu(UserData(), Notifier(plants))
    myApp.show()
    app.exec()
