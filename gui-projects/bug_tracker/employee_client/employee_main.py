"""
The main file to execute for the employee client.
"""

import sys

from PyQt5.QtWidgets import QApplication, QDialog

from employee_client.employee_login_window import EmployeeLoginWindow
from employee_client.employee_window import EmployeeMainWindow


def run_login_window(app_in_use):
    """
    Runs the login verification process through the technician's login window class.

    :return: The main technician window if login verification is successful. Otherwise, cancels.
    """

    employee_login_window = EmployeeLoginWindow()

    if employee_login_window.exec_() == QDialog.Accepted:
        run_main_window()
    else:
        return

    # sys.exit(app_in_use.exec_())


def run_main_window():
    """
    Runs the main technician client through the technician's main window class.

    :return: All data associated with the MongoDB connected to.
    """

    employee_main_window = EmployeeMainWindow()
    employee_main_window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":

    app = QApplication(sys.argv)
    employee_login_window = EmployeeLoginWindow()

    if employee_login_window.exec_() == QDialog.Accepted:
        employee_main_window = EmployeeMainWindow()
        employee_main_window.show()

    sys.exit(app.exec())
