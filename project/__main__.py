"""Main method for starting the application"""

import sys

from PySide6.QtWidgets import QApplication

from project.application import ExampleApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = ExampleApplication()
    myApp.show()
    app.exec()
