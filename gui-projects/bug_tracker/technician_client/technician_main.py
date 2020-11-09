"""
The main file to execute for the technician client.
"""

import sys

from PyQt5.QtWidgets import QApplication, QDialog

from technician_client.technician_login_window import TechnicianLoginWindow
from technician_client.technician_window import TechnicianMainWindow


def run_login_window():
    """
    Runs the login verification process through the technician's login window class.

    :return: The main technician window if login verification is successful. Otherwise, cancels.
    """
    app = QApplication(sys.argv)

    technician_login_window = TechnicianLoginWindow()

    if technician_login_window.exec_() == QDialog.Accepted:
        run_main_window()

    sys.exit(app.exec_())


def run_main_window():
    """
    Runs the main technician client through the technician's main window class.

    :return: All data associated with the MongoDB connected to.
    """
    app = QApplication(sys.argv)

    technician_main_window = TechnicianMainWindow()
    technician_main_window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    run_login_window()
    # run_main_window()
