"""The main application"""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from project.ui.output import Ui_MainWindow


class ExampleApplication(QMainWindow):
    """Example application"""

    def __init__(self):
        super().__init__()
        # Create a file with pyside6-uic project/ui/app.ui -o project/ui/output.py
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    @Slot()
    def button_clicked(self):
        """Triggers if you click the button in the ui"""
        self.ui.label.setText("You CLICKED the BUTTON!!!")
        self.ui.label.setStyleSheet("QLabel {color: red; font-weight: bold;}")
