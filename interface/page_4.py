# By: <Your Name Here>
# Date: 2025-06-12
# Program Details: <Program Description Here>

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import manager
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow
from gui.page_4_ui import Ui_MainWindow
from PySide6.QtCore import QTimer,QRect,Qt

if __name__ == "__main__":    
    manager.start()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        with manager.image_gui_path():
            self.setupUi(self)
            self.ppoint = 0     
        self.positions = {}
        self.btn_whack.setVisible(False)
        self.btn_whack.setStyleSheet("border-image: url(\"images/chip.png\") 0 0 0 0 stretch stretch;")
    def btn_whack_a(self):
        self.ppoint += 1
        self.lbl_ppoint.setText(f"Points: {self.ppoint}")
        self.btn_whack.setVisible(False)
    def btn_start_a(self):
        self.btn_whack.setVisible(True)
        self.btn_start.setVisible(False)