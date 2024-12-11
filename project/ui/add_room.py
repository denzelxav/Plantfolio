# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_room.ui'
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
    QLabel, QLineEdit, QSizePolicy, QWidget)

class Ui_AddRoomWindow(object):
    def setupUi(self, AddRoomWindow):
        if not AddRoomWindow.objectName():
            AddRoomWindow.setObjectName(u"AddRoomWindow")
        AddRoomWindow.resize(300, 93)
        self.confirm_room = QDialogButtonBox(AddRoomWindow)
        self.confirm_room.setObjectName(u"confirm_room")
        self.confirm_room.setGeometry(QRect(-70, 50, 341, 32))
        self.confirm_room.setOrientation(Qt.Orientation.Horizontal)
        self.confirm_room.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.room_name_input = QLineEdit(AddRoomWindow)
        self.room_name_input.setObjectName(u"room_name_input")
        self.room_name_input.setGeometry(QRect(180, 20, 113, 21))
        font = QFont()
        font.setBold(True)
        self.room_name_input.setFont(font)
        self.label = QLabel(AddRoomWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 20, 71, 16))
        self.label.setFont(font)
        self.house_image = QLabel(AddRoomWindow)
        self.house_image.setObjectName(u"house_image")
        self.house_image.setGeometry(QRect(10, 10, 81, 71))
        self.house_image.setPixmap(QPixmap(u"../art/huisje.png"))
        self.house_image.setScaledContents(True)

        self.retranslateUi(AddRoomWindow)
        self.confirm_room.accepted.connect(AddRoomWindow.accept)
        self.confirm_room.rejected.connect(AddRoomWindow.reject)

        QMetaObject.connectSlotsByName(AddRoomWindow)
    # setupUi

    def retranslateUi(self, AddRoomWindow):
        AddRoomWindow.setWindowTitle(QCoreApplication.translate("AddRoomWindow", u"Add Room", None))
        self.room_name_input.setText("")
        self.label.setText(QCoreApplication.translate("AddRoomWindow", u"Room name", None))
        self.house_image.setText("")
    # retranslateUi

