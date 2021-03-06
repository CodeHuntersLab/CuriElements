"""
 / ___|___   __| | ___| | | |_   _ _ __ | |_ ___ _ __ ___  | |    __ _| |__
| |   / _ \ / _` |/ _ \ |_| | | | | '_ \| __/ _ \ '__/ __| | |   / _` | '_ \
| |__| (_) | (_| |  __/  _  | |_| | | | | ||  __/ |  \__ \ | |__| (_| | |_) |
 \____\___/ \__,_|\___|_| |_|\__,_|_| |_|\__\___|_|  |___/ |_____\__,_|_.__/
"""

from PyQt5.QtWidgets import QApplication
import sys

sys.path.insert(0, "../")

from CuriElements.curiwidget import CuriWidget


def app():
    app = QApplication(sys.argv)
    app.setApplicationName('CuriElements')
    app.setApplicationDisplayName('CuriElements')
    app.setOrganizationName('CodeHuntersLab')
    app.setOrganizationDomain('CodeHuntersLab.com')
    app.setApplicationVersion('1.0')
    w = CuriWidget()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    app()
