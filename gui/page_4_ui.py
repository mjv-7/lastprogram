# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_4.ui'
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
        MainWindow.resize(1145, 769)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_player = QLabel(self.centralwidget)
        self.lbl_player.setObjectName(u"lbl_player")
        self.lbl_player.setGeometry(QRect(30, 660, 51, 51))
        self.lbl_player.setPixmap(QPixmap(u"../images/player.png"))
        self.lbl_player.setScaledContents(True)
        self.btn_whack = QPushButton(self.centralwidget)
        self.btn_whack.setObjectName(u"btn_whack")
        self.btn_whack.setGeometry(QRect(540, 440, 71, 51))
        self.btn_whack.setStyleSheet(u"background-image: url(\"images/chip.png\");")
        self.lbl_ppoint = QLabel(self.centralwidget)
        self.lbl_ppoint.setObjectName(u"lbl_ppoint")
        self.lbl_ppoint.setGeometry(QRect(10, 20, 161, 31))
        font = QFont()
        font.setPointSize(16)
        self.lbl_ppoint.setFont(font)
        self.lbl_ppoint.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1145, 770))
        self.label.setPixmap(QPixmap(u"../images/mole.png"))
        self.label.setScaledContents(True)
        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(960, 50, 141, 51))
        font1 = QFont()
        font1.setPointSize(20)
        self.btn_start.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.lbl_player.raise_()
        self.btn_whack.raise_()
        self.lbl_ppoint.raise_()
        self.btn_start.raise_()

        self.retranslateUi(MainWindow)
        self.btn_whack.clicked.connect(MainWindow.btn_whack_a)
        self.btn_start.clicked.connect(MainWindow.btn_start_a)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"whack-A-mole", None))
        self.lbl_player.setText("")
        self.btn_whack.setText("")
        self.lbl_ppoint.setText(QCoreApplication.translate("MainWindow", u"Points:", None))
        self.label.setText("")
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

