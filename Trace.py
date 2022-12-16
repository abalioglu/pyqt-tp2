from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Trace():
    def __init__(self):
        super().__init__()
        self.points = list()
        self.width = 10
        self.color = QColor('black')