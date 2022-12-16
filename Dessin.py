import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from CanvasDessin import CanvasDessin

class Dessin(QMainWindow):
    canvasd = CanvasDessin()
    def __init__(self):
        super().__init__()
        self.resize(300,200)
        self.setCentralWidget(self.canvasd)
    
def main():
    app = QApplication(sys.argv)
    window = Dessin()
    window.show()
    app.exec() 
    
    
if __name__ == "__main__":
    args = sys.argv
    main()
    print("execution du programme")