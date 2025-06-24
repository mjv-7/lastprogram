# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_1.ui'
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
        MainWindow.resize(957, 597)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_gamenu = QPushButton(self.centralwidget)
        self.btn_gamenu.setObjectName(u"btn_gamenu")
        self.btn_gamenu.setGeometry(QRect(350, 200, 231, 61))
        font = QFont()
        font.setFamilies([u"Noto Serif CJK KR SemiBold"])
        font.setPointSize(25)
        self.btn_gamenu.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 891, 111))
        font1 = QFont()
        font1.setPointSize(17)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_rules = QPushButton(self.centralwidget)
        self.btn_rules.setObjectName(u"btn_rules")
        self.btn_rules.setGeometry(QRect(350, 270, 231, 61))
        font2 = QFont()
        font2.setFamilies([u"P052"])
        font2.setPointSize(30)
        font2.setItalic(True)
        self.btn_rules.setFont(font2)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 951, 601))
        self.label_2.setPixmap(QPixmap(u"../images/desert.png"))
        self.label_2.setScaledContents(True)
        self.btn_exit = QPushButton(self.centralwidget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(350, 340, 231, 61))
        self.btn_exit.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_2.raise_()
        self.btn_gamenu.raise_()
        self.label.raise_()
        self.btn_rules.raise_()
        self.btn_exit.raise_()

        self.retranslateUi(MainWindow)
        self.btn_gamenu.clicked.connect(MainWindow.btn_gamenu_a)
        self.btn_rules.clicked.connect(MainWindow.btn_rules_a)
        self.btn_exit.clicked.connect(MainWindow.btn_exit_a)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gambling desert", None))
        self.btn_gamenu.setText(QCoreApplication.translate("MainWindow", u"GAME MENU", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome to GREAT AND THE FUNNIEST GAME THAT IS DEFINETLY NOT BORING", None))
        self.btn_rules.setText(QCoreApplication.translate("MainWindow", u"RULES", None))
        self.label_2.setText("")
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
    # retranslateUi

