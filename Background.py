from PyQt5.QtCore import (QPoint, QSize, Qt, QRect)
from PyQt5.QtGui import (QPainter, QPixmap, QRegion)
from PyQt5.QtWidgets import (QAction, QWidget, qApp,QPushButton)

from Atoms import Atoms


class BackGround(QWidget):
    def __init__(self, parent=None):
        super(BackGround, self).__init__(parent, Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)
        self.dragPosition = QPoint()
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        quitAction = QAction("E&xit", self, shortcut="Ctrl+Q", triggered=qApp.quit)
        self.addAction(quitAction)
        side = 40
        self.setFixedSize(side * QSize(30, 15))

        region = QRegion(QRect(0, 0, 2 * side, 2 * side), QRegion.Ellipse)
        region += QRegion(QRect(side, 0, 8 * side, 15 * side))
        region += QRegion(QRect(0, side, side, 13 * side))
        region += QRegion(QRect(0, 13 * side, 2 * side, 2 * side), QRegion.Ellipse)
        region += QRegion(QRect(9 * side, side, side, 14 * side))
        region += QRegion(QRect(8 * side, 0, 2 * side, 2 * side), QRegion.Ellipse)
        region += QRegion(QRect(10 * side, 2 * side, 19 * side, 13 * side))
        region += QRegion(QRect(28 * side, 2*side, 2 * side, 2 * side), QRegion.Ellipse)
        region += QRegion(QRect(29 * side, 3 * side, side, 11*side))
        region += QRegion(QRect(28 * side, 13 * side, 2 * side, 2 * side), QRegion.Ellipse)

        self.atoms = Atoms(self)
        self.atoms.setGeometry(QRect(2*side, 2*side, 6*side, 6*side))
        self.btn2 = QPushButton("OLA K ASE", self)
        self.btn2.setGeometry(QRect(2 * side, 9 * side, 6 * side, 4 * side))
        self.setMask(region)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), QPixmap("background.png"))
