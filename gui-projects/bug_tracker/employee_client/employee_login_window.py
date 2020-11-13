"""
Handles the login process of an employee, verifying their information with MongoDB, proceeding to
open the main program after successful verification.
"""
import pymongo
from PyQt5.QtWidgets import (
    QDialog,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
)

from employee_client.modules.managers import verification_manager


class EmployeeLoginWindow(QDialog):
    """
    Handles the initiation of the login window used to log in the employee.
    """

    def __init__(self):
        super().__init__()
        # super(EmployeeLoginWindow, self).__init__(parent)

        # Initializations
        self.setWindowTitle("Employee Login")
        self.employee_login_line = QLineEdit(self)
        self.employee_password_line = QLineEdit(self)
        self.employee_login_button = QPushButton(self)
        self.employee_label = QLabel(self)

        # Text Lines
        self.employee_login_line.setPlaceholderText("Account Name/Email Address")
        self.employee_password_line.setPlaceholderText("Password")
        self.employee_password_line.setEchoMode(QLineEdit.Password)

        # Buttons
        self.employee_login_button.setText("Login")
        self.employee_login_button.clicked.connect(self.verify_employee)

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.employee_login_line)
        layout.addWidget(self.employee_password_line)
        layout.addWidget(self.employee_login_button)

        # MongoDB Connection
        mongodb_url = open("../mongo_cluster.txt", "r")
        connection = mongodb_url.read()
        cluster = pymongo.MongoClient(connection)
        self.database = cluster["bug_tracker_db"]

    def verify_employee(self):
        """
        Verifies the login information using MongoDB for the employee login.

        :return: A success or fail result upon verification.
        """

        account_name = self.employee_login_line.text()
        password = self.employee_password_line.text()

        account_list = self.database.accounts
        account = account_list.find_one({"account_name": account_name})

        print(account_name)

        if account:
            verification_manager.verify_employee(self, account, password)
        else:
            QMessageBox.warning(self, "No Match", "No matching account found.")
