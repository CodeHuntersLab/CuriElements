from PyQt5.QtCore import (QFile, QIODevice)
from PyQt5.QtMultimedia import (QMediaContent, QMediaPlayer)
from PyQt5.QtWidgets import (QApplication, QWidget)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    player = QMediaPlayer(None)
    file = QFile("hello.mp3")
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
