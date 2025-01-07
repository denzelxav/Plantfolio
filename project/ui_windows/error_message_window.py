from project.ui.error_message import Ui_ErrorMessageWindow
from PySide6.QtWidgets import QDialog
import images_qr


class ErrorMessageWindow(QDialog):
    def __init__(self, message: str, parent=None):
        super().__init__()
        self.ui = Ui_ErrorMessageWindow()
        self.ui.setupUi(self)
        self.ui.close_message.clicked.connect(self.close)
        self.ui.error_message.setText(message)