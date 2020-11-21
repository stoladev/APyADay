"""
The main file to execute for the technician client.
"""

# pylint: disable=import-error
# Reason: Importing is working fine, but pylint begs to differ. Most likely because of venv.

import sys

from PyQt5.QtWidgets import QApplication, QDialog

from technician_client.technician_login_window import TechnicianLoginWindow
from technician_client.technician_window import TechnicianMainWindow


def run_login_window():
    """
    Runs the login verification process through the technician's login window class.

    :return: The main technician window if login verification is successful. Otherwise, cancels.
    """

    technician_login_window = TechnicianLoginWindow()

    if technician_login_window.exec_() == QDialog.Accepted:
        run_main_window()
    else:
        return


def run_main_window():
    """
    Runs the main technician client through the technician's main window class.

    :return: All data associated with the MongoDB connected to.
    """

    print("loaded")
    technician_main_window = TechnicianMainWindow()
    technician_main_window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # run_login_window()
    run_main_window()
