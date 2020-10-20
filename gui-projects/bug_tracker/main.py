from PyQt5 import QtCore, QtGui

import sys
from PyQt5.QtWidgets import QApplication

from forms.login_window import LoginWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    sys.exit(app.exec())
