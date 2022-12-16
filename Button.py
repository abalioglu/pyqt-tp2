import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import math
from ButtonModel import ButtonModel

class CanvasButton(QWidget):
    bbox = QRect(5,5,120,40)
    defaultCol = QColor('red')
    buttonm = ButtonModel()
    hoverCol = QColor('blue')
    pressCol = QColor('black')

    def _init_(self):
        super().__init__()
        self.setMouseTracking(True)  
        
    def mousePressEvent(self, event): # evenement mousePress
        #print("press: ", event.pos())
        cursorOver = self.cursorOnEllipse(event.pos())
        if(cursorOver == True):
            self.buttonm.enter()
            self.buttonm.press()
        else:
            self.buttonm.state = self.buttonm.pressOut
        self.update()
        print(self.buttonm.state)
    def mouseReleaseEvent(self, event): # evenement mouseRelease
        #print("release: ", event.pos())
        self.buttonm.release()
        self.update()
        print(self.buttonm.state)
    def mouseMoveEvent(self, event): # evenement mouseMove
        #print("move: ", event.pos())
        cursorOver = self.cursorOnEllipse(event.pos())
        if(cursorOver == True):
            self.buttonm.enter()
        else:
            self.buttonm.leave()
        self.update()
        print(self.buttonm.state)
        #print(cursorOver)
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(self.defaultCol) # add a red pen
        if(self.buttonm.state == self.buttonm.idle):
            painter.setBrush(self.defaultCol)
        if(self.buttonm.state == self.buttonm.hover):
            painter.setBrush(self.hoverCol)
        if(self.buttonm.state == self.buttonm.pressIn):
            painter.setBrush(self.pressCol)
        if(self.buttonm.state == self.buttonm.pressOut):
            painter.setBrush(self.defaultCol)
        painter.drawEllipse(self.bbox)
        
    def cursorOnEllipse(self, point):
        p = ((math.pow((point.x() - 65), 2) / math.pow(60, 2)) + (math.pow((point.y() - 25), 2) / math.pow(20, 2)))
        if(p<=1):
            return True
        else:
            return False
        
        
def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.resize(300,200)
    canvasbutton = CanvasButton()
    window.setCentralWidget(canvasbutton)
    window.show()
    app.exec() 
    
    
if __name__ == "__main__":
    args = sys.argv
    main()
    print("execution du programme")