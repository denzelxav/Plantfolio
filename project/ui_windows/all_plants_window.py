from __future__ import annotations
from typing import TYPE_CHECKING
from PySide6.QtCore import Slot, QSize
from PySide6.QtGui import QIcon
import os
import sys

from PySide6 import QtCore, QtGui
from PySide6.QtCore import Slot, QSize, QPoint
from PySide6.QtGui import QPixmap, QIcon, QPainterPath
from PySide6.QtWidgets import QDialog, QTableWidgetItem, QAbstractItemView

import images_rc
from project.classes.enums import Health
from project.classes.userdata import UserData
from project.ui.all_plants import Ui_AllPlantsWindow
from project.ui_windows.plant_view_window import PlantViewWindow
from project.classes.plant import Plant
while TYPE_CHECKING:
    from project.ui_windows.main_menu import MainMenu


class AllPlantsWindow(QDialog):

    """
    Window showing an overview of all the plants the user owns.
    These can be sorted on different attributes.
    """

    def __init__(self, parent: MainMenu):
        super().__init__()
        self.userdata = parent.userdata
        self.parent_window = parent
        self.semaphore = parent.semaphore
        self.ui = Ui_AllPlantsWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/Plantfolio_logo_small.png"))

        self.setup_table()
        self.refresh_table()

        # Buttons
        self.ui.cancel_button.clicked.connect(self.reject)
        self.ui.select_plant_button.clicked.connect(self.select_plant)
        self.ui.water_all_button.clicked.connect(self.water_all)
        self.ui.plant_table.itemDoubleClicked.connect(self.select_plant)

        # Combobox
        self.ui.sort_by.addItem('ID')
        self.ui.sort_by.addItem('Name')
        self.ui.sort_by.addItem('Room')
        self.ui.sort_by.addItem('Species')
        self.ui.sort_by.addItem('Last watered')
        self.ui.sort_by.addItem('Current tasks')

        # Some table settings
        self.ui.plant_table.setSelectionBehavior(QAbstractItemView.SelectRows) # type: ignore
        self.ui.sort_by.currentIndexChanged.connect(self.sort_table)
        self.ui.reverse_button.stateChanged.connect(self.sort_table)

    @Slot()
    def select_plant(self) -> None:
        """
        Opens the plant view window for a selected plant
        """
        selection = self.ui.plant_table.selectedItems()
        if not selection:
            return
        selected_plant = selection[0].data(3)
        if selected_plant.spot:
            selected_spot = selected_plant.spot
            self.plant_view = PlantViewWindow(selected_spot, self)
            self.plant_view.show()

    @Slot()
    def sort_table(self) -> None:
        """
        Sorts the table of plants on a specific attribute
        """
        reverse = self.ui.reverse_button.isChecked()
        crit = self.ui.sort_by.currentText()
        if crit == 'ID':
            self.userdata.plants.sort(key=lambda plant: plant.personal_id, reverse=reverse)
        elif crit == 'Name':
            self.userdata.plants.sort(key=lambda plant: plant.personal_name.lower(), reverse=reverse)
        elif crit == 'Room':
            self.userdata.plants.sort(key=lambda plant: self.get_room(plant).lower(), reverse=reverse)
        elif crit == 'Species':
            self.userdata.plants.sort(key=lambda plant: plant.scientific_name.lower(), reverse=reverse)
        elif crit == 'Last watered':
            self.userdata.plants.sort(key=lambda plant: plant.watered[-1], reverse=reverse)
        elif crit == 'Current tasks':
            self.userdata.plants = self.userdata.sort_plants('current_task', reverse)
        self.refresh_table()

    @Slot()
    def water_all(self) -> None:
        """
        Waters all plants and refreshes table
        """
        self.userdata.water_all()
        self.refresh_table()

    def get_plant(self, plant_id: int) -> Plant:
        """
        Retrieves the plant object based on the ID
        """
        for plant in self.userdata.plants:
            if plant.personal_id == plant_id:
                return plant
        raise ValueError(f"Plant {plant_id} does not exist")

    def get_room(self, plant: Plant) -> str:
        """
        Retrieves the room a plant is located in
        """
        for room in self.userdata.rooms:
            if plant.spot in self.userdata.rooms[room]:
                return room
        raise IndexError(f"{plant} does not have a room")

    def setup_table(self) -> None:
        """
        Sets up the table of plants with the correct headers and column widths
        """
        self.ui.plant_table.setColumnCount(6)
        self.ui.plant_table.setHorizontalHeaderLabels([ 'Name', 'ID', 'Room', 'Species', 'Last Watered', 'Current Tasks'])
        self.ui.plant_table.setColumnWidth(0, 130)
        self.ui.plant_table.setColumnWidth(1, 20)
        self.ui.plant_table.setColumnWidth(2, 70)
        self.ui.plant_table.setColumnWidth(3, 110)
        self.ui.plant_table.setColumnWidth(4, 84)
        self.ui.plant_table.setColumnWidth(5, 90)
        self.ui.plant_table.verticalHeader().setVisible(False)
        self.ui.plant_table.setEditTriggers(QAbstractItemView.NoEditTriggers) # type: ignore


    def refresh_table(self) -> None:
        """
        Refreshes the table of plants
        """
        self.ui.plant_table.setIconSize(QSize(64, 64))
        self.ui.plant_table.setRowCount(0)  # Clear the table
        for plant in self.userdata.plants:
            row = self.ui.plant_table.rowCount()
            self.ui.plant_table.insertRow(row)
            self.ui.plant_table.setRowHeight(row, 80)

            # Add items to the table
            name_item = QTableWidgetItem(plant.personal_name)
            name_item.setData(3, plant)
            icon_path = self.get_icon_path(plant)
            if plant.custom_icon:
                icon = QIcon(self.add_health_icon(QPixmap(icon_path), plant.health))
            else:
                icon = QIcon(icon_path)
            name_item.setIcon(icon)  # Set the icon for the name column
            self.ui.plant_table.setItem(row, 0, name_item)

            self.ui.plant_table.setItem(row, 1, QTableWidgetItem(str(plant.personal_id)))
            self.ui.plant_table.setItem(row, 2, QTableWidgetItem(self.get_room(plant)))
            self.ui.plant_table.setItem(row, 3, QTableWidgetItem(plant.scientific_name))
            self.ui.plant_table.setItem(row, 4, QTableWidgetItem(plant.watered[-1].date().isoformat()))
            self.ui.plant_table.setItem(row, 5, QTableWidgetItem(", ".join(plant.current_tasks)))


    def get_icon_path(self, plant: Plant) -> str:
        """
        Returns relative path to the correct icon for the given plant.
        """

        if plant.custom_icon:
            if getattr(sys, 'frozen', False):
                appdata = os.getenv('APPDATA')
                if appdata:
                    image_path = os.path.join(appdata, "Plantfolio", "custom_pictures",
                                              plant.custom_icon)
                else:
                    raise FileNotFoundError("Could not find %appdata%")
            else:
                image_path = os.path.join("project", "custom_pictures", plant.custom_icon)
        else:
            image_path = f":/{plant.icon_type}_{plant.health.value}.png"
        if os.path.exists(image_path):
            return image_path
        plant.custom_icon = None
        return f":/{plant.icon_type}_{plant.health.value}.png"

    def add_health_icon(self, image: QPixmap, health: Health) -> QPixmap:
        """
        pastes given health smiley on the given pixmap and returns the result as a pixmap
        """
        health_icon = QPixmap(f":/smiley_{health.value}.png").scaled(image.size() * 0.4)
        radius = 600

        path = QPainterPath()
        r = QtCore.QRectF()
        r.setSize(radius * QtCore.QSizeF(1,1)) # type: ignore
        r.moveBottomRight(image.rect().bottomRight())
        path.addEllipse(r)
        painter = QtGui.QPainter(image)
        painter.setRenderHints(
            QtGui.QPainter.Antialiasing | QtGui.QPainter.SmoothPixmapTransform  # type: ignore
        )
        painter.setClipPath(path, QtCore.Qt.IntersectClip)  # type: ignore
        point = image.rect().bottomRight() * 0.5

        painter.drawPixmap(point , health_icon)
        painter.end()
        return image