# By: Mujibullah
# Date: 2025-06-12
# Program Details: Gambling Desert, Last project for Computer Science class

import os, sys, random
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import manager
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import QTimer
from gui.page_6_ui import Ui_MainWindow

if __name__ == "__main__":    
    manager.start()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        with manager.image_gui_path():
            self.setupUi(self)
            self.red = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
            self.black = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
            self.lbl_balance.setText(f"Balance: ${manager.screen3.balance}")
            self.selected_numbers = []
            for i in range(37):
                btn = getattr(self, f'btn_{i}', None)
                if btn:
                    btn.clicked.connect(self.betting)

            # Connect betting buttons
            self.btn_bet.clicked.connect(self.btn_bet_a)
            self.btn_allin.clicked.connect(self.btn_allin_a)
    def betting(self):
        if len(self.selected_numbers) >= 3:
            return  # Only allow 3 numbers
        btn = self.sender()
        btn_number = int(btn.objectName().split('_')[1])
        if btn_number not in self.selected_numbers:
            self.selected_numbers.append(btn_number) 
    def btn_bet_a(self):
        if len(self.selected_numbers) != 3:
            QMessageBox.warning(self, "Selection Error", "You must select 3 numbers before betting.")
            return

        try:
            self.bet = int(self.txt_bet.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number.")
            return

        if self.bet > manager.screen3.balance:
            QMessageBox.warning(self, "Balance Error", "Insufficient balance.")
            return

        # Deduct bet
        manager.screen3.balance -= self.bet
        self.lbl_balance.setText(f"Balance: ${manager.screen3.balance}")
        ai_choice = random.randint(0, 36)
        self.lbl_roulette.setText(str(ai_choice))

        if ai_choice in self.selected_numbers:
            self.win()
        else:
            self.lose()

        # Reset selection and button styles
        self.selected_numbers.clear()
        for i in range(37):
            btn = getattr(self, f'btn_{i}', None)
    def btn_allin_a(self):
        allin = manager.screen3.balance
        self.txt_bet.setText(str(allin))

    def reset_betting_buttons(self):
       for num in self.selected_numbers:
           btn = getattr(self, f'btn_{num}')
           btn.setStyleSheet("")
       self.selected_numbers = []

    def win(self):
        manager.screen3.balance = self.bet *2
        QMessageBox.information(self, "Result", "You win!")

    def lose(self):
       if manager.screen3.balance == 0:
           manager.widget.setCurrentWidget(manager.screen3)
           manager.widget.resize(1920, 1080)
       QMessageBox.information(self, "Result", "You lose.")