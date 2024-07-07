from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QColorConstants, QImage
from PyQt6.QtWidgets import QWidget, QLabel
import os
import requests

class MenuItemWidget(QWidget):
    def __init__(self, id, imgLink, title):
        super().__init__()
        uic.load_ui(os.path.join(os.getcwd(), "ui/menu_Item.ui"))
        self.id = id
        self.imgLink = imgLink
        self.title = title

        self.init()
    
    def init(self):
        image = QImage()
        image.loadFromData(requests.get(self.imgLink).content)
        self.image.setPixmap(QPixmap(image))
        self.name.setText(self.title)

    def navigateToHome():
        return
    
    def navigateToDetail():
        return