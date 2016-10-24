# -*- coding: utf-8 -*-

"""
Module implementing Atoms.
"""
from math import pi, cos, sin

from PyQt5.QtCore import (QParallelAnimationGroup, QPointF, QPropertyAnimation, QRectF, Qt, qrand, qsrand, QTime)
from PyQt5.QtGui import (QBrush, QColor, QPen)
from PyQt5.QtGui import QPainterPath
from PyQt5.QtGui import QTransform
from PyQt5.QtWidgets import (QGraphicsObject, QGraphicsScene, QWidget)

from Ui_Atoms import Ui_Atoms


class Atoms(QWidget, Ui_Atoms):
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
        self.setupUi(self)
        scene = QGraphicsScene()
        scene.setSceneRect(0, 0, 200, 200)
        n = 12
        group = QParallelAnimationGroup(self)
        now = QTime.currentTime()
        qsrand(now.msec())

        center = QPointF(100, 100)
        a, b = 100, 20
        transform = QTransform()
        transform.translate(center.x(), center.y())

        for j in range(n):
            color = QColor(qrand() % 254, qrand() % 254, qrand() % 254)
            item = CircleObject(color=color)
            animation = QPropertyAnimation(item, b'pos')
            l = []
            initial = (qrand() % 360)*pi/180
            alpha = 180 * j / n

            transform.rotate(alpha)
            alpha *= pi/180
            path = QPainterPath()
            path.addEllipse(QPointF(0, 0), a, b)

            scene.addPath(transform.map(path), QPen(color))

            for i in range(361):
                angle = pi * i / 180 + initial
                x, y = a * cos(angle), b * sin(angle)
                point = QPointF(x * cos(alpha) - y * sin(alpha), x * sin(alpha) + y * cos(alpha))
                l.append((i / 360, center + point))
            animation.setKeyValues(l)
            animation.setDuration(5000)
            group.addAnimation(animation)
            scene.addItem(item)
        group.start()
        group.finished.connect(group.start)
        self.graphicsView.setScene(scene)


class CircleObject(QGraphicsObject):
    def __init__(self, parent=None, color=Qt.red):
        super(CircleObject, self).__init__(parent)
        self.color = color

    def paint(self, painter, option, widget):
        pen = QPen(self.color, 1)
        brush = QBrush(self.color)
        rect = self.boundingRect()
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawEllipse(rect)

    def boundingRect(self):
        return QRectF(0, 0, 5, 5)
