from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QWidget,
)

from employee_client.forms.main_window import MainWindow
from modules import mongo_connection


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # GENERAL SETTINGS
        self.setWindowTitle("Login Window")
        self.setEnabled(True)
        self.setFixedSize(300, 100)
        self.main_app = MainWindow()

        # WIDGET INITIALIZATION
        self.central_widget = QWidget(self)
        self.id_line = QLineEdit(self.central_widget)
        self.password_line = QLineEdit(self.central_widget)
        self.login_button = QPushButton(self.central_widget)

        # ACTIVATION
        self.widget_setup()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def sizing_policy_setup(self):
        # SIZING POLICY
        size = QSizePolicy
        size_policy = QSizePolicy(size.Fixed, size.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)

    def widget_setup(self):
        # CENTRAL WIDGET
        self.central_widget.setObjectName("central_widget")
        self.setCentralWidget(self.central_widget)
        # USERNAME FIELD
        self.id_line.setObjectName(u"id_line")
        self.id_line.setGeometry(QtCore.QRect(10, 10, 281, 24))
        self.id_line.returnPressed.connect(self.verify_login)
        self.id_line.setPlaceholderText("Employee ID")
        # PASSWORD FIELD
        self.password_line.setObjectName(u"password_line")
        self.password_line.setGeometry(QtCore.QRect(10, 40, 281, 24))
        self.password_line.setEchoMode(QLineEdit.Password)
        self.password_line.returnPressed.connect(self.verify_login)
        self.password_line.setPlaceholderText("Password")
        # LOGIN BUTTON
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QtCore.QRect(210, 70, 80, 24))
        self.login_button.setText("Login")
        self.login_button.clicked.connect(self.verify_login)

    def verify_login(self):
        username = self.id_line.text()
        password = self.password_line.text()

        if username == "stoladev" and password == "password":

            mongo_connection.verify_user(username, password)
            # print("Login Successful.")
            # self.main_app.show()
            # self.hide()
        else:
            msg = QMessageBox()
            msg.critical(self, "Error!", "Login Failed.")
            msg.exec_()
