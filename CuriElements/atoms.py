from math import pi, cos, sin

from PyQt5.QtCore import (QParallelAnimationGroup, QPointF, QPropertyAnimation, QRectF, Qt, qrand, qsrand, QTime)
from PyQt5.QtGui import (QBrush, QColor, QPen, QPainterPath, QTransform, QRadialGradient)
from PyQt5.QtWidgets import (QGraphicsObject, QGraphicsScene, QGraphicsView)


class Atoms(QGraphicsView):
    def __init__(self, parent=None):
        super(Atoms, self).__init__(parent)
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 150, 150)
        self.group = QParallelAnimationGroup(self)
        self.center = QPointF(75, 75)

        gradient = QRadialGradient(self.center, 150)
        gradient.setColorAt(0.9, QColor(0, 0, 0))
        gradient.setColorAt(0.6, QColor("#002e5b"))
        gradient.setColorAt(0.1, QColor(0, 0, 0))
        gradient.setColorAt(0, QColor("#fde428"))

        self.setBackgroundBrush(QBrush(gradient))
        self.setScene(self.scene)

    def update_number(self, n):
        self.group.stop()
        self.group = QParallelAnimationGroup(self)
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 150, 150)
        now = QTime.currentTime()
        qsrand(now.msec())

        a, b = 75, 20
        transform = QTransform()
        transform.translate(self.center.x(), self.center.y())

        alpha = 180 / n

        p = 60
        path = QPainterPath()
        path.addEllipse(QPointF(0, 0), a, b)

        # Lookup table
        points = [QPointF(a * cos(2 * pi * i / p), b * sin(2 * pi * i / p)) for i in range(p)]

        for j in range(n):
            color = QColor(qrand() % 255, qrand() % 255, qrand() % 255)

            transform.rotate(alpha)
            self.scene.addPath(transform.map(path), QPen(color))

            # number % p => 0:p-1
            initial = (qrand() % p)

            l = [(i / (p - 1), transform.map(points[(i + initial) % p])) for i in range(p)]

            item = ElectronObject(color=color)
            animation = QPropertyAnimation(item, b'pos')
            animation.setKeyValues(l)
            animation.setDuration(2000)
            self.group.addAnimation(animation)
            self.scene.addItem(item)

        self.group.start()
        self.group.finished.connect(self.group.start)

        self.setScene(self.scene)

    def stop(self):
        self.group.stop()


class ElectronObject(QGraphicsObject):
    def __init__(self, parent=None, color=Qt.red):
        super(ElectronObject, self).__init__(parent)
        self.color = color

    def paint(self, painter, option, widget):
        pen = QPen(self.color, 1)
        rect = self.boundingRect()
        gradient = QRadialGradient(rect.center(), rect.width())
        gradient.setColorAt(0.7, self.color)
        gradient.setColorAt(0, QColor(255, 255, 255))
        brush = QBrush(gradient)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawEllipse(rect)

    def boundingRect(self):
        return QRectF(0, 0, 6, 6)
