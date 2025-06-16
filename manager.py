
# By: <Your Name Here>
# Date:2025-06-12
# Program Details: <Program Description Here>

import sys, os, contextlib
from PySide6.QtWidgets import (QStackedWidget, QApplication)
import interface.page_1
import interface.page_2 
import interface.page_3
import interface.page_4

def start():
    widget.show()
    
    sys.exit(app.exec())

@contextlib.contextmanager
def image_gui_path():
    try:
        os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gui'))
        yield
    finally:
        os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__))))

app = QApplication(sys.argv)
screen1 = interface.page_1.MainWindow()
screen2 = interface.page_2.MainWindow()
screen3 = interface.page_3.MainWindow()
screen4 = interface.page_4.MainWindow()
list_on_screens = list(globals())
widget = QStackedWidget()
for variable_name in list_on_screens:
    if variable_name.startswith('screen'):
        value = globals()[variable_name]
        widget.addWidget(value)
widget.resize(screen1.size())
widget.setWindowTitle(screen1.windowTitle())
