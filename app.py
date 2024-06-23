from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6 import uic
import sys

class Register(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/register.ui", self)
        self.name = ""
        self.btnRegister.clicked.connect(self.Register)
        self.btnLogin.clicked.connect(self.showLoginPage)

    def Register(self):
        self.name = self.txtName.text()
        email = self.txtEmail.text
        password = self.txtPassword.text()
        comfirm_password = self.txtCPassword.text()

        if not self.name:
            msg_box.setText("Vui lòng nhập tên!")
            msg_box.exec
            return
        if not email:
            msg_box.setText("Vui lòng nhập email!")
            msg_box.exec
            return
        if not password:
            msg_box.setText("Vui lòng nhập mật khẩu!")
            msg_box.exec()
            return
        if not self.agree.isChecked():
            msg_box.setText("Vui lòng đọc và đồng ý với các điều khoản của AdoptMate!")
            msg_box.exec
            return
        
        success_box.setText("Bạn đã đăng kí tài khoản thành công!")
        self.close()

    def showLoginPage(self):
        loginPage.show()
        self.close()

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/login.ui",self)
        self.btnLogin.clicked.connect(self.check_login)
        self.btnRegister.clicked.connect(self.show_register)

    def check_login(self):
        email = self.txtEmail.text()
        password = self.txtPassword.text()

        if not email:
            msg_box.setText("Vui lòng nhập lại email!")
            msg_box.exec
            return
    
        if not password:
            msg_box.setText("Vui lòng nhập lại mật khẩu!")
            msg_box.exec()
            return
        
        if email == "admin@gmail.com" and password == "123456":
            success_box.setText("Đăng nhập thành công!")
            success_box.exec()
            return
        else:
            msg_box.setText("Email hoặc mật khẩu không đúng!")
            msg_box.exec()
            return
        
    def show_register(self):
        registerPage

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    loginPage = Login()
    loginPage.show()
    registerPage = Register()

    msg_box = QMessageBox()
    msg_box.setWindowTitle("Error")
    msg_box.setIcon(QMessageBox.Icon.Warning)

    success_box = QMessageBox()
    success_box.setWindowTitle("Success")
    success_box.setIcon(QMessageBox.Icon.Information)

    app.exec()