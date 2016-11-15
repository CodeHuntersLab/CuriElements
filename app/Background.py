import os

from PyQt5.QtCore import (QFile, QPoint, QRect, QSize, Qt, QUrl, pyqtSlot)
from PyQt5.QtGui import (QIcon, QColor, QPainter, QPixmap, QRegion)
from PyQt5.QtMultimedia import (QMediaContent, QMediaPlayer)
from PyQt5.QtWidgets import (qApp, QAction, QMessageBox, QWidget)
from gtts import gTTS
from wikipedia import wikipedia

from app.Atoms import Atoms
from app.CodeHuntersBox import CodeHuntersBox
from app.CuriButton import ElementButton, CuriButton


class Background(QWidget):
    def __init__(self, parent=None):
        super(Background, self).__init__(parent, Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)
        self.player = QMediaPlayer(self, QMediaPlayer.StreamPlayback)
        self.dragPosition = QPoint()
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        quitAction = QAction("Salir", self, icon=QIcon(":close"), shortcut="Ctrl+Q", triggered=qApp.quit)
        self.addAction(quitAction)
        aboutAction = QAction("Acerca de Qt", self, icon=QIcon(":qt"), shortcut="Ctrl+A", triggered=self.about)
        self.addAction(aboutAction)
        codehunterAction = QAction("Acerca de Codehunters", self, icon=QIcon(":codehunters"), shortcut="Ctrl+I",
                                   triggered=self.codehunters)
        self.addAction(codehunterAction)

        side = 40
        self.setFixedSize(side * QSize(30, 15))
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

        while not file.atEnd():
            x, y, name, symbol, electron, description, description2 = file.readLine().split(',')
            coordinate = QPoint(int(x), int(y))

            # text = "El {name} cuyo simbolo químico es {symbol} tiene {electron} electrones y protones. {description}" \
            #     .format(name=bytearray(name).decode(),
            #             symbol=self.getSymbol(bytearray(symbol).decode()),
            #             electron=bytearray(electron).decode(),
            #             description=" ")

            text = bytearray(name).decode()
            btn = ElementButton(QSize(side, side), ":{number}.{symbol}.0"
                                .format(symbol=bytearray(symbol).decode(),
                                        number=bytearray(electron).decode()),
                                QColor("#002e5b"),
                                int(electron),
                                bytearray(symbol).decode(),
                                text, self)
            btn.move(offset + coordinate * side)
            btn.clicked.connect(self.button_clicked)
        self.imageDescription = CuriButton(side * QSize(7, 4), "", QColor("#002e5b"), self)
        self.imageDescription.move(1.5 * side, 9 * side)
        btnSound = CuriButton(side * QSize(2, 2), ":soundOn", QColor("#002e5b"), self)
        btnSound.move(11 * side, 12 * side)
        btnSound.clicked.connect(self.sound_clicled)

        self.button = None

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
        self.player.stop()
        wikipedia.set_lang("es")
        text = wikipedia.summary(name, sentences=1)
        # print(text)
        filename = os.path.dirname(os.path.realpath(__file__)) + "/Curie.mp3"
        # os.remove(filename)
        print(text)
        tts = gTTS(text=text, lang='es')
        tts.save(filename)
        media = QMediaContent(QUrl.fromLocalFile(filename))
        self.player.setMedia(media)
        self.player.play()

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
        self.player.stop()
        super().closeEvent(event)

import app.resource_rc