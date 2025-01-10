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
        self.setWindowIcon(QIcon(":/Plantfolio_logo_small.png"))
        self.ui.frame.setPixmap(QPixmap(u":/list_art.png"))

        self.recommendations = self.recommender.get_recommendations()
        for recommendation in self.recommendations:
            plant = plant_from_database(recommendation)
            self.ui.select_recommendation.addItem(plant.scientific_name)

        self.ui.pet_tox_check.stateChanged.connect(self.pet_safe_change)

    @Slot()
    def pet_safe_change(self, state):
        if state == 2:  # Qt.Checked is 2
            self.userdata.pet_toxicity = True
        else:
            self.userdata.pet_toxicity = False

        self.recommender.userdata = self.userdata
        self.recommender.set_values()
        self.recommendations = self.recommender.get_recommendations()

        self.ui.select_recommendation.clear()
        for recommendation in self.recommendations:
            plant = plant_from_database(recommendation)
            self.ui.select_recommendation.addItem(plant.scientific_name)
        
