from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog

from project.ui.confirmation_window import Ui_ConfirmationWindow
import images_rc

class ConfirmationWindow(QDialog):
    """
    Asks for confirmation of an action
    """
    def __init__(self, message: str, parent=None):
        super().__init__()
        self.ui = Ui_ConfirmationWindow()
        self.ui.setupUi(self)
        self.ui.message.setText(message)
        self.ui.confirmation_box.accepted.connect(self.accept)
        self.ui.confirmation_box.rejected.connect(self.reject)
