# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help_window.ui'
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
    QSizePolicy, QTextBrowser, QWidget)

class Ui_HelpWindow(object):
    def setupUi(self, HelpWindow):
        if not HelpWindow.objectName():
            HelpWindow.setObjectName(u"HelpWindow")
        HelpWindow.resize(450, 450)
        HelpWindow.setMinimumSize(QSize(450, 450))
        HelpWindow.setMaximumSize(QSize(450, 450))
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
        HelpWindow.setPalette(palette)
        self.frame = QLabel(HelpWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 401, 401))
        self.frame.setPixmap(QPixmap(u"../art/list_art.png"))
        self.frame.setScaledContents(True)
        self.text_display = QTextBrowser(HelpWindow)
        self.text_display.setObjectName(u"text_display")
        self.text_display.setGeometry(QRect(90, 60, 271, 301))
        self.select_box = QComboBox(HelpWindow)
        self.select_box.setObjectName(u"select_box")
        self.select_box.setGeometry(QRect(210, 20, 151, 24))
        self.info_label = QLabel(HelpWindow)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setGeometry(QRect(100, 20, 101, 16))
        font = QFont()
        font.setBold(True)
        self.info_label.setFont(font)
        self.nutrition_image = QLabel(HelpWindow)
        self.nutrition_image.setObjectName(u"nutrition_image")
        self.nutrition_image.setGeometry(QRect(130, 370, 81, 71))
        self.nutrition_image.setPixmap(QPixmap(u"../art/nutrition.png"))
        self.nutrition_image.setScaledContents(True)
        self.water_image = QLabel(HelpWindow)
        self.water_image.setObjectName(u"water_image")
        self.water_image.setGeometry(QRect(260, 370, 81, 71))
        self.water_image.setPixmap(QPixmap(u"../art/water.png"))
        self.water_image.setScaledContents(True)
        self.pot_image = QLabel(HelpWindow)
        self.pot_image.setObjectName(u"pot_image")
        self.pot_image.setGeometry(QRect(190, 380, 71, 61))
        self.pot_image.setPixmap(QPixmap(u"../art/empty_pot.png"))
        self.pot_image.setScaledContents(True)

        self.retranslateUi(HelpWindow)

        QMetaObject.connectSlotsByName(HelpWindow)
    # setupUi

    def retranslateUi(self, HelpWindow):
        HelpWindow.setWindowTitle(QCoreApplication.translate("HelpWindow", u"Dialog", None))
        self.frame.setText("")
        self.info_label.setText(QCoreApplication.translate("HelpWindow", u"Show info about:", None))
        self.nutrition_image.setText("")
        self.water_image.setText("")
        self.pot_image.setText("")
    # retranslateUi

