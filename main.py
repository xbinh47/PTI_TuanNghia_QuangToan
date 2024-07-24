from PyQt6 import QtWidgets 
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt6.QtCore import QUrl
from PyQt6 import uic
import sys
import sqlite3
import requests
import datetime
# http://openweathermap.org/img/w/04d.png
class Register(QtWidgets.QMainWindow):
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

class Login(QtWidgets.QMainWindow):
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
        self.showMainPage()

    def showRegisterPage(self):
            registerPage.show()
            self.close()
            
class AccInfo(QtWidgets.QMainWindow):
    def __init__(self, id):
        super().__init__()
        uic.loadUi("ui/acc_info.ui", self)
        self.btnUpdate.clicked.connect(self.updateInfo)
        self.id = id
        self.showInfo()
        self.uploadBtn.clicked.connect(self.loadAvatar)
        self.avatarFile = ""
        
    def showInfo(self):
        user = get_user_by_id(self.id)
        self.txtName.setText(user[1])
        self.txtEmail.setText(user[2])
        self.txtPassword.setText(user[3])
        self.txtAge.setText(user[4])
        if user[5] == 'Female':
            self.txtGender.setCurrentIndex(0)
        else:
            self.txtGender.setCurrentIndex(1)
        self.txtWeight.setText(user[6])
        self.txtHeight.setText(user[7])
        if user[8]:
            # load avatar
            self.avatarLabel.setPixmap(QPixmap(user[8]))
            self.txtAvatar = user[8]
            
    def loadAvatar(self):
        # local
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)")
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

    app = QtWidgets.QApplication(sys.argv)

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
    