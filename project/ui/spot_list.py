# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spot_list.ui'
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
    QLabel, QListWidget, QListWidgetItem, QSizePolicy,
    QWidget)

class Ui_SpotListWindow(object):
    def setupUi(self, SpotListWindow):
        if not SpotListWindow.objectName():
            SpotListWindow.setObjectName(u"SpotListWindow")
        SpotListWindow.resize(349, 277)
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
        SpotListWindow.setPalette(palette)
        self.confirm_spot = QDialogButtonBox(SpotListWindow)
        self.confirm_spot.setObjectName(u"confirm_spot")
        self.confirm_spot.setGeometry(QRect(260, 10, 81, 241))
        self.confirm_spot.setOrientation(Qt.Orientation.Vertical)
        self.confirm_spot.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.spot_list = QListWidget(SpotListWindow)
        self.spot_list.setObjectName(u"spot_list")
        self.spot_list.setGeometry(QRect(50, 40, 191, 201))
        self.label = QLabel(SpotListWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 10, 241, 16))
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.frame = QLabel(SpotListWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 271, 261))
        self.frame.setPixmap(QPixmap(u"../art/list_art.png"))
        self.frame.setScaledContents(True)
        self.frame.raise_()
        self.confirm_spot.raise_()
        self.spot_list.raise_()
        self.label.raise_()

        self.retranslateUi(SpotListWindow)
        self.confirm_spot.accepted.connect(SpotListWindow.accept)
        self.confirm_spot.rejected.connect(SpotListWindow.reject)

        QMetaObject.connectSlotsByName(SpotListWindow)
    # setupUi

    def retranslateUi(self, SpotListWindow):
        SpotListWindow.setWindowTitle(QCoreApplication.translate("SpotListWindow", u"Move plant to spot", None))
        self.label.setText(QCoreApplication.translate("SpotListWindow", u"Select spot to move plant to:", None))
        self.frame.setText("")
    # retranslateUi

