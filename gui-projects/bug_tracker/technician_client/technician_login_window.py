import bcrypt
from PyQt5.QtWidgets import (
    QDialog,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
)

from modules.mongo_connection import cluster


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
        username = self.technician_login_line.text()
        password = self.technician_password_line.text()

        db = cluster["bug_tracker_db"]
        accounts = db.technicians

        account = accounts.find_one({"username": username})

        if account:
            key = password.encode("utf-8")
            salt = account["password"]
            lock = account["password"]
            if bcrypt.hashpw(key, salt) == lock:
                self.accept()
            else:
                QMessageBox.warning(self, "Error", "Password incorrect.")
