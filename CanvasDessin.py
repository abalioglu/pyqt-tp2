from PyQt5.QtWidgets import *

class CanvasDessin(QWidget):
    def _init_(self):
        super().__init__()
        self.setMinimumSize(100)
        self.list = list()
    def press(self,event):
        list.append(event.pos())
        self.update
        