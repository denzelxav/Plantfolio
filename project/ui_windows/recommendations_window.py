from __future__ import annotations

from typing import TYPE_CHECKING
from PySide6.QtCore import Slot, QThread, QSemaphore
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QDialog, QListWidgetItem

from project.classes.wiki_page import WikiRequest
from project.ui.recommendations_ui import Ui_RecommendationsWindow
from project.classes.plant import plant_from_database

if TYPE_CHECKING:
    from project.classes.userdata import UserData
    from project.classes.recommender import Recommender
    from project.ui_windows.main_menu import MainMenu

class RecommendationsWindow(QDialog):
    """
    Shows plant recommendations for the user and info on those plants.
    """

    def __init__(self, parent: MainMenu) -> None:
        super().__init__()

        self.ui = Ui_RecommendationsWindow()
        self.ui.setupUi(self)

        self.parent_window = parent
        self.semaphore = parent.semaphore
        self.userdata = self.parent_window.userdata

        self.threads: list[tuple[QThread, WikiRequest]] = []
        self.page = {"title": "No wiki page available", "description": "...", "image": QPixmap(":/plant_1_healthy.png")}
        self.recommender = self.parent_window.recommender

        self.setWindowIcon(QIcon(":/Plantfolio_logo_small.png"))
        self.ui.frame.setPixmap(QPixmap(u":/list_art.png"))

        self.recommendations = self.recommender.get_recommendations()
        for recommendation in self.recommendations:
            plant = plant_from_database(recommendation)
            self.ui.select_recommendation.addItem(plant.scientific_name)
        self.ui.select_recommendation.itemSelectionChanged.connect(self.selection_changed)

        self.ui.pet_tox_check.stateChanged.connect(self.pet_safe_change)
        self.parent_window.close_all.connect(self.close)
        # self.ui.Move_button.clicked.connect(self.move_plant_spot())
        self.refresh_change_spot()
        self.ui.Move_button.clicked.connect(self.move_plant_spot)

    def refresh_change_spot(self):
        self.ui.spot_changes.clear()
        dict_move_plant = self.recommender.move_plant()
        print(dict_move_plant)
        if dict_move_plant is None:
            self.ui.spot_changes.addItem('Every plant is in the optimal spot')
        else:
            for plant, empty_spot in dict_move_plant.items():
                input_text = (f"Move {plant.personal_name} from {plant.spot.spot_id} "
                              f"to this empty spot: {empty_spot.spot_id}")
                list_input = QListWidgetItem(input_text)
                list_input.setData(3, plant)  # Store Plant in role 0
                list_input.setData(4, empty_spot)  # Store Spot in role 1

                # Add the QListWidgetItem to the QListWidget
                self.ui.spot_changes.addItem(list_input)

    def move_plant_spot(self):
        selected_plant_to_move = self.ui.spot_changes.selectedItems()
        selected_item = selected_plant_to_move[0]
        if not selected_plant_to_move:
            return
        elif selected_item.text() == 'Every plant is in the optimal spot':
            return

        plant = selected_item.data(3)  # Retrieve Plant object
        empty_spot = selected_item.data(4)  # Retrieve Spot object
        self.recommender.change_plant_spot(plant, empty_spot)
        self.refresh_change_spot()
        self.parent_window.refresh_all_data()


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


        # self.spot_changes = self.recommender.move_plant_dict
        # for plant, empty_spot in self.recommender.move_plant_dict.items():
        #     input_text = f"Move {plant.personal_name} from {plant.spot} to this empty spot: {empty_spot.spot_id}"
        #     list_input = QListWidgetItem(input_text)
        #     list_input.setData(0, plant)
        #     list_input.setData(1, empty_spot)
        #     self.ui.spot_changes.addItem(list_input)

