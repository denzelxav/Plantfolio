# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notifier_windowAzocoJ.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QSizePolicy, QStatusBar, QWidget)

class Ui_Notifier_window(object):
    def setupUi(self, Notifier_window):
        if not Notifier_window.objectName():
            Notifier_window.setObjectName(u"Notifier_window")
        Notifier_window.resize(445, 325)
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
        Notifier_window.setPalette(palette)
        Notifier_window.setStyleSheet(u"")
        self.centralwidget = QWidget(Notifier_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.personal_id_plant = QLabel(self.centralwidget)
        self.personal_id_plant.setObjectName(u"personal_id_plant")
        self.personal_id_plant.setGeometry(QRect(70, 130, 161, 16))
        self.notification_type = QLabel(self.centralwidget)
        self.notification_type.setObjectName(u"notification_type")
        self.notification_type.setGeometry(QRect(70, 170, 121, 16))
        self.Notifications = QComboBox(self.centralwidget)
        self.Notifications.setObjectName(u"Notifications")
        self.Notifications.setGeometry(QRect(30, 20, 401, 41))
        self.weight = QLabel(self.centralwidget)
        self.weight.setObjectName(u"weight")
        self.weight.setGeometry(QRect(70, 210, 91, 16))
        self.original_due_date = QLabel(self.centralwidget)
        self.original_due_date.setObjectName(u"original_due_date")
        self.original_due_date.setGeometry(QRect(70, 250, 121, 16))
        self.Notification_info = QLabel(self.centralwidget)
        self.Notification_info.setObjectName(u"Notification_info")
        self.Notification_info.setGeometry(QRect(10, 80, 151, 21))
        self.Id_icon = QLabel(self.centralwidget)
        self.Id_icon.setObjectName(u"Id_icon")
        self.Id_icon.setGeometry(QRect(20, 130, 31, 21))
        self.Id_icon.setPixmap(QPixmap(u"../../../../Documents/A-Tu delft/Minor informatica/CS project/Nieuwe icons/Nieuwe icons/id.png"))
        self.Id_icon.setScaledContents(True)
        self.Type_notification_icon = QLabel(self.centralwidget)
        self.Type_notification_icon.setObjectName(u"Type_notification_icon")
        self.Type_notification_icon.setGeometry(QRect(10, 160, 41, 41))
        self.Type_notification_icon.setPixmap(QPixmap(u"../../../../Documents/A-Tu delft/Minor informatica/CS project/Nieuwe icons/Nieuwe icons/type_notification.png"))
        self.Type_notification_icon.setScaledContents(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 200, 41, 31))
        self.label.setPixmap(QPixmap(u"../../../../Documents/A-Tu delft/Minor informatica/CS project/Nieuwe icons/Nieuwe icons/weight.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 240, 41, 41))
        self.label_2.setPixmap(QPixmap(u"../../../../Documents/A-Tu delft/Minor informatica/CS project/Nieuwe icons/Nieuwe icons/date.png"))
        self.label_2.setScaledContents(True)
        Notifier_window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Notifier_window)
        self.statusbar.setObjectName(u"statusbar")
        Notifier_window.setStatusBar(self.statusbar)

        self.retranslateUi(Notifier_window)

        QMetaObject.connectSlotsByName(Notifier_window)
    # setupUi

    def retranslateUi(self, Notifier_window):
        Notifier_window.setWindowTitle(QCoreApplication.translate("Notifier_window", u"Notification", None))
        self.personal_id_plant.setText(QCoreApplication.translate("Notifier_window", u"personal_id_plant", None))
        self.notification_type.setText(QCoreApplication.translate("Notifier_window", u"notificication_type", None))
        self.weight.setText(QCoreApplication.translate("Notifier_window", u"weight", None))
        self.original_due_date.setText(QCoreApplication.translate("Notifier_window", u"original_due_date", None))
#if QT_CONFIG(tooltip)
        self.Notification_info.setToolTip(QCoreApplication.translate("Notifier_window", u"<html><head/><body><p><span style=\" font-weight:700;\">Notification info</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Notification_info.setText(QCoreApplication.translate("Notifier_window", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Notification info</span></p></body></html>", None))
        self.Id_icon.setText("")
        self.Type_notification_icon.setText("")
        self.label.setText("")
        self.label_2.setText("")
    # retranslateUi




