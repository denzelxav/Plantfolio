from __future__ import annotations

from typing import TYPE_CHECKING
from PySide6.QtCore import Slot, QThread, QSemaphore
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QDialog

from project.classes.wiki_page import WikiRequest
from project.ui.recommendations_ui import Ui_RecommendationsWindow
from project.classes.plant import plant_from_database

if TYPE_CHECKING:
    from project.classes.spot_notification import Spot
    from project.classes.userdata import UserData
    from project.classes.recommender import Recommender
    from project.classes.plant import Plant

class RecommendationsWindow(QDialog):
    """
    Shows plant recommendations for the user and info on those plants.
    """

    def __init__(self, recommender: Recommender, userdata: UserData) -> None:
        super().__init__()

        self.semaphore = QSemaphore(1)
        self.threads: list[tuple[QThread, WikiRequest]] = []
        self.ui = Ui_RecommendationsWindow()
        self.ui.setupUi(self)
        self.userdata = userdata
        self.recommender = recommender
        self.setWindowIcon(QIcon(":/Plantfolio_logo_small.png"))
        self.ui.frame.setPixmap(QPixmap(u":/list_art.png"))
        self.page = {"title": "No wiki page available", "description": "...", "image": QPixmap(":/plant_1_healthy.png")}

        self.recommendations = self.recommender.get_recommendations()
        for recommendation in self.recommendations:
            plant = plant_from_database(recommendation)
            self.ui.select_recommendation.addItem(plant.scientific_name)
        self.ui.select_recommendation.itemSelectionChanged.connect(self.selection_changed)

        self.ui.pet_tox_check.stateChanged.connect(self.pet_safe_change)

    @Slot()
    def selection_changed(self) -> None:
        """
        Runs a wikipedia search in another thread, which will call update_wiki_info when done
        """
        selection = self.ui.select_recommendation.selectedItems()
        if selection:
            if self.threads:
                self.threads[-1][1].redundant = True
            plant_name = selection[0].text()
            thread = QThread()
            wiki_search = WikiRequest(plant_name, self)
            wiki_search.moveToThread(thread)
            thread.started.connect(wiki_search.run)
            wiki_search.finished.connect(self.update_wiki_info)
            thread.finished.connect(thread.deleteLater)
            wiki_search.finished.connect(thread.quit)
            wiki_search.finished.connect(wiki_search.deleteLater)
            self.threads.append((thread, wiki_search))
            thread.start()


    @Slot()
    def update_wiki_info(self) -> None:
        """
        Runs after wiki search completes
        """
        self.ui.article_title.setText(self.page["title"])
        self.ui.article_title.setOpenExternalLinks(True)
        self.ui.article_description.setText(self.page["description"])
        plant_image: QPixmap = self.page["image"] # type: ignore
        im_width, im_height = self.ui.article_image.width(), self.ui.article_image.height()
        plant_image.scaled(im_width, im_height)
        self.ui.article_image.setPixmap(plant_image)
        self.semaphore.release()


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
        
