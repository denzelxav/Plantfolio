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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QHeaderView, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_AllPlantsWindow(object):
    def setupUi(self, AllPlantsWindow):
        if not AllPlantsWindow.objectName():
            AllPlantsWindow.setObjectName(u"AllPlantsWindow")
        AllPlantsWindow.resize(550, 350)
        AllPlantsWindow.setMinimumSize(QSize(423, 350))
        AllPlantsWindow.setMaximumSize(QSize(550, 350))
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
        self.select_plant.setGeometry(QRect(10, 90, 531, 81))
        self.select_plant.setIconSize(QSize(64, 64))
        self.select_label = QLabel(AllPlantsWindow)
        self.select_label.setObjectName(u"select_label")
        self.select_label.setGeometry(QRect(10, 70, 151, 16))
        font = QFont()
        font.setBold(True)
        self.select_label.setFont(font)
        self.sort_by = QComboBox(AllPlantsWindow)
        self.sort_by.setObjectName(u"sort_by")
        self.sort_by.setGeometry(QRect(340, 60, 121, 24))
        self.cancel_button = QPushButton(AllPlantsWindow)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(470, 10, 75, 24))
        self.select_plant_button = QPushButton(AllPlantsWindow)
        self.select_plant_button.setObjectName(u"select_plant_button")
        self.select_plant_button.setGeometry(QRect(90, 10, 75, 24))
        self.water_all_button = QPushButton(AllPlantsWindow)
        self.water_all_button.setObjectName(u"water_all_button")
        self.water_all_button.setGeometry(QRect(10, 10, 75, 24))
        self.sort_by_label = QLabel(AllPlantsWindow)
        self.sort_by_label.setObjectName(u"sort_by_label")
        self.sort_by_label.setGeometry(QRect(290, 60, 151, 16))
        self.sort_by_label.setFont(font)
        self.reverse_button = QCheckBox(AllPlantsWindow)
        self.reverse_button.setObjectName(u"reverse_button")
        self.reverse_button.setGeometry(QRect(470, 60, 78, 20))
        self.plant_table = QTableWidget(AllPlantsWindow)
        self.plant_table.setObjectName(u"plant_table")
        self.plant_table.setGeometry(QRect(10, 180, 531, 151))

        self.retranslateUi(AllPlantsWindow)

        QMetaObject.connectSlotsByName(AllPlantsWindow)
    # setupUi

    def retranslateUi(self, AllPlantsWindow):
        AllPlantsWindow.setWindowTitle(QCoreApplication.translate("AllPlantsWindow", u"All plants", None))
        self.select_label.setText(QCoreApplication.translate("AllPlantsWindow", u"All your plants:", None))
        self.cancel_button.setText(QCoreApplication.translate("AllPlantsWindow", u"Cancel", None))
        self.select_plant_button.setText(QCoreApplication.translate("AllPlantsWindow", u"View plant", None))
        self.water_all_button.setText(QCoreApplication.translate("AllPlantsWindow", u"Water all", None))
        self.sort_by_label.setText(QCoreApplication.translate("AllPlantsWindow", u"Sort by:", None))
        self.reverse_button.setText(QCoreApplication.translate("AllPlantsWindow", u"Reverse", None))
    # retranslateUi

