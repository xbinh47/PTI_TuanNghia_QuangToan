import sys
from PyQt6 import uic
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QSizePolicy, QScrollArea
from PyQt6.QtGui import QPixmap, QImage
import api
import requests

class MenuItemWidget(QWidget):
    navigate_to_detail = QtCore.pyqtSignal(int)
    def __init__(self, id, imgLink, title, parent=None):
        super().__init__(parent)
        uic.loadUi("ui/menu_Item.ui", self)
        self.id = id
        self.imgLink = imgLink
        self.title = title
        self.detail.clicked.connect(self.navigateToDetail)

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
    
    def navigateToDetail(self):
        self.navigate_to_detail.emit(self.id)

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/home.ui", self)
        self.searchBtn.clicked.connect(self.searchFood)
        with open("main.qss", "r") as style_file:
            style_config = style_file.read()
        self.setStyleSheet(style_config)
        
        # Create a QScrollArea
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setGeometry(self.listItems.geometry())
        
        # Create a QWidget to hold the grid layout
        self.foodItem = QWidget()
        self.gridLayout = QGridLayout(self.foodItem)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        
        self.foodItem.setLayout(self.gridLayout)
        
        # Set the scroll area widget to foodItem
        self.scrollArea.setWidget(self.foodItem)
        self.scrollArea.setWidgetResizable(True)
        
        # Replace the listItems with the scrollArea in the layout
        self.layout().replaceWidget(self.listItems, self.scrollArea)
        self.listItems.deleteLater()
        
    def searchFood(self):
        name = self.search.text()
        if name == "":
            return
        
        # Clear previous search results
        for i in reversed(range(self.gridLayout.count())): 
            widgetToRemove = self.gridLayout.itemAt(i).widget()
            self.gridLayout.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)
        
        recipes = api.search_recipes(name)
        row = 0
        column = 0
        for recipe in recipes["results"]:
            itemWidget = MenuItemWidget(recipe["id"], recipe["image"], recipe["title"])
            itemWidget.navigate_to_detail.connect(self.navigateToDetail)
            itemWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            itemWidget.setMinimumHeight(320)
            itemWidget.setMinimumWidth(220)
            self.gridLayout.addWidget(itemWidget, row, column)
            column += 1
            if column == 2:
                column = 0
                row += 1
                
    @QtCore.pyqtSlot(int)
    def navigateToDetail(self, movie_id):
        self.detailScreen = FoodItem(movie_id)
        self.detailScreen.show()


class FoodItem(QMainWindow):
    def __init__(self, id):
        super().__init__()

        uic.loadUi("ui/food_item.ui", self)
        self.food_detail = api.detail_recipe(id)
        self.time.setText(f"{self.food_detail['readyInMinutes']} minutes")

app = QApplication(sys.argv)
home = Home()
home.show()
sys.exit(app.exec())
