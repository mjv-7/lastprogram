# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_3.ui'
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
        MainWindow.resize(1920, 1080)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1920, 1080))
        self.label.setPixmap(QPixmap(u"../images/games.png"))
        self.label.setScaledContents(True)
        self.btn_main = QPushButton(self.centralwidget)
        self.btn_main.setObjectName(u"btn_main")
        self.btn_main.setGeometry(QRect(800, 1040, 121, 41))
        font = QFont()
        font.setFamilies([u"Noto Serif Tangut"])
        font.setPointSize(12)
        self.btn_main.setFont(font)
        self.lbl_player = QLabel(self.centralwidget)
        self.lbl_player.setObjectName(u"lbl_player")
        self.lbl_player.setGeometry(QRect(950, 990, 51, 51))
        self.lbl_player.setPixmap(QPixmap(u"../images/player.png"))
        self.lbl_player.setScaledContents(True)
        self.lbl_mole = QLabel(self.centralwidget)
        self.lbl_mole.setObjectName(u"lbl_mole")
        self.lbl_mole.setGeometry(QRect(250, 550, 31, 51))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 370, 161, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(1640, 320, 181, 41))
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(900, 100, 161, 61))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_spin = QLabel(self.centralwidget)
        self.lbl_spin.setObjectName(u"lbl_spin")
        self.lbl_spin.setGeometry(QRect(970, 220, 61, 21))
        self.lbl_slots = QLabel(self.centralwidget)
        self.lbl_slots.setObjectName(u"lbl_slots")
        self.lbl_slots.setGeometry(QRect(1750, 520, 54, 51))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_main.clicked.connect(MainWindow.btn_main_a)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.label.setText("")
        self.btn_main.setText(QCoreApplication.translate("MainWindow", u"MAIN MENU", None))
        self.lbl_player.setText("")
        self.lbl_mole.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Level 1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Level 2", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Level 3", None))
        self.lbl_spin.setText("")
        self.lbl_slots.setText("")
    # retranslateUi

