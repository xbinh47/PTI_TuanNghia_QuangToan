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
        self.txtAmount = QLabel(Form)
        self.txtAmount.setObjectName(u"txtAmount")
        self.txtAmount.setGeometry(QRect(150, 60, 431, 31))
        font = QFont()
        font.setPointSize(16)
        self.txtAmount.setFont(font)
        self.txtName = QLabel(Form)
        self.txtName.setObjectName(u"txtName")
        self.txtName.setGeometry(QRect(150, 0, 431, 51))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.txtName.setFont(font1)
        self.txtMetric = QLabel(Form)
        self.txtMetric.setObjectName(u"txtMetric")
        self.txtMetric.setGeometry(QRect(150, 100, 431, 31))
        self.txtMetric.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.image.setText("")
        self.txtAmount.setText(QCoreApplication.translate("Form", u"3 medium carrots, peeled and diced", None))
        self.txtName.setText(QCoreApplication.translate("Form", u"Carrot", None))
        self.txtMetric.setText(QCoreApplication.translate("Form", u"3 medium carrots, peeled and diced", None))
    # retranslateUi

