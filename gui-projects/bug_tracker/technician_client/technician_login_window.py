# TODO
# Simplify MongoDB load and make it more secure.

from PyQt5.QtWidgets import (
    QDialog,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)

from technician_client.modules.managers import verification_manager


class TechnicianLoginWindow(QDialog):
    def __init__(self, parent=None):
        super(TechnicianLoginWindow, self).__init__(parent)

        # Initializations
        self.setWindowTitle("Technician Login")
        self.technician_login_line = QLineEdit(self)
        self.technician_password_line = QLineEdit(self)
        self.technician_login_button = QPushButton(self)
        self.technician_label = QLabel(self)

        # Text Lines
        self.technician_login_line.setPlaceholderText("Username/Email Address")
        self.technician_password_line.setPlaceholderText("Password")
        self.technician_password_line.setEchoMode(QLineEdit.Password)

        # Buttons
        self.technician_login_button.setText("Login")
        self.technician_login_button.clicked.connect(self.verify_technician)

        layout = QVBoxLayout(self)
        layout.addWidget(self.technician_login_line)
        layout.addWidget(self.technician_password_line)
        layout.addWidget(self.technician_login_button)

    def verify_technician(self):
        verification_manager.verify_technician(self)
