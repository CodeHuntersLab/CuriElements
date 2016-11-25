from PyQt5.QtCore import (QRect, QSize, Qt)
from PyQt5.QtGui import (QFont, QFontDatabase, QIcon, QPainter)
from PyQt5.QtWidgets import (QPushButton, )


class CuriButton(QPushButton):
    def __init__(self, size, colors, parent=None):
        super(CuriButton, self).__init__(parent)
        self.setFixedSize(size)  # size = QSize(20, 30) QPoint(20, 30)
        self.setFlat(True)
        self.setStyleSheet("QPushButton {{background-color:{ncolor}; border-radius: 2px; border: 4px solid #00000000;}}"
                           "QPushButton:focus {{ background-color:{ncolor};border: 2px solid {pcolor}}}"
                           "QPushButton:pressed {{background-color: {ncolor};}}"
                           "QPushButton:hover {{ background-color: {pcolor};}}"
                           .format(ncolor=colors[0].name(), pcolor=colors[1].name()))


class ElementButton(CuriButton):
    def __init__(self, size, color, number, symbol, description, parent=None):
        super(ElementButton, self).__init__(size, color, parent)
        self.number = number
        self.symbol = symbol
        self.description = description
        id_font = QFontDatabase.addApplicationFont(":YanoneKaffeesatz-Regular")
        self.family = QFontDatabase.applicationFontFamilies(id_font)[0]

    def paintEvent(self, event):
        super().paintEvent(event)
        width = self.size().width()
        height = self.size().height()
        painter = QPainter(self)
        painter.setPen(Qt.white)

        painter.setFont(QFont(self.family, height / 2))
        painter.drawText(QRect(width / 6, height / 5, 7 * width / 10, 7 * height / 10),
                         Qt.AlignBottom | Qt.AlignRight, self.symbol)

        painter.setFont(QFont(":pokemonSolid", height / 6))
        painter.drawText(QRect(width / 10, height / 10, 7 * width / 10, height / 2), Qt.AlignTop | Qt.AlignLeft,
                         str(self.number))


class DescriptionButton(CuriButton):
    def __init__(self, size, color, parent=None):
        super(DescriptionButton, self).__init__(size, [color, color], parent)

    def updateBackground(self, img):
        icon = QIcon(img)
        self.setIcon(icon)
        self.setIconSize(QSize(self.width(), self.height()))
