from os.path import expanduser

from PyQt5.QtCore import (QThread, QUrl, pyqtSlot)
from PyQt5.QtMultimedia import (QMediaContent, QMediaPlayer)
from gtts import gTTS
from wikipedia import wikipedia


class SoundThread(QThread):
    def __init__(self, parent=None):
        super(SoundThread, self).__init__(parent)
        self.name = ""
        home = expanduser("~")
        self.filename = home + "/Curie.mp3"
        wikipedia.set_lang("es")
        self.player = QMediaPlayer(None, QMediaPlayer.StreamPlayback)
        media = QMediaContent(QUrl.fromLocalFile(self.filename))
        self.player.setMedia(media)

    def setName(self, name):
        self.name = name

    @pyqtSlot()
    def run(self):
        print(self.name)
        try:
            text = wikipedia.summary("{}".format(self.name), sentences=2)
        except wikipedia.DisambiguationError as e:
            text = wikipedia.summary("{} químico".format(self.name), sentences=2)
            print(e.options)
        tts = gTTS(text=text, lang='es')
        print(text)
        tts.save(self.filename)
        print("finish")
        self.player.play()
        print("play")

    def stop(self):
        self.player.stop()
