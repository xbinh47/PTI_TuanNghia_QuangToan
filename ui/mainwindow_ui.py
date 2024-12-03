# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(552, 736)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Name_main = QLabel(self.centralwidget)
        self.Name_main.setObjectName(u"Name_main")
        self.Name_main.setGeometry(QRect(20, 90, 431, 51))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(24)
        font.setBold(True)
        self.Name_main.setFont(font)
        self.Calories = QLabel(self.centralwidget)
        self.Calories.setObjectName(u"Calories")
        self.Calories.setGeometry(QRect(20, 140, 331, 31))
        palette = QPalette()
        brush = QBrush(QColor(255, 170, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.Calories.setPalette(palette)
        font1 = QFont()
        font1.setPointSize(12)
        self.Calories.setFont(font1)
        self.Homebutton_main = QPushButton(self.centralwidget)
        self.Homebutton_main.setObjectName(u"Homebutton_main")
        self.Homebutton_main.setGeometry(QRect(10, 20, 71, 31))
        icon = QIcon()
        icon.addFile(u"../img/house-chimney-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Homebutton_main.setIcon(icon)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 200, 31, 31))
        self.label_3.setPixmap(QPixmap(u"../img/clock-regular.svg"))
        self.label_3.setScaledContents(True)
        self.Time_main = QLabel(self.centralwidget)
        self.Time_main.setObjectName(u"Time_main")
        self.Time_main.setGeometry(QRect(60, 200, 161, 31))
        font2 = QFont()
        font2.setPointSize(11)
        self.Time_main.setFont(font2)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 250, 181, 31))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label.setFont(font3)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 380, 551, 421))
        self.label_6.setStyleSheet(u"border-radius: 20px;\n"
"background: rgb(255, 255, 255)")
        self.Main_image = QLabel(self.centralwidget)
        self.Main_image.setObjectName(u"Main_image")
        self.Main_image.setGeometry(QRect(0, 0, 561, 391))
        self.Main_image.setPixmap(QPixmap(u"../img/Carrot-Cake-Recipe-Video.jpg"))
        self.Main_image.setScaledContents(True)
        self.Ingredients_5 = QLabel(self.centralwidget)
        self.Ingredients_5.setObjectName(u"Ingredients_5")
        self.Ingredients_5.setGeometry(QRect(500, 100, 31, 31))
        self.Ingredients_5.setPixmap(QPixmap(u"../img/heart-regular.svg"))
        self.Ingredients_5.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 390, 541, 291))
        self.ingredient_item = QListWidget(self.centralwidget)
        self.ingredient_item.setObjectName(u"ingredient_item")
        self.ingredient_item.setGeometry(QRect(20, 280, 511, 91))
        MainWindow.setCentralWidget(self.centralwidget)
        self.Main_image.raise_()
        self.ingredient_item.raise_()
        self.Name_main.raise_()
        self.Calories.raise_()
        self.Homebutton_main.raise_()
        self.label_3.raise_()
        self.Time_main.raise_()
        self.label.raise_()
        self.label_6.raise_()
        self.Ingredients_5.raise_()
        self.label_2.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 552, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Name_main.setText(QCoreApplication.translate("MainWindow", u"Carrot cake", None))
        self.Calories.setText(QCoreApplication.translate("MainWindow", u"200 calories", None))
        self.Homebutton_main.setText("")
        self.label_3.setText("")
        self.Time_main.setText(QCoreApplication.translate("MainWindow", u"100min", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ingredients", None))
        self.label_6.setText("")
        self.Main_image.setText("")
        self.Ingredients_5.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"- hjbijnimmmmmmmmmmmmmmmmmmmmmmmmmmmnn", None))
    # retranslateUi

