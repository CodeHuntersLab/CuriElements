from PyQt5.QtWidgets import QPushButton


class CuriButton(QPushButton):
    def __init__(self, size, image, color, parent=None):
        super(CuriButton, self).__init__(parent)
        self.setFixedSize(size)  # size = QSize(20, 30) QPoint(20, 30)
        # self.setFlat(True)
        self.setStyleSheet("QPushButton {{background-image:url({img}); border-style: solid;}} "
                           "QPushButton:focus {{ background-color: rgb(253, 228, 40);}}"
                           "QPushButton:hover {{ background-color: rgb({cred}, {cgreen}, {cblue});}}"
                           "QPushButton:pressed {{background-color: rgb(253, 228, 40);"
                           " padding-top: -15px;padding-bottom: -17px;}}"
                           .format(img=image, cred=color.red(), cgreen=color.green(), cblue=color.blue()))


class ElementButton(CuriButton):
    def __init__(self, size, image, color, number, description, parent=None):
        super(ElementButton, self).__init__(size, image, color, parent)
        self.number = number
        self.description = description
