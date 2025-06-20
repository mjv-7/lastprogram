# By: Mujibullah
# Date: 2025-06-12
# Program Details: Gambling Desert, Last project for Computer Science class

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import manager
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow
from gui.page_2_ui import Ui_MainWindow

if __name__ == "__main__":    
    manager.start()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        with manager.image_gui_path():
            self.setupUi(self)
    def btn_main_a(self):
        manager.widget.setCurrentWidget(manager.screen1)
        manager.widget.resize(960, 600)