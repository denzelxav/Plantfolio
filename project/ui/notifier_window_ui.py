# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notifier_window.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_Notifier_windows(object):
    def setupUi(self, Notifier_windows):
        if not Notifier_windows.objectName():
            Notifier_windows.setObjectName(u"Notifier_windows")
        Notifier_windows.resize(445, 305)
        self.centralwidget = QWidget(Notifier_windows)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 40, 121, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 90, 49, 16))
        Notifier_windows.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Notifier_windows)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 445, 33))
        Notifier_windows.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Notifier_windows)
        self.statusbar.setObjectName(u"statusbar")
        Notifier_windows.setStatusBar(self.statusbar)

        self.retranslateUi(Notifier_windows)

        QMetaObject.connectSlotsByName(Notifier_windows)
    # setupUi

    def retranslateUi(self, Notifier_windows):
        Notifier_windows.setWindowTitle(QCoreApplication.translate("Notifier_windows", u"Notification", None))
        self.label.setText(QCoreApplication.translate("Notifier_windows", u"Notification type", None))
        self.label_2.setText(QCoreApplication.translate("Notifier_windows", u"corresponding plant", None))
    # retranslateUi

