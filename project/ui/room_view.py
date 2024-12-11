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
from PySide6.QtWidgets import (QApplication, QDialog, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QWidget)

class Ui_Room_View(object):
    def setupUi(self, Room_View):
        if not Room_View.objectName():
            Room_View.setObjectName(u"Room_View")
        Room_View.resize(400, 261)
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
    # retranslateUi

