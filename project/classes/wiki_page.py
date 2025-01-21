from __future__ import annotations
from typing import TYPE_CHECKING
from PySide6.QtCore import Signal, QObject

from project.classes.public_methods import wiki_page

while TYPE_CHECKING:
    from project.ui_windows.recommendations_window import RecommendationsWindow
    from project.ui_windows.add_plant_window import AddPlantWindow

class WikiRequest(QObject):
    """
    This class represents a wikipedia API request for the recommendations window.
    It is run through a thread, checks if it is the most recently created request,
    sets the recommendationsWindow.page and emits the finished signal.
    """

    finished = Signal()

    def __init__(self, query: str, parent: RecommendationsWindow | AddPlantWindow) -> None:
        super().__init__()
        self.parent_window = parent
        self.query = query
        self.redundant = False

    def run(self) -> None:
        """
        Runs the wiki search and calls update_wiki_info
        """
        self.parent_window.semaphore.acquire()
        if self.redundant:
            self.finished.emit()
            return
        try:
            page = wiki_page(self.query)
            self.parent_window.page = page # type: ignore
        except Exception as e:
            raise e
        finally:
            self.finished.emit()
