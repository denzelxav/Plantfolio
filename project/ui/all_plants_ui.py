# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'all_plants.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_AllPlantsWindow(object):
    def setupUi(self, AllPlantsWindow):
        if not AllPlantsWindow.objectName():
            AllPlantsWindow.setObjectName(u"AllPlantsWindow")
        AllPlantsWindow.resize(403, 324)
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
        AllPlantsWindow.setPalette(palette)
        self.select_plant = QListWidget(AllPlantsWindow)
        self.select_plant.setObjectName(u"select_plant")
        self.select_plant.setGeometry(QRect(10, 90, 256, 221))
        self.select_label = QLabel(AllPlantsWindow)
        self.select_label.setObjectName(u"select_label")
        self.select_label.setGeometry(QRect(10, 70, 151, 16))
        font = QFont()
        font.setBold(True)
        self.select_label.setFont(font)
        self.plant_icon = QLabel(AllPlantsWindow)
        self.plant_icon.setObjectName(u"plant_icon")
        self.plant_icon.setGeometry(QRect(280, 90, 101, 141))
        self.plant_icon.setPixmap(QPixmap(u"../art/all plants/plant_3_healthy.png"))
        self.plant_icon.setScaledContents(True)
        self.name_label = QLabel(AllPlantsWindow)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(280, 230, 49, 16))
        self.water_label = QLabel(AllPlantsWindow)
        self.water_label.setObjectName(u"water_label")
        self.water_label.setGeometry(QRect(280, 250, 81, 16))
        self.room_label = QLabel(AllPlantsWindow)
        self.room_label.setObjectName(u"room_label")
        self.room_label.setGeometry(QRect(280, 270, 49, 16))
        self.spot_label = QLabel(AllPlantsWindow)
        self.spot_label.setObjectName(u"spot_label")
        self.spot_label.setGeometry(QRect(280, 290, 49, 16))
        self.sort_by = QComboBox(AllPlantsWindow)
        self.sort_by.setObjectName(u"sort_by")
        self.sort_by.setGeometry(QRect(180, 60, 80, 24))
        self.cancel_button = QPushButton(AllPlantsWindow)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(320, 10, 75, 24))
        self.select_plant_button = QPushButton(AllPlantsWindow)
        self.select_plant_button.setObjectName(u"select_plant_button")
        self.select_plant_button.setGeometry(QRect(270, 60, 75, 24))

        self.retranslateUi(AllPlantsWindow)

        QMetaObject.connectSlotsByName(AllPlantsWindow)
    # setupUi

    def retranslateUi(self, AllPlantsWindow):
        AllPlantsWindow.setWindowTitle(QCoreApplication.translate("AllPlantsWindow", u"All plants", None))
        self.select_label.setText(QCoreApplication.translate("AllPlantsWindow", u"All your plants:", None))
        self.plant_icon.setText("")
        self.name_label.setText(QCoreApplication.translate("AllPlantsWindow", u"Name", None))
        self.water_label.setText(QCoreApplication.translate("AllPlantsWindow", u"Last watered", None))
        self.room_label.setText(QCoreApplication.translate("AllPlantsWindow", u"Room", None))
        self.spot_label.setText(QCoreApplication.translate("AllPlantsWindow", u"Spot", None))
        self.cancel_button.setText(QCoreApplication.translate("AllPlantsWindow", u"Cancel", None))
        self.select_plant_button.setText(QCoreApplication.translate("AllPlantsWindow", u"Select plant", None))
    # retranslateUi

