# By: Mujibullah
# Date: 2025-06-12
# Program Details: Gambling Desert, Last project for Computer Science class

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import manager, random
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QMessageBox
from gui.page_4_ui import Ui_MainWindow
from PySide6.QtCore import QTimer,QRect,Qt

if __name__ == "__main__":    
    manager.start()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        with manager.image_gui_path():
            self.setupUi(self)
 # Initialize score and tries
        self.ppoint = 0
        self.tries = 0
        self.max_points = 5
        self.max_tries = 8 # Number of chances to click the mole

        # Timer
        self.timer = QTimer()
        self.timer.setInterval(1000)  # 1 second
        self.timer.timeout.connect(self.move_mole)

        # Positions (slot index: [x, y])
        self.positions = {1: [310, 420],  2: [360, 330],  3: [610, 330],  4: [610, 420], 5: [900, 420], 6: [860, 330]}

        # Button setup
        self.btn_whack.setVisible(False)
        self.btn_whack.setStyleSheet("border-image: url(\"images/chip.png\") 0 0 0 0 stretch stretch;")
        try:
            self.btn_whack.clicked.disconnect()
        except TypeError:
            pass
        self.btn_whack.clicked.connect(self.btn_whack_a)
        self.btn_start.clicked.connect(self.btn_start_a)

    def btn_start_a(self):
        self.ppoint = 0
        self.tries = 0
        self.lbl_ppoint.setText("Points: 0")
        self.btn_whack.setVisible(True)
        self.btn_start.setVisible(False)
        self.timer.start()

    def move_mole(self):
        self.tries += 1
        if self.tries > self.max_tries:
            self.timer.stop()
            self.btn_whack.setVisible(False)
            self.btn_start.setVisible(True)
            self.lbl_ppoint.setText("Points: 0")
            QMessageBox.information(self, "Game Over", "You lost! Try again.")
            return

        random_slot = random.randint(1, 6)
        position = self.positions[random_slot]
        self.btn_whack.move(position[0], position[1])
        self.btn_whack.setVisible(True)

    def btn_whack_a(self):
        print("Whack!")
        self.ppoint += 1
        self.lbl_ppoint.setText(f"Points: {self.ppoint}")
        self.btn_whack.setVisible(False)

        if self.ppoint >= self.max_points:
            manager.screen3.balance += 250
            manager.screen3.lbl_balance.setText(f"Balance: ${manager.screen3.balance}")
            self.timer.stop()
            self.btn_whack.setVisible(False)
            QMessageBox.information(self, "You Win!", "You won the game!")
            # Simulate moving to screen 3
            manager.widget.setCurrentWidget(manager.screen3)  # Replace with your screen switch function
            manager.widget.resize(1920, 1080)
            self.btn_start.setVisible(True)
            self.ppoint = 0
            self.tries = 0
            self.max_points = 5
            self.max_tries = 8 
            self.lbl_ppoint.setText("Points: 0")
