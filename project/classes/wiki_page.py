from __future__ import annotations
from typing import TYPE_CHECKING
from PySide6.QtCore import Signal, QObject

from project.classes.public_methods import wiki_page
while TYPE_CHECKING:
    from project.ui_windows.recommendations_window import RecommendationsWindow

class WikiRequest(QObject):
    """
    This class represents a wikipedia API request for the recommendations window.
    It is run through a thread, checks if it is the most recently created request,
    sets the recommendationsWindow.page and emits the finished signal.
    """

    finished = Signal()

    def __init__(self, query: str, parent: RecommendationsWindow) -> None:
        super().__init__()
        self.parent_window = parent
        self.query = query
        self.redundant = False
        print(f"thread created for {self.query}")

    def run(self) -> None:
        """
        Runs the wiki search and calls update_wiki_info
        """
        self.parent_window.semaphore.acquire()
        if self.redundant:
            self.finished.emit()
            return
        try:
            print(f"wiki search for {self.query} is being run")
            page = wiki_page(self.query)
            print(f"wiki search for {self.query} is done")
            self.parent_window.page = page # type: ignore
        except Exception as e:
            print(f"Error: {e}")
            raise e
        finally:
            self.finished.emit()
