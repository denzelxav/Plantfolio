# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_Main_Menu(object):
    def setupUi(self, Main_Menu):
        if not Main_Menu.objectName():
            Main_Menu.setObjectName(u"Main_Menu")
        Main_Menu.resize(608, 450)
        self.centralwidget = QWidget(Main_Menu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.PlantFolio_Icon = QLabel(self.centralwidget)
        self.PlantFolio_Icon.setObjectName(u"PlantFolio_Icon")
        self.PlantFolio_Icon.setGeometry(QRect(0, -10, 381, 131))
        self.PlantFolio_Icon.setPixmap(QPixmap(u"../art/Plantfolio_logo.png"))
        self.PlantFolio_Icon.setScaledContents(True)
        self.open_rooms = QPushButton(self.centralwidget)
        self.open_rooms.setObjectName(u"open_rooms")
        self.open_rooms.setGeometry(QRect(40, 350, 75, 24))
        self.open_notifier = QPushButton(self.centralwidget)
        self.open_notifier.setObjectName(u"open_notifier")
        self.open_notifier.setGeometry(QRect(350, 350, 75, 24))
        self.Notification_list = QListWidget(self.centralwidget)
        self.Notification_list.setObjectName(u"Notification_list")
        self.Notification_list.setGeometry(QRect(340, 150, 256, 192))
        self.open_recommender = QPushButton(self.centralwidget)
        self.open_recommender.setObjectName(u"open_recommender")
        self.open_recommender.setGeometry(QRect(450, 50, 111, 31))
        self.Room_list = QListWidget(self.centralwidget)
        self.Room_list.setObjectName(u"Room_list")
        self.Room_list.setGeometry(QRect(30, 151, 201, 181))
        self.water_all_button = QPushButton(self.centralwidget)
        self.water_all_button.setObjectName(u"water_all_button")
        self.water_all_button.setGeometry(QRect(240, 120, 75, 24))
        self.add_room_button = QPushButton(self.centralwidget)
        self.add_room_button.setObjectName(u"add_room_button")
        self.add_room_button.setGeometry(QRect(120, 350, 75, 24))
        self.all_plants = QPushButton(self.centralwidget)
        self.all_plants.setObjectName(u"all_plants")
        self.all_plants.setGeometry(QRect(240, 150, 75, 24))
        self.sort_notifications = QComboBox(self.centralwidget)
        self.sort_notifications.addItem("")
        self.sort_notifications.addItem("")
        self.sort_notifications.addItem("")
        self.sort_notifications.setObjectName(u"sort_notifications")
        self.sort_notifications.setGeometry(QRect(390, 120, 80, 24))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(470, 120, 121, 31))
        Main_Menu.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main_Menu)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 608, 33))
        Main_Menu.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(Main_Menu)
        self.statusBar.setObjectName(u"statusBar")
        Main_Menu.setStatusBar(self.statusBar)

        self.retranslateUi(Main_Menu)

        QMetaObject.connectSlotsByName(Main_Menu)
    # setupUi

    def retranslateUi(self, Main_Menu):
        Main_Menu.setWindowTitle(QCoreApplication.translate("Main_Menu", u"Main_Menu", None))
        self.PlantFolio_Icon.setText("")
        self.open_rooms.setText(QCoreApplication.translate("Main_Menu", u"Rooms", None))
        self.open_notifier.setText(QCoreApplication.translate("Main_Menu", u"Notifications", None))
        self.open_recommender.setText(QCoreApplication.translate("Main_Menu", u"Recommendations", None))
        self.water_all_button.setText(QCoreApplication.translate("Main_Menu", u"Water all", None))
        self.add_room_button.setText(QCoreApplication.translate("Main_Menu", u"Add Room", None))
        self.all_plants.setText(QCoreApplication.translate("Main_Menu", u"All Plants", None))
        self.sort_notifications.setItemText(0, QCoreApplication.translate("Main_Menu", u"day", None))
        self.sort_notifications.setItemText(1, QCoreApplication.translate("Main_Menu", u"type", None))
        self.sort_notifications.setItemText(2, QCoreApplication.translate("Main_Menu", u"weight", None))

        self.pushButton.setText(QCoreApplication.translate("Main_Menu", u"refresh notifications", None))
    # retranslateUi

