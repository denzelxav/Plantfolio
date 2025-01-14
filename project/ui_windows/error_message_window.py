from project.ui.error_message import Ui_ErrorMessageWindow
from PySide6.QtWidgets import QDialog
import images_rc


class ErrorMessageWindow(QDialog):
    def __init__(self, exception: Exception | str, title: str | None = None, parent=None):
        super().__init__()
        self.ui = Ui_ErrorMessageWindow()
        self.ui.setupUi(self)
        self.ui.close_message.clicked.connect(self.close)
        if isinstance(exception, Exception):
            title = type(exception).__name__
        elif title is None:
            raise ValueError("Must give a title when passing string as exception")
        self.ui.error_type.setText(title)
        self.ui.error_message.setText(str(exception))