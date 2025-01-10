# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_spot.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QLabel, QLineEdit,
    QSizePolicy, QSpinBox, QWidget)

class Ui_AddSpotWindow(object):
    def setupUi(self, AddSpotWindow):
        if not AddSpotWindow.objectName():
            AddSpotWindow.setObjectName(u"AddSpotWindow")
        AddSpotWindow.resize(305, 180)
        AddSpotWindow.setMinimumSize(QSize(305, 180))
        AddSpotWindow.setMaximumSize(QSize(305, 180))
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
        AddSpotWindow.setPalette(palette)
        self.confirm_spot = QDialogButtonBox(AddSpotWindow)
        self.confirm_spot.setObjectName(u"confirm_spot")
        self.confirm_spot.setGeometry(QRect(-30, 140, 261, 32))
        self.confirm_spot.setOrientation(Qt.Orientation.Horizontal)
        self.confirm_spot.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.Spot_Name_input = QLineEdit(AddSpotWindow)
        self.Spot_Name_input.setObjectName(u"Spot_Name_input")
        self.Spot_Name_input.setGeometry(QRect(110, 10, 113, 21))
        self.temperature_input = QDoubleSpinBox(AddSpotWindow)
        self.temperature_input.setObjectName(u"temperature_input")
        self.temperature_input.setGeometry(QRect(110, 70, 88, 23))
        self.sunlight_input = QComboBox(AddSpotWindow)
        self.sunlight_input.addItem("")
        self.sunlight_input.addItem("")
        self.sunlight_input.addItem("")
        self.sunlight_input.addItem("")
        self.sunlight_input.setObjectName(u"sunlight_input")
        self.sunlight_input.setGeometry(QRect(110, 100, 91, 24))
        self.label = QLabel(AddSpotWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 70, 101, 16))
        self.label_2 = QLabel(AddSpotWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 100, 61, 16))
        self.label_3 = QLabel(AddSpotWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 61, 16))
        self.label_4 = QLabel(AddSpotWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 40, 71, 16))
        self.humidity_input = QSpinBox(AddSpotWindow)
        self.humidity_input.setObjectName(u"humidity_input")
        self.humidity_input.setGeometry(QRect(110, 40, 88, 23))
        self.sun_image = QLabel(AddSpotWindow)
        self.sun_image.setObjectName(u"sun_image")
        self.sun_image.setGeometry(QRect(200, 20, 161, 131))
        self.sun_image.setPixmap(QPixmap(u"../art/full_sun.png"))
        self.sun_image.setScaledContents(True)

        self.retranslateUi(AddSpotWindow)
        self.confirm_spot.accepted.connect(AddSpotWindow.accept)
        self.confirm_spot.rejected.connect(AddSpotWindow.reject)

        QMetaObject.connectSlotsByName(AddSpotWindow)
    # setupUi

    def retranslateUi(self, AddSpotWindow):
        AddSpotWindow.setWindowTitle(QCoreApplication.translate("AddSpotWindow", u"Add Spot", None))
#if QT_CONFIG(tooltip)
        self.Spot_Name_input.setToolTip(QCoreApplication.translate("AddSpotWindow", u"<html><head/><body><p>Name of the spot. Must be unique.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.temperature_input.setToolTip(QCoreApplication.translate("AddSpotWindow", u"<html><head/><body><p>Temperature of the spot in degrees Celsius.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sunlight_input.setItemText(0, QCoreApplication.translate("AddSpotWindow", u"full shade", None))
        self.sunlight_input.setItemText(1, QCoreApplication.translate("AddSpotWindow", u"part shade", None))
        self.sunlight_input.setItemText(2, QCoreApplication.translate("AddSpotWindow", u"part sun", None))
        self.sunlight_input.setItemText(3, QCoreApplication.translate("AddSpotWindow", u"full sun", None))

#if QT_CONFIG(tooltip)
        self.sunlight_input.setToolTip(QCoreApplication.translate("AddSpotWindow", u"<html><head/><body><p>The amount of light that the spot receives</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("AddSpotWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Temperature (\u00b0C)</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("AddSpotWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Light level</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("AddSpotWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Spot name</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("AddSpotWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Humidity(%)</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.humidity_input.setToolTip(QCoreApplication.translate("AddSpotWindow", u"<html><head/><body><p>Humidity of the spot in percentage.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sun_image.setText("")
    # retranslateUi

