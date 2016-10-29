from PyQt5.QtWidgets import QApplication

from Background import Background

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setApplicationName('CURIElements')
    app.setApplicationDisplayName('CURIElements')
    app.setOrganizationName('CodeHuntersLab')
    app.setOrganizationDomain('CodeHuntersLab.com')
    app.setApplicationVersion('1.0')
    w = Background()
    w.show()
    sys.exit(app.exec_())