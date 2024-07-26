# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ingredient_Item.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(590, 150)
        self.image = QLabel(Form)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(0, 0, 150, 150))
        self.image.setPixmap(QPixmap(u"../../../../Downloads/images (2).jpeg"))
        self.image.setScaledContents(True)
        self.amount = QLabel(Form)
        self.amount.setObjectName(u"amount")
        self.amount.setGeometry(QRect(150, 110, 431, 31))
        font = QFont()
        font.setPointSize(11)
        self.amount.setFont(font)
        self.name = QLabel(Form)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(150, 0, 151, 51))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.name.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.image.setText("")
        self.amount.setText(QCoreApplication.translate("Form", u"3 medium carrots, peeled and diced", None))
        self.name.setText(QCoreApplication.translate("Form", u"Carrot", None))
    # retranslateUi

