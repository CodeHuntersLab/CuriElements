import os

from PyQt5.QtCore import (QFile, QPoint, QRect, QSize, Qt, qrand, pyqtSlot)
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import (QIcon, QColor, QPainter, QPixmap, QRegion)
from PyQt5.QtWidgets import (qApp, QAction, QMessageBox, QWidget)
from gtts import gTTS

from PyQt5.QtCore import (QFile, QIODevice)
from PyQt5.QtMultimedia import (QMediaContent, QMediaPlayer)

from Atoms import Atoms
from CuriButton import CuriButton


class Background(QWidget):
    def __init__(self, parent=None):
        super(Background, self).__init__(parent, Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)

        self.player = QMediaPlayer(self,  QMediaPlayer.StreamPlayback)

        self.dragPosition = QPoint()
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        quitAction = QAction("E&xit", self, icon=QIcon(":close"), shortcut="Ctrl+Q", triggered=qApp.quit)
        self.addAction(quitAction)
        aboutAction = QAction("A&bout", self, icon=QIcon(":qt"), shortcut="Ctrl+A", triggered=self.about)
        self.addAction(aboutAction)
        side = 40
        self.setFixedSize(side * QSize(30, 15))
        self.setWindowIcon(QIcon(":codehunters"))

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

        self.atoms = Atoms(self)
        self.atoms.setGeometry(QRect(1.5 * side, 1.5 * side, 7 * side, 7 * side))
        self.setMask(region)

        offset = QPoint(10 * side, 3 * side)
        file = QFile(":elements")
        file.open(QFile.ReadOnly | QFile.Text)

        n = 0

        while not file.atEnd():
            x, y, text = file.readLine().split(',')
            coordinate = QPoint(int(x), int(y))
            n += 1
            btn = CuriButton(QSize(side, side), n, bytearray(text).decode(), self)
            btn.move(offset + coordinate * side)
            btn.setText("{}, {}".format(coordinate.x(), coordinate.y()))
            color = QColor(qrand() % 256, qrand() % 256, qrand() % 256)
            btn.setStyleSheet('background: rgb({}, {}, {});'.format(color.red(), color.green(), color.blue()))
            btn.clicked.connect(self.button_clicked)
        # btnSound = CuriButton(QSize(2*side, 2*side), self)
        # btnSound.move(11*side, 12*side)

    def test(self, text):
        self.player.stop()
        filename = os.path.dirname(os.path.realpath(__file__)) + "/Curie.mp3"
        tts = gTTS(text=text, lang='es')
        tts.save(filename)
        media = QMediaContent(QUrl.fromLocalFile(filename))
        self.player.setMedia(media)
        self.player.play()

    @pyqtSlot()
    def button_clicked(self):
        self.atoms.update_number(self.sender().id)
        self.test(self.sender().text)

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


import resource_rc
