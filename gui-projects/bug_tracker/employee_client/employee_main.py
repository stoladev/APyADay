"""
The main file to execute for the employee client.
"""

import sys

from PyQt5.QtWidgets import QApplication

from employee_client.employee_login_window import LoginWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    sys.exit(app.exec())
