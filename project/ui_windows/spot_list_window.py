from __future__ import annotations

from PySide6.QtWidgets import QListWidgetItem, QDialog
from PySide6.QtGui import QPixmap, QIcon

from project.ui.spot_list import Ui_SpotListWindow
from typing import TYPE_CHECKING

while TYPE_CHECKING:
    from project.classes.plant import Plant
    from project.ui_windows.plant_view_window import PlantViewWindow

class SpotListWindow(QDialog):
    def __init__(self, parent: PlantViewWindow):
        super().__init__()
        self.ui = Ui_SpotListWindow()
        self.ui.setupUi(self)
        self.plant_to_move = parent.plant # type: ignore
        self.parent_window: PlantViewWindow = parent
        self.userdata = parent.userdata
        self.main_menu = parent.main_menu # type: ignore

        self.ui.frame.setPixmap(QPixmap(u":/list_art.png"))
        self.setWindowIcon(QIcon(":/Plantfolio_logo_small.png"))

        for room in self.userdata.rooms.values():
            for spot in room:
                if not spot.assigned_plant:
                    spot_item = QListWidgetItem(spot.spot_id)
                    spot_item.setData(3, spot)
                    self.ui.spot_list.addItem(spot_item)
        self.ui.confirm_spot.accepted.connect(self.accept)
        self.ui.confirm_spot.rejected.connect(self.reject)
        self.main_menu.close_all.connect(self.close)

    def accept(self):
        selection = self.ui.spot_list.selectedItems()
        if len(selection) > 0:
            spot = selection[0].data(3)
            self.plant_to_move.change_spot(spot)
            self.main_menu.refresh_all_data()
            super().accept()
