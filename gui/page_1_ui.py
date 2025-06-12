# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_1.ui'
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
        MainWindow.resize(957, 600)
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_gamenu.clicked.connect(MainWindow.btn_gamenu_a)
        self.btn_rules.clicked.connect(MainWindow.btn_rules_a)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.btn_gamenu.setText(QCoreApplication.translate("MainWindow", u"GAME MENU", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome to GREAT AND THE FUNNIEST GAME THAT IS DEFINETLY NOT BORING", None))
        self.btn_rules.setText(QCoreApplication.translate("MainWindow", u"RULES", None))
    # retranslateUi

