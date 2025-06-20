# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_5.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 1024)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1024, 1024))
        font = QFont()
        font.setFamilies([u"Playbill"])
        self.label.setFont(font)
        self.label.setPixmap(QPixmap(u"../images/slots.png"))
        self.label.setScaledContents(True)
        self.lbl_slot1 = QLabel(self.centralwidget)
        self.lbl_slot1.setObjectName(u"lbl_slot1")
        self.lbl_slot1.setGeometry(QRect(100, 130, 251, 491))
        self.lbl_slot1.setScaledContents(True)
        self.lbl_slot2 = QLabel(self.centralwidget)
        self.lbl_slot2.setObjectName(u"lbl_slot2")
        self.lbl_slot2.setGeometry(QRect(390, 130, 251, 491))
        self.lbl_slot2.setScaledContents(True)
        self.lbl_slot3 = QLabel(self.centralwidget)
        self.lbl_slot3.setObjectName(u"lbl_slot3")
        self.lbl_slot3.setGeometry(QRect(680, 130, 251, 491))
        self.lbl_slot3.setScaledContents(True)
        self.btn_spin = QPushButton(self.centralwidget)
        self.btn_spin.setObjectName(u"btn_spin")
        self.btn_spin.setGeometry(QRect(350, 930, 271, 51))
        font1 = QFont()
        font1.setFamilies([u"Elephant"])
        font1.setPointSize(35)
        self.btn_spin.setFont(font1)
        self.lbl_balance = QLabel(self.centralwidget)
        self.lbl_balance.setObjectName(u"lbl_balance")
        self.lbl_balance.setGeometry(QRect(40, 30, 321, 61))
        font2 = QFont()
        font2.setFamilies([u"MS Sans Serif"])
        font2.setPointSize(30)
        self.lbl_balance.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_spin.clicked.connect(MainWindow.btn_spin_a)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.label.setText("")
        self.lbl_slot1.setText("")
        self.lbl_slot2.setText("")
        self.lbl_slot3.setText("")
        self.btn_spin.setText(QCoreApplication.translate("MainWindow", u"SPIN!!", None))
        self.lbl_balance.setText(QCoreApplication.translate("MainWindow", u"BALANCE:", None))
    # retranslateUi

