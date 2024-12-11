# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menu.ui'
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

class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        if not MainMenu.objectName():
            MainMenu.setObjectName(u"MainMenu")
        MainMenu.resize(608, 426)
        MainMenu.setMinimumSize(QSize(608, 426))
        MainMenu.setMaximumSize(QSize(608, 426))
        self.centralwidget = QWidget(MainMenu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.PlantFolio_Icon = QLabel(self.centralwidget)
        self.PlantFolio_Icon.setObjectName(u"PlantFolio_Icon")
        self.PlantFolio_Icon.setGeometry(QRect(0, -10, 381, 131))
        self.PlantFolio_Icon.setPixmap(QPixmap(u"../art/Plantfolio_logo.png"))
        self.PlantFolio_Icon.setScaledContents(True)
        self.open_room = QPushButton(self.centralwidget)
        self.open_room.setObjectName(u"open_room")
        self.open_room.setGeometry(QRect(40, 350, 75, 24))
        self.open_notifier = QPushButton(self.centralwidget)
        self.open_notifier.setObjectName(u"open_notifier")
        self.open_notifier.setGeometry(QRect(350, 350, 75, 24))
        self.Notification_list = QListWidget(self.centralwidget)
        self.Notification_list.setObjectName(u"Notification_list")
        self.Notification_list.setGeometry(QRect(340, 150, 256, 192))
        self.open_recommender = QPushButton(self.centralwidget)
        self.open_recommender.setObjectName(u"open_recommender")
        self.open_recommender.setGeometry(QRect(450, 50, 111, 31))
        self.room_list = QListWidget(self.centralwidget)
        self.room_list.setObjectName(u"room_list")
        self.room_list.setGeometry(QRect(30, 151, 201, 181))
        self.water_all = QPushButton(self.centralwidget)
        self.water_all.setObjectName(u"water_all")
        self.water_all.setGeometry(QRect(240, 120, 75, 24))
        self.add_room = QPushButton(self.centralwidget)
        self.add_room.setObjectName(u"add_room")
        self.add_room.setGeometry(QRect(120, 350, 75, 24))
        self.all_plants = QPushButton(self.centralwidget)
        self.all_plants.setObjectName(u"all_plants")
        self.all_plants.setGeometry(QRect(240, 150, 75, 24))
        self.sort_notifications_by = QComboBox(self.centralwidget)
        self.sort_notifications_by.addItem("")
        self.sort_notifications_by.addItem("")
        self.sort_notifications_by.addItem("")
        self.sort_notifications_by.setObjectName(u"sort_notifications_by")
        self.sort_notifications_by.setGeometry(QRect(390, 120, 80, 24))
        self.refresh_notifications = QPushButton(self.centralwidget)
        self.refresh_notifications.setObjectName(u"refresh_notifications")
        self.refresh_notifications.setGeometry(QRect(470, 120, 121, 31))
        MainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainMenu)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 608, 33))
        MainMenu.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainMenu)
        self.statusBar.setObjectName(u"statusBar")
        MainMenu.setStatusBar(self.statusBar)

        self.retranslateUi(MainMenu)

        QMetaObject.connectSlotsByName(MainMenu)
    # setupUi

    def retranslateUi(self, MainMenu):
        MainMenu.setWindowTitle(QCoreApplication.translate("MainMenu", u"Plantfolio", None))
        self.PlantFolio_Icon.setText("")
        self.open_room.setText(QCoreApplication.translate("MainMenu", u"Open Room", None))
        self.open_notifier.setText(QCoreApplication.translate("MainMenu", u"Notifications", None))
        self.open_recommender.setText(QCoreApplication.translate("MainMenu", u"Recommendations", None))
        self.water_all.setText(QCoreApplication.translate("MainMenu", u"Water all", None))
        self.add_room.setText(QCoreApplication.translate("MainMenu", u"Add Room", None))
        self.all_plants.setText(QCoreApplication.translate("MainMenu", u"All Plants", None))
        self.sort_notifications_by.setItemText(0, QCoreApplication.translate("MainMenu", u"day", None))
        self.sort_notifications_by.setItemText(1, QCoreApplication.translate("MainMenu", u"type", None))
        self.sort_notifications_by.setItemText(2, QCoreApplication.translate("MainMenu", u"weight", None))

        self.refresh_notifications.setText(QCoreApplication.translate("MainMenu", u"refresh notifications", None))
    # retranslateUi

