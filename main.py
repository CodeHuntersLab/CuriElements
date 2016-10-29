from PyQt5.QtWidgets import QApplication

from Background.Background import BackGround

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setApplicationName('CuriElements')
    app.setApplicationDisplayName('CuriElements')
    app.setOrganizationName('CodeHuntersLab')
    app.setOrganizationDomain('CodeHuntersLab.com')
    app.setApplicationVersion('1.0')
    w = BackGround()
    w.show()
    sys.exit(app.exec_())