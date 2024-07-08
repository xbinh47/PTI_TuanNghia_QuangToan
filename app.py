import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QSizePolicy, QScrollArea
import api
from ui.widget.menu_Item import MenuItemWidget

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
            itemWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            itemWidget.setMinimumHeight(320)
            itemWidget.setMinimumWidth(220)
            self.gridLayout.addWidget(itemWidget, row, column)
            column += 1
            if column == 2:
                column = 0
                row += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    home = Home()
    home.show()
    sys.exit(app.exec())
