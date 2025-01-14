# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error_message.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)
import images_rc

class Ui_ErrorMessageWindow(object):
    def setupUi(self, ErrorMessageWindow):
        if not ErrorMessageWindow.objectName():
            ErrorMessageWindow.setObjectName(u"ErrorMessageWindow")
        ErrorMessageWindow.resize(376, 218)
        ErrorMessageWindow.setMinimumSize(QSize(376, 218))
        ErrorMessageWindow.setMaximumSize(QSize(376, 218))
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
        ErrorMessageWindow.setPalette(palette)
        self.error_message = QLabel(ErrorMessageWindow)
        self.error_message.setObjectName(u"error_message")
        self.error_message.setGeometry(QRect(10, 90, 351, 91))
        self.error_message.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setBold(False)
        self.error_message.setFont(font)
        self.error_message.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.close_message = QPushButton(ErrorMessageWindow)
        self.close_message.setObjectName(u"close_message")
        self.close_message.setGeometry(QRect(290, 190, 75, 24))
        self.label = QLabel(ErrorMessageWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 0, 31, 51))
        self.label.setPixmap(QPixmap(u":/exclamation_mark.png"))
        self.label.setScaledContents(True)
        self.error_type = QLabel(ErrorMessageWindow)
        self.error_type.setObjectName(u"error_type")
        self.error_type.setGeometry(QRect(8, 55, 361, 31))
        self.error_type.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(ErrorMessageWindow)

        QMetaObject.connectSlotsByName(ErrorMessageWindow)
    # setupUi

    def retranslateUi(self, ErrorMessageWindow):
        ErrorMessageWindow.setWindowTitle(QCoreApplication.translate("ErrorMessageWindow", u"Plantfolio Error", None))
        self.error_message.setText(QCoreApplication.translate("ErrorMessageWindow", u"Error message here", None))
        self.close_message.setText(QCoreApplication.translate("ErrorMessageWindow", u"Close", None))
        self.label.setText("")
        self.error_type.setText(QCoreApplication.translate("ErrorMessageWindow", u"Error type here", None))
    # retranslateUi

