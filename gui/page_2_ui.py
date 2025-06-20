# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_2.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
        MainWindow.resize(1490, 618)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 10, 511, 51))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 70, 1211, 191))
        font1 = QFont()
        font1.setPointSize(27)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 330, 1451, 191))
        font2 = QFont()
        font2.setPointSize(13)
        self.label_3.setFont(font2)
        self.btn_main = QPushButton(self.centralwidget)
        self.btn_main.setObjectName(u"btn_main")
        self.btn_main.setGeometry(QRect(1280, 540, 141, 41))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_main.clicked.connect(MainWindow.btn_main_a)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hello and welcome to the game that was created by Mujibullah", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"This game consists of 3 levels. the first is whack a mole\n"
" The second game is spin machine\n"
" the third game is roulette", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"For the whack-a-mole You have to get 5 casino chips, and you would receive $250, the entrance is free\n"
" For spin machine You have to have $500 in your balance, or you can not enter, to enter the spin machine, you would spend $300, and when you win, you would recieve $500  \n"
" and Finally Roulette, Your challenge is to pick only three numbers, and bet as much as you want. If you win, you would recieve double of your bet money", None))
        self.btn_main.setText(QCoreApplication.translate("MainWindow", u"Main Menu", None))
    # retranslateUi

