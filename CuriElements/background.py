from PyQt5.QtCore import (QFile, QPoint, QRect, QSize, Qt, pyqtSlot)
from PyQt5.QtGui import (QIcon, QPainter, QPixmap, QRegion)
from PyQt5.QtWidgets import (qApp, QAction, QMessageBox, QWidget)

from CuriElements.atoms import Atoms
from CuriElements.codehuntersBox import CodeHuntersBox
from CuriElements.constants import (blue, yellow, rows, cols)
from CuriElements.cuributton import (ElementButton, DescriptionButton)
from CuriElements.soundthread import SoundThread


class Background(QWidget):
    def __init__(self, parent=None):
        super(Background, self).__init__(parent, Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)

        self.thread = SoundThread(self)
        self.dragPosition = QPoint()
        self.button = None

        w = qApp.desktop().screenGeometry().width()
        h = qApp.desktop().screenGeometry().height()

        side = round((8 / 9) * min(w / cols, h / rows))
        self.setFixedSize(side * QSize(cols, rows))
        self.setWindowIcon(QIcon(":curielements"))

        region = QRegion(QRect(0, 0, 2 * side, 2 * side), QRegion.Ellipse)
        region += QRegion(QRect(side, 0, 8 * side, 15 * side))
        region += QRegion(QRect(0, side, side, 13 * side))
        region += QRegion(QRect(0, 13 * side, 2 * side, 2 * side), QRegion.Ellipse)
        region += QRegion(QRect(9 * side, side, side, 14 * side))
        region += QRegion(QRect(8 * side, 0, 2 * side, 2 * side), QRegion.Ellipse)
        region += QRegion(QRect(10 * side, 2 * side, 19 * side, 13 * side))
        region += QRegion(QRect(28 * side, 2 * side, 2 * side, 2 * side), QRegion.Ellipse)
        region += QRegion(QRect(29 * side, 3 * side, side, 11 * side))
        region += QRegion(QRect(28 * side, 13 * side, 2 * side, 2 * side), QRegion.Ellipse)

        self.setMask(region)

        self.atoms = Atoms(self)
        self.atoms.setGeometry(QRect(1.5 * side, 1.5 * side, 7 * side, 7 * side))

        offset = QPoint(10 * side, 3 * side)
        file = QFile(":elements")
        file.open(QFile.ReadOnly | QFile.Text)
        colors = [blue, yellow]

        while not file.atEnd():
            x, y, name, symbol, electron, description, description2, _ = file.readLine().split(',')
            coordinate = QPoint(int(x), int(y))
            text = bytearray(name).decode()
            btn = ElementButton(QSize(side, side),
                                colors,
                                int(electron),
                                bytearray(symbol).decode(),
                                text, self)
            btn.move(offset + coordinate * side)
            btn.clicked.connect(self.button_clicked)

        self.imageDescription = DescriptionButton(side * QSize(7, 4.5), blue, self)
        self.imageDescription.move(1.5 * side, 9 * side)
        btnSound = DescriptionButton(side * QSize(2, 2), blue, self)
        btnSound.move(11 * side, 12 * side)
        btnSound.updateBackground(":soundOn")
        btnSound.clicked.connect(self.sound_clicled)
        self.addCustomAction()

    def addCustomAction(self):
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        quitAction = QAction("Salir", self, icon=QIcon(":close"), shortcut="Ctrl+Q", triggered=qApp.quit)
        self.addAction(quitAction)
        aboutAction = QAction("Acerca de Qt", self, icon=QIcon(":qt"), shortcut="Ctrl+A", triggered=self.about)
        self.addAction(aboutAction)
        codehunterAction = QAction("Acerca de Codehunters", self, icon=QIcon(":codehunters"), shortcut="Ctrl+I",
                                   triggered=self.codehunters)
        self.addAction(codehunterAction)

    @pyqtSlot()
    def button_clicked(self):
        self.button = self.sender()
        self.atoms.update_number(self.button.number)
        self.imageDescription.updateBackground(":{number}.{symbol}.2".format(symbol=self.button.symbol,
                                                                             number=self.button.number))

    def sound_clicled(self):
        if self.button:
            self.speak(self.button.description)

    def getSymbol(self, symbol):
        return "".join([x + "," for x in symbol])

    def speak(self, name):
        self.thread.stop()
        self.thread.quit()
        self.thread.wait()
        qApp.processEvents()
        self.thread.setName(name)
        self.thread.start()

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
        painter.drawPixmap(self.rect(), QPixmap(":background"))

    def about(self):
        QMessageBox.aboutQt(self, self.tr("Acerca de Qt"))

    def codehunters(self):
        messageBox = CodeHuntersBox(self)
        messageBox.exec_()

    def closeEvent(self, event):
        self.atoms.stop()
        self.thread.quit()
        self.thread.wait()
        # remove(self.filename)
        super().closeEvent(event)

import CuriElements.resource_rc
