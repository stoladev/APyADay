"""
The main file to execute for the employee client.
"""

import sys

from PyQt5.QtWidgets import QApplication, QDialog

from employee_client.employee_login_window import EmployeeLoginWindow
from employee_client.employee_window import EmployeeMainWindow

if __name__ == "__main__":

    app = QApplication(sys.argv)
    employee_login_window = EmployeeLoginWindow()

    if employee_login_window.exec_() == QDialog.Accepted:
        employee_main_window = EmployeeMainWindow()
        employee_main_window.show()

    # TODO
    # Close process on app exit.
    sys.exit(app.exec())
