from PyQt5.QtCore import QRect
from PyQt5.QtGui import QRegion
from PyQt5.QtWidgets import QPushButton


class CuriButton(QPushButton):
    def __init__(self, size, parent=None,):
        super(CuriButton, self).__init__(parent)
        self.setFixedSize(size)
        w = size.width()
        h = size.height()
        region = QRegion(QRect(0, 0, w/2, h/2), QRegion.Ellipse)
        region += QRegion(QRect(w/4, 0, w/2, h), QRegion.Rectangle)
        region += QRegion(QRect(w/2, 0, w / 2, h / 2), QRegion.Ellipse)
        region += QRegion(QRect(0, h/2, w / 2, h / 2), QRegion.Ellipse)
        region += QRegion(QRect(w/2, h / 2, w / 2, h / 2), QRegion.Ellipse)
        region += QRegion(QRect(0, h/4, w, h/2), QRegion.Rectangle)
        self.setMask(region)