# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_Item.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(230, 270)
        self.image = QLabel(Form)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(0, -10, 230, 230))
        self.image.setPixmap(QPixmap(u"../img/Carrot-Cake-Recipe-Video.jpg"))
        self.image.setScaledContents(True)
        self.name = QLabel(Form)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(-10, 220, 241, 51))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.name.setFont(font)
        self.name.setStyleSheet(u"padding: 0px 5px;\n"
"white-space: pre;")
        self.name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.detail = QPushButton(Form)
        self.detail.setObjectName(u"detail")
        self.detail.setGeometry(QRect(180, 0, 40, 40))
        icon = QIcon()
        icon.addFile(u"../img/list-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.detail.setIcon(icon)
        self.detail.setIconSize(QSize(30, 30))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.image.setText("")
        self.name.setText(QCoreApplication.translate("Form", u"Carrot cake", None))
        self.detail.setText("")
    # retranslateUi

