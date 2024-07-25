import sys
from PyQt6 import uic
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QSizePolicy, QScrollArea, QMessageBox, QFileDialog
from PyQt6.QtGui import QPixmap, QImage
import api
import requests
import sqlite3
class Register(QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("ui/register.ui", self)
        self.name = ""
        self.btnRegister.clicked.connect(self.register)
        self.btnRegister_2.clicked.connect(self.showLoginPage)

    def register(self):
        self.name = self.txtName.text()
        email = self.txtEmail.text()
        password = self.txtPassword.text()

        if not self.name:
            err_box.setText("Please enter your name!")
            err_box.exec()
            return 

        if not email:
            err_box.setText("Please enter your email!")
            err_box.exec() 
            return 

        if not password:
            err_box.setText("Please enter your password!")
            err_box.exec()
            return
        
        query = f"SELECT * FROM USER WHERE email = ('{email}')"
        result = query_db(query)

        if len(result) > 0:
            err_box.setText("This email had been used for an another account!")
            err_box.exec()
            return
        
        query = f"INSERT INTO USER (name, password, email) VALUES ('{self.name}', '{password}', '{email}')"
        print(query)
        insert_db(query)

        success_box.setText("Register Successfully!")
        loginPage.show()
        self.close()

    def showLoginPage(self):
        loginPage.show()
        self.close()

class Login(QMainWindow):
    def __init__(self):
        super().__init__() #call out the characters of ParentClass
        uic.loadUi("ui/login.ui", self) #Create and load the file ui
        self.name = ""
        self.Login.clicked.connect(self.checkLogin)
        self.btnRegister.clicked.connect(self.showRegisterPage)
        
    def checkLogin(self):
        email = self.txtEmail.text()
        password = self.txtPassword.text()

        if not email:
            err_box.setText("Please enter your email!")
            err_box.exec()
            return

        if not password:
            err_box.setText("Please enter your password!")
            err_box.exec()
            return

        query = f"SELECT * FROM USER WHERE email ='{email}' and password='{password}'" #query select
        result = query_db(query)

        if len(result) == 0:
            err_box.setText("Invalid Username or Password!")
            err_box.exec()
            return
        
        self.name = result[0][1]
        success_box.setText("Succesfully Login!")
        success_box.exec()
        self.showMainPage(result[0][0])

    def showRegisterPage(self):
            registerPage.show()
            self.close()
            
    def showMainPage(self, id):
        self.mainPage = Home(id)
        self.mainPage.show()
        self.close()
            
class AccInfo(QMainWindow):
    def __init__(self, id):
        super().__init__()
        uic.loadUi("ui/acc_info.ui", self)
        self.btnUpdate.clicked.connect(self.updateInfo)
        self.id = id
        self.user = get_user_by_id(self.id)
        self.showInfo()
        self.uploadBtn.clicked.connect(self.loadAvatar)
        self.avatarFile = ""
        self.btnBack.clicked.connect(self.showMainPage)
        self.caculateBtn.clicked.connect(self.healthCondition)

    def bmiCaculate(self,weight,height):
        height = height/100
        return weight/(height*height)
        
    def healthCondition(self):
        if not self.user[6] and not self.user[7]:
            err_box.setText("Weight and Height are not saved")
            err_box.exec()
            return
        bmi = self.bmiCaculate(float(self.user[6]),float(self.user[7]))
        print(bmi)
        if bmi < 18.5:
            self.bmi.setText(f"Underweight")
        elif bmi < 24.9:
            self.bmi.setText(f"Normal")
        elif bmi < 29.9:
            self.bmi.setText(f"Overweight")
        elif bmi < 34.9:
            self.bmi.setText(f"Obese")
        else:
            self.bmi.setText(f"Extremly obese")


    def showInfo(self):
        
        self.txtName.setText(self.user[1])
        self.txtEmail.setText(self.user[2])
        self.txtPassword.setText(self.user[3])
        self.txtAge.setText(str(self.user[4]))
        if self.user[5] == 'Female':
            self.txtGender.setCurrentIndex(0)
        else:
            self.txtGender.setCurrentIndex(1)
        self.txtWeight.setText(str(self.user[6]))
        self.txtHeight.setText(str(self.user[7]))
        if self.user[8]:
            # load avatar
            self.avatarLabel.setPixmap(QPixmap(self.user[8]))
            self.txtAvatar = self.user[8]
            
    def loadAvatar(self):
        # local
        file, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)")
        if file:
            self.avatarFile = file
            self.avatarLabel.setPixmap(QPixmap(file))

    def updateInfo(self):
        txt_name = self.txtName.text()
        txt_email = self.txtEmail.text()
        txt_age = self.txtAge.text()
        txt_gender = self.txtGender.currentText()
        txt_weight = self.txtWeight.text()
        txt_height = self.txtHeight.text()
        
        update_user(self.id, txt_name, txt_email, txt_age, txt_gender, txt_weight, txt_height, self.avatarFile)
        success_box.setText("Update user successfully")
        success_box.exec()
        
    def showMainPage(self):
        self.mainPage = Home(self.id)
        self.mainPage.show()
        self.close()

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
    def __init__(self, id):
        super().__init__()
        uic.loadUi("ui/home.ui", self)
        self.id = id
        user = get_user_by_id(self.id)
        if user[8]:
            self.avatar.setPixmap(QPixmap(user[8]))
        self.hi.setText(user[1])
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
        self.accountBtn.clicked.connect(self.showAccount)
    
    def showAccount(self):
        self.accountScreen = AccInfo(self.id)
        self.accountScreen.show()
        self.close()
        
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
        self.vegetarian.setText(f"vegetarian: {self.food_detail['vegetarian']}")
        self.name.setText(f"{self.food_detail['title']}")
        self.gluten.setText(f"glutenFree: {self.food_detail['glutenFree']}")
        self.money.setText(f"cheap: {self.food_detail['cheap']}")
        self.healthy.setText(f"veryHealthy: {self.food_detail['veryHealthy']}")
        self.popular.setText(f"veryPopular: {self.food_detail['veryPopular']}")
        self.dairy.setText(f"dairyFree: {self.food_detail['dairyFree']}")
        self.like.setText(f"{self.food_detail['aggregateLikes']}")
        self.label_2.setText(f"{self.food_detail['instructions']}")
        image = QImage()
        image.loadFromData(requests.get(self.food_detail['image']).content)
        self.image.setPixmap(QPixmap(image))
        print(self.food_detail['image'])

if __name__ == '__main__':
    sqliteConnection = sqlite3.connect('data/data.db')
    def insert_db(query):
        cusor = sqliteConnection.cursor()
        cusor.execute(query)
        sqliteConnection.commit()
        cusor.close()

    def query_db(query):
        cursor = sqliteConnection.cursor()
        cursor.execute(query)
        result = cursor.fetchall() #check if the result was in db(in list)
        cursor.close()
        return result
    
    def get_user_by_id(id):
        query = f"SELECT * FROM USER WHERE id = {id}"
        result = query_db(query)
        return result
    
    def get_user_by_id(id):
        query = f"SELECT * FROM USER WHERE id = {id}"
        result = query_db(query)
        return result[0]
    
    def update_user(id, name, email, age, gender, weight, height, avatar):
        query = f"UPDATE USER SET name = '{name}', email = '{email}', age = '{age}', gender = '{gender}', weight = '{weight}', height = '{height}', avatar = '{avatar}' WHERE id = {id}"
        insert_db(query)

    app = QApplication(sys.argv)

    loginPage = Login()
    loginPage.show()
    registerPage = Register()

    err_box = QMessageBox()
    err_box.setWindowTitle("Error.")
    err_box.setIcon(QMessageBox.Icon.Warning)
    # msg_box.setStyleSheet()
    
    success_box = QMessageBox()
    success_box.setWindowTitle("Success!")
    success_box.setIcon(QMessageBox.Icon.Information)
    # success_box.setStyleSheet
    app.exec()
    
