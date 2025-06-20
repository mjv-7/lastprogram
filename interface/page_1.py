# By: <Mujibullah
# Date: 2025-06-12
# Program Details: <Gambling Desert, Last project for Computer Science class

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import manager
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow
from gui.page_1_ui import Ui_MainWindow

if __name__ == "__main__":    
    manager.start()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        with manager.image_gui_path():
            self.setupUi(self)
    def btn_gamenu_a(self):
          manager.widget.setCurrentWidget(manager.screen3)
          manager.widget.resize(1920, 1080)
    def btn_rules_a(self):
            manager.widget.setCurrentWidget(manager.screen2)
            manager.widget.resize(1490, 620)
    def btn_exit_a(self):
         sys.exit()