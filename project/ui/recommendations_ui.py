# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recommendations.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_RecommendationsWindow(object):
    def setupUi(self, RecommendationsWindow):
        if not RecommendationsWindow.objectName():
            RecommendationsWindow.setObjectName(u"RecommendationsWindow")
        RecommendationsWindow.resize(330, 385)
        RecommendationsWindow.setMinimumSize(QSize(330, 385))
        RecommendationsWindow.setMaximumSize(QSize(330, 385))
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
        RecommendationsWindow.setPalette(palette)
        self.select_recommendation = QListWidget(RecommendationsWindow)
        self.select_recommendation.setObjectName(u"select_recommendation")
        self.select_recommendation.setGeometry(QRect(50, 40, 211, 181))
        self.Recommendations_text = QLabel(RecommendationsWindow)
        self.Recommendations_text.setObjectName(u"Recommendations_text")
        self.Recommendations_text.setGeometry(QRect(60, 10, 171, 16))
        font = QFont()
        font.setBold(True)
        self.Recommendations_text.setFont(font)
        self.cancel_recommendations = QPushButton(RecommendationsWindow)
        self.cancel_recommendations.setObjectName(u"cancel_recommendations")
        self.cancel_recommendations.setGeometry(QRect(120, 360, 75, 24))
        self.frame = QLabel(RecommendationsWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, 10, 311, 241))
        self.frame.setPixmap(QPixmap(u"../art/list_art.png"))
        self.frame.setScaledContents(True)
        self.pet_tox_check = QCheckBox(RecommendationsWindow)
        self.pet_tox_check.setObjectName(u"pet_tox_check")
        self.pet_tox_check.setGeometry(QRect(70, 230, 161, 20))
        self.label = QLabel(RecommendationsWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 251, 181, 20))
        self.spot_changes = QListWidget(RecommendationsWindow)
        self.spot_changes.setObjectName(u"spot_changes")
        self.spot_changes.setGeometry(QRect(60, 270, 211, 71))
        self.frame2 = QLabel(RecommendationsWindow)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setGeometry(QRect(0, 260, 301, 91))
        self.frame2.setPixmap(QPixmap(u"../art/list_art.png"))
        self.frame2.setScaledContents(True)
        self.Move_button = QPushButton(RecommendationsWindow)
        self.Move_button.setObjectName(u"Move_button")
        self.Move_button.setGeometry(QRect(120, 340, 75, 21))
        self.frame2.raise_()
        self.frame.raise_()
        self.select_recommendation.raise_()
        self.Recommendations_text.raise_()
        self.cancel_recommendations.raise_()
        self.pet_tox_check.raise_()
        self.label.raise_()
        self.spot_changes.raise_()
        self.Move_button.raise_()

        self.retranslateUi(RecommendationsWindow)
        self.cancel_recommendations.clicked.connect(RecommendationsWindow.close)

        QMetaObject.connectSlotsByName(RecommendationsWindow)
    # setupUi

    def retranslateUi(self, RecommendationsWindow):
        RecommendationsWindow.setWindowTitle(QCoreApplication.translate("RecommendationsWindow", u"Recommendations", None))
        self.Recommendations_text.setText(QCoreApplication.translate("RecommendationsWindow", u"Recommended plants for you", None))
        self.cancel_recommendations.setText(QCoreApplication.translate("RecommendationsWindow", u"Cancel", None))
        self.frame.setText("")
        self.pet_tox_check.setText(QCoreApplication.translate("RecommendationsWindow", u"Only show pet-safe plants", None))
        self.label.setText(QCoreApplication.translate("RecommendationsWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Recommended spot changes</span></p></body></html>", None))
        self.frame2.setText("")
        self.Move_button.setText(QCoreApplication.translate("RecommendationsWindow", u"Move", None))
    # retranslateUi

