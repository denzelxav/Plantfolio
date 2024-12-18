# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'room_view.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QWidget)

class Ui_Room_View(object):
    def setupUi(self, Room_View):
        if not Room_View.objectName():
            Room_View.setObjectName(u"Room_View")
        Room_View.resize(400, 260)
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
        Room_View.setPalette(palette)
        self.spot_list = QListWidget(Room_View)
        self.spot_list.setObjectName(u"spot_list")
        self.spot_list.setGeometry(QRect(30, 30, 341, 141))
        self.open_spot = QPushButton(Room_View)
        self.open_spot.setObjectName(u"open_spot")
        self.open_spot.setGeometry(QRect(220, 180, 75, 24))
        self.add_spot = QPushButton(Room_View)
        self.add_spot.setObjectName(u"add_spot")
        self.add_spot.setGeometry(QRect(300, 180, 75, 24))
        self.delete_spot = QPushButton(Room_View)
        self.delete_spot.setObjectName(u"delete_spot")
        self.delete_spot.setGeometry(QRect(300, 210, 75, 24))
        self.delete_room = QPushButton(Room_View)
        self.delete_room.setObjectName(u"delete_room")
        self.delete_room.setGeometry(QRect(320, 0, 75, 24))
        self.add_plant = QPushButton(Room_View)
        self.add_plant.setObjectName(u"add_plant")
        self.add_plant.setGeometry(QRect(140, 180, 75, 24))
        self.spots_text = QLabel(Room_View)
        self.spots_text.setObjectName(u"spots_text")
        self.spots_text.setGeometry(QRect(30, 10, 49, 16))
        font = QFont()
        font.setBold(True)
        self.spots_text.setFont(font)

        self.retranslateUi(Room_View)

        QMetaObject.connectSlotsByName(Room_View)
    # setupUi

    def retranslateUi(self, Room_View):
        Room_View.setWindowTitle(QCoreApplication.translate("Room_View", u"Room View", None))
        self.open_spot.setText(QCoreApplication.translate("Room_View", u"Open spot", None))
        self.add_spot.setText(QCoreApplication.translate("Room_View", u"Add spot", None))
        self.delete_spot.setText(QCoreApplication.translate("Room_View", u"Delete spot", None))
        self.delete_room.setText(QCoreApplication.translate("Room_View", u"Delete room", None))
        self.add_plant.setText(QCoreApplication.translate("Room_View", u"Add plant", None))
        self.spots_text.setText(QCoreApplication.translate("Room_View", u"Spots", None))
    # retranslateUi

