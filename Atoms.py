# -*- coding: utf-8 -*-

"""
Module implementing Atoms.
"""
from math import pi, cos, sin

from PyQt5.QtCore import (QParallelAnimationGroup, QPointF, QPropertyAnimation, QRectF, Qt, qrand, qsrand, QTime)
from PyQt5.QtGui import (QBrush, QColor, QPen, QPainterPath, QTransform, QRadialGradient)
from PyQt5.QtWidgets import (QGraphicsObject, QGraphicsScene, QGraphicsView)


class Atoms(QGraphicsView):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Atoms, self).__init__(parent)
        scene = QGraphicsScene()

        scene.setSceneRect(0, 0, 150, 150)
        n = 4
        group = QParallelAnimationGroup(self)
        now = QTime.currentTime()
        qsrand(now.msec())

        center = QPointF(75, 75)
        a, b = 75, 20
        transform = QTransform()
        transform.translate(center.x(), center.y())

        alpha = 180 / n

        p = 60
        path = QPainterPath()
        path.addEllipse(QPointF(0, 0), a, b)

        # Lookup table
        points = [QPointF(a * cos(2 * pi * i / p), b * sin(2 * pi * i / p)) for i in range(p)]

        for j in range(n):
            color = QColor(qrand() % 255, qrand() % 255, qrand() % 255)

            transform.rotate(alpha)
            scene.addPath(transform.map(path), QPen(color))

            # number % p => 0:p-1
            initial = (qrand() % p)

            l = [(i / (p - 1), transform.map(points[(i + initial) % p])) for i in range(p)]

            item = CircleObject(color=color)
            animation = QPropertyAnimation(item, b'pos')
            animation.setKeyValues(l)
            animation.setDuration(2000)
            group.addAnimation(animation)
            scene.addItem(item)

        group.start()
        group.finished.connect(group.start)
        self.setScene(scene)

        gradient = QRadialGradient(center, 150)
        gradient.setColorAt(0.9, QColor(0, 0, 0))
        gradient.setColorAt(0.6, QColor(255, 0, 0))
        gradient.setColorAt(0.1, QColor(0, 0, 0))
        gradient.setColorAt(0, QColor(0, 200, 0))

        self.setBackgroundBrush(QBrush(gradient))


class CircleObject(QGraphicsObject):
    def __init__(self, parent=None, color=Qt.red):
        super(CircleObject, self).__init__(parent)
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
