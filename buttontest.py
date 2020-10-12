# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QHBoxLayout,
                             QVBoxLayout, QPushButton, QLabel, QLineEdit)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.count = 0
        
    def init_ui(self):
        label = QLabel("Name")
        name_input = QLineEdit()
        self.button = QPushButton("Clicked : 0 times")
        self.button.pressed.connect(self.pressedButton)
        self.button.clicked.connect(self.clickedButton)
        self.button.released.connect(self.releasedButton)
        
        h = QHBoxLayout()
        h.addWidget(label)
        h.addWidget(name_input)
        
        v = QVBoxLayout()
        v.addLayout(h)
        v.addWidget(self.button)
        
        self.setLayout(v)
        
        self.setWindowTitle("Horizontal Layout")
        self.show()
        
    def clickedButton(self):
        print("Clickity Clack")
        
    def pressedButton(self):
        print("Button on the pressing stage")
        self.count += 1
        self.button.setText("Clicked :" + str(self.count) + " times")
        
    def releasedButton(self):
        print("Tata")
         
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
        