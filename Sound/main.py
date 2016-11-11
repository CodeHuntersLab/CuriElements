from PyQt5.QtCore import (QFile, QIODevice)
from PyQt5.QtMultimedia import (QMediaContent, QMediaPlayer)
from PyQt5.QtWidgets import (QApplication, QWidget)
from gtts import gTTS

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    player = QMediaPlayer(None)
    filename = "Curie.mp3"
    tts = gTTS(text="Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto."
                    " Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500,"
                    " cuando un impresor (N. del T. persona que se dedica a la imprenta) "
                    "desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos"
                    " especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos"
                    " electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación"
                    " de las hojas \"Letraset\", las cuales contenian pasajes de Lorem Ipsum,"
                    " y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker,"
                    " el cual incluye versiones de Lorem Ipsum.", lang='es')
    tts.save(filename)

    file = QFile(filename)
    if file.open(QIODevice.ReadOnly):
        player.setMedia(QMediaContent(), file)
        player.setVolume(100)
        player.play()

    app.setApplicationName('Sound')
    app.setApplicationDisplayName('Sound')
    app.setOrganizationName('CodeHuntersLab')
    app.setOrganizationDomain('CodeHuntersLab.com')
    app.setApplicationVersion('1.0')
    w = QWidget()
    w.show()
    sys.exit(app.exec_())
