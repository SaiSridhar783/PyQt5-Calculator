# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QApplication, 
                             QHBoxLayout, QVBoxLayout,
                             QPushButton, QLabel)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        label = QLabel("Nagachika Bankai")
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        
        horizontal = QHBoxLayout()
        horizontal.addStretch()
        
        horizontal.addWidget(okButton)
        horizontal.addWidget(cancelButton)
        
        vertical = QVBoxLayout()
        vertical.addWidget(label)
        vertical.addStretch()
        vertical.addLayout(horizontal)
        
        self.setLayout(vertical)
        
        self.setWindowTitle("Horizontal Layout")
        self.show()
         
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
        