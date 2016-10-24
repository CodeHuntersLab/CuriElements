# -*- coding: utf-8 -*-

"""
Module implementing Atoms.
"""
from math import pi, cos, sin

from PyQt5.QtCore import (QParallelAnimationGroup, QPointF, QPropertyAnimation, QRectF, Qt, qrand, qsrand, QTime)
from PyQt5.QtGui import (QBrush, QColor, QPen, QPainterPath, QTransform)
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
        n = 4
        group = QParallelAnimationGroup(self)
        now = QTime.currentTime()
        qsrand(now.msec())

        center = QPointF(100, 100)
        a, b = 100, 20
        transform = QTransform()
        transform.translate(center.x(), center.y())

        alpha = 180 / n

        p = 30
        path = QPainterPath()
        path.addEllipse(QPointF(0, 0), a, b)

        for j in range(n):
            color = QColor(qrand() % 255, qrand() % 255, qrand() % 255)

            transform.rotate(alpha)
            scene.addPath(transform.map(path), QPen(color))

            initial = (qrand() % 360) * pi / 180
            l = []
            for i in range(p):
                angle = 2 * pi * i / p + initial
                point = transform.map(QPointF(a * cos(angle), b * sin(angle)))
                l.append((i / (p - 1), point))

            item = CircleObject(color=color)
            animation = QPropertyAnimation(item, b'pos')
            animation.setKeyValues(l)
            animation.setDuration(2000)
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
