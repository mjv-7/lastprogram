# By: <Your Name Here>
# Date: 2025-06-12
# Program Details: <Program Description Here>

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import manager, interface
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QTimer,QRect
from PySide6.QtCore import Qt   
from PySide6.QtWidgets import QMainWindow
from gui.page_3_ui import Ui_MainWindow

if __name__ == "__main__":    
    manager.start()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        with manager.image_gui_path():
            self.setupUi(self)
        
        self.timer=QTimer()
        self.timer.timeout.connect(self.move_lbl) 
        self.timer.start(5)
        self.key_press=[]
        self.speed=1
        self.walls = [self.lbl_w1,self.lbl_w2,self.lbl_w3,self.lbl_w4,self.lbl_w5,self.lbl_w6,self.lbl_w7,self.lbl_w8,self.lbl_w9]
        
    def btn_main_a(self):
        manager.widget.setCurrentWidget(manager.screen1)
        manager.widget.resize(960, 600)
    def move_lbl(self):
        move_x = ((Qt.Key.Key_D in self.key_press) * self.speed) + ((Qt.Key.Key_A in self.key_press)* -self.speed)
        move_y = ((Qt.Key.Key_W in self.key_press) * -self.speed) + ((Qt.Key.Key_S in self.key_press)* self.speed)
        self.lbl_player.move(self.lbl_player.x()+move_x,self.lbl_player.y()+move_y)

        for wall in self.walls:
            if self.collision(self.lbl_player, wall):
                self.lbl_player.move(self.lbl_player.x()-move_x,self.lbl_player.y()-move_y)

        if self.collision(self.lbl_player, self.lbl_mole):
         manager.widget.setCurrentWidget(manager.screen4)
         manager.widget.resize(1280, 720)
         self.lbl_player.move(950, 990)
         self.key_press.clear()
         
    def keyPressEvent(self, event):
        self.key_press.append(event.key())
    def keyReleaseEvent(self, event):
       if self.key_press:
            self.key_press.remove(event.key())
    def collision(self, object1, object2):
        # Get the global coordinates of the top-left corner of object1
        object1_global_top_left = object1.mapToGlobal(object1.rect().topLeft())

        # Get the global coordinates of the top-left corner of object2
        object2_global_top_left = object2.mapToGlobal(object2.rect().topLeft())

        # Check for collision
        return QRect(object1_global_top_left, object1.rect().size()).intersects(QRect(object2_global_top_left, object2.rect().size()))

