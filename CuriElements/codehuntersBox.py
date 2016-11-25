from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox


class CodeHuntersBox(QMessageBox):
    def __init__(self, parent=None):
        super(CodeHuntersBox, self).__init__(parent=parent)

        self.dragPosition = QPoint()

        urlgithub = 'https://github.com/CodeHuntersLab'
        urlfacebook = 'https://www.facebook.com/CodeHuntersLab'
        mail = 'hola@codehunterslab.com'

        text = "<H1><font color=#fde428>Code</font><font color=#002e5b>Hunters</font> Lab</H1>" \
               "<H2>Laboratorio de Creación Tecnológica</H2>" \
               "<H3>Carabayllo, Lima, Perú</H3>" \
               "<p> Comunidad que desarrolla actividades orientadas a la formación en investigación y" \
               " creación tecnológica, dirigidas a jóvenes entre 15 y 20 años.</p> " \
               "<H4>Búsquenos en:</H4>" \
               "<p><a href=\"{facebook}\"><img src=\":facebook\" height=\"20\"></a> " \
               "<a href=\"{github}\"><img src=\":github\" height=\"20\"></a></p>" \
               "¿Quieres saber más de nosotros?" \
               "<H4>Escríbenos:</H4>" \
               "<p><a href=\"mailto:{mail}\">{mail}</a></p>" \
               "<p>© 2016 CodeHunters Lab</p>" \
            .format(github=urlgithub, facebook=urlfacebook, mail=mail)
        self.setWindowTitle(self.tr("Acerca de CodeHunterLab"))
        self.setText(text)
        self.setIconPixmap(QPixmap(":codehunters").scaled(60, 60, Qt.KeepAspectRatio))
        self.setParent(parent)
        self.setWindowFlags(Qt.Window | Qt.WindowSystemMenuHint | Qt.CustomizeWindowHint)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()
