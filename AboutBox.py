from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QMessageBox, QTextEdit)


class CodeHuntersBox(QMessageBox):
    def __init__(self, parent=None):
        super(CodeHuntersBox, self).__init__(parent=parent)
        self.setIconPixmap(QPixmap(":codehunters"))
        self.setStyleSheet("QLabel{min-width:300 px;}")
        urlgithub = 'https://github.com/CodeHuntersLab'
        urlfacebook = 'https://www.facebook.com/CodeHuntersLab'
        text = "<H1>CodeHunters Lab</H1>" \
               "<p> Comunidad que desarrolla actividades orientadas a la formación en investigación y" \
               " creación tecnológica, dirigidas a jóvenes entre 15 y 20 años.</p> " \
               "<p>Búscanos en: </p>" \
               "<p><a href=\"{github}\"> <img src=\":github\" height=\"20\"></a></p>" \
               "<p><a href=\"{facebook}\"> <img src=\":facebook\" height=\"20\"></a></p>" \
            .format(github=urlgithub, facebook=urlfacebook)

        self.setInformativeText("© 2016 CodeHunters Lab")
        self.setText(text)
        self.setWindowTitle(self.tr("Acerca de CodeHunterLab"))

    def resizeEvent(self, event):
        result = super(CodeHuntersBox, self).resizeEvent(event)
        details_box = self.findChild(QTextEdit)
        if details_box is not None:
            details_box.setFixedSize(details_box.sizeHint())
        return result
