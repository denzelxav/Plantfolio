from __future__ import annotations
from typing import TYPE_CHECKING
import datetime
from PySide6.QtCore import Slot, QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QMainWindow, QDialog, QListWidgetItem

from project.ui.plant_view import Ui_PlantViewWindow
from project.ui.recommendations_ui import Ui_RecommendationsWindow
from project.classes.plant import plant_from_database

if TYPE_CHECKING:
    from project.classes.spot_notification import Spot
    from project.classes.userdata import UserData
    from project.classes.recommender import Recommender
    from project.classes.plant import Plant

class RecommendationsWindow(QDialog):

    def __init__(self, recommender: Recommender, userdata: UserData):
        super().__init__()
        self.ui = Ui_RecommendationsWindow()
        self.ui.setupUi(self)
        self.userdata = userdata
        self.recommender = recommender
        self.setWindowIcon(QIcon("./project/art/Plantfolio_logo_small.png"))
        self.ui.image_recommender.setPixmap(QPixmap(u"./project/art/plant_1_healthy.png"))

        self.recommendations = self.recommender.get_recommendations()
        print(self.recommendations)
        for recommendation in self.recommendations:
            plant = plant_from_database(recommendation)
            self.ui.select_recommendation.addItem(plant.scientific_name)



