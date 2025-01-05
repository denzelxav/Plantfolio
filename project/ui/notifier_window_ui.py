# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notifier_windowtgapcq.ui'
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
        Notifier_window.resize(445, 305)
        Notifier_window.setStyleSheet(u"background-color: rgb(151, 255, 135);")
        self.centralwidget = QWidget(Notifier_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.personal_id_plant = QLabel(self.centralwidget)
        self.personal_id_plant.setObjectName(u"personal_id_plant")
        self.personal_id_plant.setGeometry(QRect(40, 80, 161, 16))
        self.notification_type = QLabel(self.centralwidget)
        self.notification_type.setObjectName(u"notification_type")
        self.notification_type.setGeometry(QRect(40, 110, 121, 16))
        self.Notifications = QComboBox(self.centralwidget)
        self.Notifications.setObjectName(u"Notifications")
        self.Notifications.setGeometry(QRect(30, 20, 401, 41))
        self.weight = QLabel(self.centralwidget)
        self.weight.setObjectName(u"weight")
        self.weight.setGeometry(QRect(40, 140, 91, 16))
        self.original_due_date = QLabel(self.centralwidget)
        self.original_due_date.setObjectName(u"original_due_date")
        self.original_due_date.setGeometry(QRect(40, 170, 121, 16))
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
    # retranslateUi


