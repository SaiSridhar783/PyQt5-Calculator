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
        self.text_label = QLabel("No name, no do")
        self.label = QLabel("Name")
        self.name_input = QLineEdit()
        self.button = QPushButton("Clicked : 0 times")
        
        self.button.setText("Set Name")
        self.button.clicked.connect(self.alterName)


        h = QHBoxLayout()
        h.addWidget(self.label)
        h.addWidget(self.name_input)
        
        v = QVBoxLayout()
        v.addWidget(self.text_label)
        v.addLayout(h)
        v.addWidget(self.button)
        
        self.setLayout(v)
        
        self.setWindowTitle("Horizontal Layout")
        self.show()
        
    def alterName(self):
        input_text = self.name_input.text()
        string = "You've entered : " + input_text
        self.text_label.setText(string)
        

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
        