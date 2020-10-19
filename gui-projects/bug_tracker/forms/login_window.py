from PyQt5 import QtCore, QtWidgets
from forms.main_window import Ui_main_window
import sys


# noinspection PyAttributeOutsideInit,PyMethodMayBeStatic,PyShadowingNames


class Ui_login_window(object):
    def setupUi(self, login_window):
        login_window.setObjectName("login_window")
        login_window.setEnabled(True)
        login_window.setFixedSize(300, 160)

        # GENERAL SIZING
        size = QtWidgets.QSizePolicy
        size_policy = QtWidgets.QSizePolicy(size.Fixed, size.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(login_window.sizePolicy().hasHeightForWidth())
        login_window.setSizePolicy(size_policy)

        self.central_widget = QtWidgets.QWidget(login_window)
        self.central_widget.setObjectName("central_widget")
        login_window.setCentralWidget(self.central_widget)

        self.login_line = QtWidgets.QLineEdit(self.central_widget)
        self.login_line.setObjectName(u"login_line")
        self.login_line.setGeometry(QtCore.QRect(10, 30, 281, 24))

        self.password_line = QtWidgets.QLineEdit(self.central_widget)
        self.password_line.setObjectName(u"password_line")
        self.password_line.setGeometry(QtCore.QRect(10, 60, 281, 24))
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login_button = QtWidgets.QPushButton(self.central_widget)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QtCore.QRect(210, 130, 80, 24))

        self.translate_ui(login_window)
        self.state_update()
        QtCore.QMetaObject.connectSlotsByName(login_window)

    def translate_ui(self, login_window):
        _translate = QtCore.QCoreApplication.translate
        login_window.setWindowTitle(_translate("login_window", "Bug Reporter 9001"))
        self.login_line.setPlaceholderText(_translate("login_window", u"Employee ID", None))
        self.password_line.setPlaceholderText(_translate("login_window", u"Password", None))
        self.login_button.setText(_translate("login_window", u"Login", None))

    def state_update(self):
        self.login_button.clicked.connect(self.verify_login)

    def verify_login(self):
        if self.login_line.text() == "stoladev" and self.password_line.text() == "password":
            print("Login Successful.")
            load_main_window()
            QtWidgets.QApplication.quit()
        else:
            print("Login Failed.")


def load_main_window():
    main_app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_ui = Ui_main_window()
    main_ui.setupUi(main_window)
    main_ui.update_preview()
    main_window.show()
    main_app.exec_()
