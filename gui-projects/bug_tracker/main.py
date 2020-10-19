from PyQt5 import QtCore, QtGui, QtWidgets

from forms.login_window import Ui_login_window


def load_login_window():
    login_window = QtWidgets.QMainWindow()
    login_ui = Ui_login_window()
    login_ui.setupUi(login_window)
    login_window.show()
    login_app.exec_()




if __name__ == "__main__":
    import sys
    login_app = QtWidgets.QApplication(sys.argv)

    load_login_window()
