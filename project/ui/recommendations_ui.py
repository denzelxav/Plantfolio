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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QWidget)

class Ui_RecommendationsWindow(object):
    def setupUi(self, RecommendationsWindow):
        if not RecommendationsWindow.objectName():
            RecommendationsWindow.setObjectName(u"RecommendationsWindow")
        RecommendationsWindow.resize(403, 324)
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
        self.select_recommendation.setGeometry(QRect(10, 40, 256, 271))
        self.Recommendations_text = QLabel(RecommendationsWindow)
        self.Recommendations_text.setObjectName(u"Recommendations_text")
        self.Recommendations_text.setGeometry(QRect(10, 20, 151, 16))
        font = QFont()
        font.setBold(True)
        self.Recommendations_text.setFont(font)
        self.cancel_recommendations = QPushButton(RecommendationsWindow)
        self.cancel_recommendations.setObjectName(u"cancel_recommendations")
        self.cancel_recommendations.setGeometry(QRect(320, 10, 75, 24))
        self.refresh_recommendation_button = QPushButton(RecommendationsWindow)
        self.refresh_recommendation_button.setObjectName(u"refresh_recommendation_button")
        self.refresh_recommendation_button.setGeometry(QRect(320, 40, 75, 24))
        self.image_recommender = QLabel(RecommendationsWindow)
        self.image_recommender.setObjectName(u"image_recommender")
        self.image_recommender.setGeometry(QRect(270, 120, 131, 161))
        self.image_recommender.setTextFormat(Qt.TextFormat.RichText)
        self.image_recommender.setPixmap(QPixmap(u"../art/all plants/plant_1_healthy.png"))
        self.image_recommender.setScaledContents(True)

        self.retranslateUi(RecommendationsWindow)
        self.refresh_recommendation_button.clicked.connect(RecommendationsWindow.update)
        self.cancel_recommendations.clicked.connect(RecommendationsWindow.close)

        QMetaObject.connectSlotsByName(RecommendationsWindow)
    # setupUi

    def retranslateUi(self, RecommendationsWindow):
        RecommendationsWindow.setWindowTitle(QCoreApplication.translate("RecommendationsWindow", u"Recommendations", None))
        self.Recommendations_text.setText(QCoreApplication.translate("RecommendationsWindow", u"Recommended plants", None))
        self.cancel_recommendations.setText(QCoreApplication.translate("RecommendationsWindow", u"Cancel", None))
        self.refresh_recommendation_button.setText(QCoreApplication.translate("RecommendationsWindow", u"Refresh", None))
        self.image_recommender.setText("")
    # retranslateUi

