from PyQt5.QtWidgets import QApplication

from Atoms import Atoms

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setApplicationName('Atoms')
    app.setApplicationDisplayName('Atoms')
    app.setOrganizationName('CodeHunters')
    app.setOrganizationDomain('CodeHunters.com')
    app.setApplicationVersion('1.0')
    w = Atoms()
    w.show()
    sys.exit(app.exec_())
