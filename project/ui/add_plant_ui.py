# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_plant.ui'
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
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QSizePolicy, QWidget)

class Ui_AddPlantWindow(object):
    def setupUi(self, AddPlantWindow):
        if not AddPlantWindow.objectName():
            AddPlantWindow.setObjectName(u"AddPlantWindow")
        AddPlantWindow.resize(525, 300)
        AddPlantWindow.setMinimumSize(QSize(525, 300))
        AddPlantWindow.setMaximumSize(QSize(525, 300))
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
        AddPlantWindow.setPalette(palette)
        self.confirm_plant = QDialogButtonBox(AddPlantWindow)
        self.confirm_plant.setObjectName(u"confirm_plant")
        self.confirm_plant.setGeometry(QRect(430, 220, 81, 241))
        self.confirm_plant.setOrientation(Qt.Orientation.Vertical)
        self.confirm_plant.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.select_icon = QLabel(AddPlantWindow)
        self.select_icon.setObjectName(u"select_icon")
        self.select_icon.setGeometry(QRect(290, 60, 71, 16))
        font = QFont()
        font.setBold(True)
        self.select_icon.setFont(font)
        self.search_bar = QLineEdit(AddPlantWindow)
        self.search_bar.setObjectName(u"search_bar")
        self.search_bar.setGeometry(QRect(20, 50, 113, 21))
        self.label = QLabel(AddPlantWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 111, 16))
        self.label.setFont(font)
        self.name_input = QLineEdit(AddPlantWindow)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setGeometry(QRect(400, 80, 113, 21))
        self.choose_name = QLabel(AddPlantWindow)
        self.choose_name.setObjectName(u"choose_name")
        self.choose_name.setGeometry(QRect(400, 60, 91, 16))
        self.choose_name.setFont(font)
        self.all_plants_list = QListWidget(AddPlantWindow)
        self.all_plants_list.setObjectName(u"all_plants_list")
        self.all_plants_list.setGeometry(QRect(20, 80, 256, 192))
        self.icon_list = QListWidget(AddPlantWindow)
        self.icon_list.setObjectName(u"icon_list")
        self.icon_list.setGeometry(QRect(290, 80, 101, 192))
        self.icon_list.setIconSize(QSize(50, 50))

        self.retranslateUi(AddPlantWindow)
        self.confirm_plant.accepted.connect(AddPlantWindow.accept)
        self.confirm_plant.rejected.connect(AddPlantWindow.reject)

        QMetaObject.connectSlotsByName(AddPlantWindow)
    # setupUi

    def retranslateUi(self, AddPlantWindow):
        AddPlantWindow.setWindowTitle(QCoreApplication.translate("AddPlantWindow", u"Add plant", None))
        self.select_icon.setText(QCoreApplication.translate("AddPlantWindow", u"Select icon", None))
        self.label.setText(QCoreApplication.translate("AddPlantWindow", u"Search plant", None))
        self.choose_name.setText(QCoreApplication.translate("AddPlantWindow", u"Choose a name", None))
    # retranslateUi

