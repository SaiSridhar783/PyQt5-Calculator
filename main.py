import sys
import math
from PyQt5.QtWidgets import (QPushButton, QLineEdit, QGridLayout,
                             QWidget, QApplication)

class Button:
    def __init__(self, text, results):
        self.b = QPushButton(str(text))
        self.text = text
        self.results = results
        self.b.clicked.connect(lambda: self.handleInput(self.text))
        
    def handleInput(self, v):
        if v == "=":
            res = eval(self.results.text())
            self.results.setText(str(res))
            
        elif v == "AC":
            self.results.setText("")
            
        elif v == "√":
            k = float(self.results.text())
            self.results.setText(str(math.sqrt(k)))
            
        elif v == "DEL":
            k = self.results.text()
            self.results.setText(k[:-1])
            
        else:
            cur = self.results.text()
            new = cur + str(v)
            self.results.setText(new)
        
        
class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.CreateApp()
        
    def CreateApp(self):
        
        # Creating a Grid
        grid = QGridLayout()
        result = QLineEdit()
        
        buttons = ["AC","√","DEL","/",
                   7,8,9,"*",
                   4,5,6,"-",
                   1,2,3,"+",
                   0,".","="]
        
        row = 2
        col = 0
        
        grid.addWidget(result, 0, 0, 2, 4)
        
        for button in buttons:
            if col>3:
                col = 0
                row += 1
                
            butObj = Button(button, result)
                
            if button==0:
                grid.addWidget(butObj.b, row, col, 1, 2)
                col += 1
                
            else:
                grid.addWidget(butObj.b, row, col, 1, 1)
            
            col += 1
        
        self.setLayout(grid)        
        self.show()
        
    
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec_())