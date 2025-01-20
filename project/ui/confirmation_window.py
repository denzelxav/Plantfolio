# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirmation_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QWidget)
import images_rc

class Ui_ConfirmationWindow(object):
    def setupUi(self, ConfirmationWindow):
        if not ConfirmationWindow.objectName():
            ConfirmationWindow.setObjectName(u"ConfirmationWindow")
        ConfirmationWindow.resize(335, 117)
        ConfirmationWindow.setMinimumSize(QSize(335, 117))
        ConfirmationWindow.setMaximumSize(QSize(335, 117))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 179))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush2 = QBrush(QColor(64, 159, 63, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        brush3 = QBrush(QColor(165, 204, 159, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette.setBrush(QPalette.Active, QPalette.Accent, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush2)
        ConfirmationWindow.setPalette(palette)
        icon = QIcon()
        icon.addFile(u":/Plantfolio_logo_small.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        ConfirmationWindow.setWindowIcon(icon)
        self.confirmation_box = QDialogButtonBox(ConfirmationWindow)
        self.confirmation_box.setObjectName(u"confirmation_box")
        self.confirmation_box.setGeometry(QRect(10, 70, 311, 32))
        self.confirmation_box.setOrientation(Qt.Orientation.Horizontal)
        self.confirmation_box.setStandardButtons(QDialogButtonBox.StandardButton.No|QDialogButtonBox.StandardButton.Yes)
        self.message = QLabel(ConfirmationWindow)
        self.message.setObjectName(u"message")
        self.message.setGeometry(QRect(10, 50, 361, 21))
        self.exclamation_mark = QLabel(ConfirmationWindow)
        self.exclamation_mark.setObjectName(u"exclamation_mark")
        self.exclamation_mark.setGeometry(QRect(150, 0, 21, 41))
        self.exclamation_mark.setPixmap(QPixmap(u":/exclamation_mark.png"))
        self.exclamation_mark.setScaledContents(True)

        self.retranslateUi(ConfirmationWindow)
        self.confirmation_box.accepted.connect(ConfirmationWindow.accept)
        self.confirmation_box.rejected.connect(ConfirmationWindow.reject)

        QMetaObject.connectSlotsByName(ConfirmationWindow)
    # setupUi

    def retranslateUi(self, ConfirmationWindow):
        ConfirmationWindow.setWindowTitle(QCoreApplication.translate("ConfirmationWindow", u"Dialog", None))
        self.message.setText(QCoreApplication.translate("ConfirmationWindow", u"You are about to delete {plant_name}, are you sure?", None))
        self.exclamation_mark.setText("")
    # retranslateUi

