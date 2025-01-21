from __future__ import annotations
from typing import TYPE_CHECKING
from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QDialog, QMainWindow, QListWidgetItem
import images_rc
from project.classes.exceptions import NameTakenError, EmptyNameError

from project.ui_windows.error_message_window import ErrorMessageWindow
from project.ui.help_window import Ui_HelpWindow
while TYPE_CHECKING:
    from project.ui_windows.main_menu import MainMenu

water_text = (
    'The watering needs of plants differ, and it is recommended to read up on the specific watering needs of your plant. ' 
    'This application will also provide basic information on this when you view a plant. It is good practice to always check '
    'the soil of a plant before watering by sticking your finger in it. Most houseplants will prefer the top layer of soil ' 
    'to be dry before getting new water, but some need to be kept moist at all times. To prevent root rot, it is a good idea ' 
    'to have a pot with drainage holes, this prevents water from piling up at the bottom of the pot. Alternatively you can add '
    'a layer of clay pellets at the bottom of the pot, or use both.'
    )

repot_text = (
    'Repotting generally needs to happen every 1-2 years. If your current pot has drainage holes in the bottom you can tell '
    'that a plant needs to be repotted since the roots will be visible and growing through the holes (although this is not a '
    '100% certain way of telling). Beware of repotting too often, as the plant needs time to settle into a new pot.'
    '\n\n'
    'To repot your plant, you need to get a pot that has a radius about 2 cm larger than the current one. It’s always good to '
    'get a pot with drainage holes, as it prevents the roots from rotting. If you are using clay pellets, you can start by adding '
    'a layer of those to the pot. Put a small amount of soil into the new pot at the bottom and around the edges, so that there '
    'is a hole in the middle that the plant can fit into. Remove the plant from the old pot, and if necessary shake out the '
    'roots a bit so they’re not clumped together. Place the plant into the new pot, and add soil as needed. You have now '
    'successfully repotted your plant!'
    )

nutrition_text = (
    'Since the soil in pots cannot get nutrition from the environment, you will periodically have to provide nutrition to your '
    'plant. Generally this nutrition can be bought at supermarkets and plant stores and comes as a liquid in bottles. Most will '
    'have instructions on the bottle but generally plants will need nutrition about once a month and you can give it by mixing '
    'a splash to a liter of water which you then water the plant with.'
    )

class HelpWindow(QDialog):
    """
    Window for adding a new room.
    It takes the parent_window as an argument so it can refer back to it when adding the room.
    """
    def __init__(self, parent: MainMenu):
        super().__init__()
        self.ui = Ui_HelpWindow()
        self.ui.setupUi(self)
        self.parent_window = parent

        self.ui.frame.setPixmap(QPixmap(u":/list_art.png"))
        self.ui.water_image.setPixmap(QPixmap(u":/water.png"))
        self.ui.nutrition_image.setPixmap(QPixmap(u":/nutrition.png"))
        self.ui.pot_image.setPixmap(QPixmap(u":/empty_pot.png"))
        self.setWindowIcon(QIcon(":/Plantfolio_logo_small.png"))

        self.ui.text_display.setText(water_text)
        self.ui.select_box.addItem('Watering')
        self.ui.select_box.addItem('Repotting')
        self.ui.select_box.addItem('Nutrition')

        self.ui.select_box.currentIndexChanged.connect(self.display)
        self.parent_window.close_all.connect(self.close)

    def display(self, index):
        if index == 0:
            self.ui.text_display.setText(water_text)
        elif index == 1:
            self.ui.text_display.setText(repot_text)
        elif index == 2:
            self.ui.text_display.setText(nutrition_text)
