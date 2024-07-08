from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QSizePolicy
import requests
import sys

class MenuItemWidget(QWidget):
    def __init__(self, id, imgLink, title, parent=None):
        super().__init__(parent)
        uic.loadUi("ui/menu_Item.ui", self)
        self.id = id
        self.imgLink = imgLink
        self.title = title

        self.init()

    def init(self):
        image = QImage()
        image.loadFromData(requests.get(self.imgLink).content)
        self.image.setPixmap(QPixmap(image))
        self.image.setScaledContents(True)
        self.name.setText(self.title)
        self.name.setWordWrap(True)  # Enable word wrapping for the title

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setMinimumHeight(300)
        self.setMinimumWidth(220)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MenuItemWidget(id=1, imgLink="https://via.placeholder.com/150", title="Sample Title")
    widget.show()
    sys.exit(app.exec())
