import sys

from PyQt5.QtWidgets import QApplication

from technician_client.technician_window import TechnicianMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # technician_login_window = TechnicianLoginWindow()

    # if technician_login_window.exec_() == QDialog.Accepted:
    technician_main_window = TechnicianMainWindow()
    technician_main_window.show()
    sys.exit(app.exec_())

    # app.quitOnLastWindowClosed()
