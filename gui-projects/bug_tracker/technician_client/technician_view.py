from PyQt5 import QtWidgets


class View:
    def __init__(self, root, model):
        root.setWindowTitle("Technician Login")

        # Initializations
        self.technician_login_line = QtWidgets.QLineEdit(root)
        self.technician_password_line = QtWidgets.QLineEdit(root)
        self.technician_login_button = QtWidgets.QPushButton(root)
        self.technician_label = QtWidgets.QLabel(root)

        # Text Lines
        self.technician_login_line.setPlaceholderText("Username/Email Address")
        self.technician_password_line.setPlaceholderText("Password")
        self.technician_password_line.setEchoMode(QtWidgets.QLineEdit.Password)

        # Buttons
        self.technician_login_button.setText("Login")
        # self.technician_login_button.clicked.connect(self.verify_technician)

        layout = QtWidgets.QVBoxLayout(root)
        layout.addWidget(self.technician_login_line)
        layout.addWidget(self.technician_password_line)
        layout.addWidget(self.technician_login_button)

        root.show()
