import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QMainWindow, QLineEdit
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import QUrl
import requests
import os
import api

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/home.ui", self)
        self.searchBtn.clicked.connect(self.searchFood)

    def searchFood(self):
        name = self.search.text()
        if name == "":
            return
        
        results = api.search_recipes(name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    home = Home()
    home.show()
    sys.exit(app.exec())
