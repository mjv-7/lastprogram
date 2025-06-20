# By: <Your Name Here>
# Date: 2025-06-12
# Program Details: <Program Description Here>

import os, sys, random
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import manager
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import QTimer
from gui.page_5_ui import Ui_MainWindow

if __name__ == "__main__":    
    manager.start()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        with manager.image_gui_path():
            self.setupUi(self)
            self.setWindowTitle("Slot Machine")
            self.images = ['7.png', 'cherry.png', "lemon.png", 'robot.png',]
            self.balance = 0
            self.btn_spin.clicked.connect(self.btn_spin_a)
            # Initialize spin timer
            self.spin_timer = QTimer()
            self.spin_timer.timeout.connect(self.btn_spin_a)

            # Track how long it's been spinning
            self.spin_duration = 0

            # Connect button
            self.btn_spin.clicked.connect(self.start_spin)
    def message_box(self,text,title):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.exec()
    def start_spin(self):
        self.balance -= 10
        self.lbl_balance.setText(f"Balance: ${self.balance}")
        self.spin_duration = 0
        self.spin_timer.start(100)  # Call spin_animation every 100ms
    def btn_spin_a(self):

            self.spin1 = random.choice(self.images)
            self.spin2 = random.choice(self.images)
            self.spin3 = random.choice(self.images)
            self.lbl_slot1.setPixmap(QPixmap(f"images/{self.spin1}"))
            self.lbl_slot2.setPixmap(QPixmap(f"images/{self.spin2}"))
            self.lbl_slot3.setPixmap(QPixmap(f"images/{self.spin3}"))
            
            

            self.spin_duration += 100

            if self.spin_duration >= 3000:  # 3 seconds
                self.spin_timer.stop()
                self.show_final_result()
    def show_final_result(self):
        if self.spin1 == self.spin2 == self.spin3:
            self.balance += 500
            manager.screen3.lbl_balance.setText(f"Balance: ${self.balance}")
            self.message_box("WINNER", "WINNER")
            manager.widget.setCurrentWidget(manager.screen3)
            manager.widget.resize(1920, 1080)
                