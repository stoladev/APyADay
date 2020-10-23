import sys

from PyQt5.QtWidgets import QApplication

from technician_client.client_window import TechnicianMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = TechnicianMainWindow()
    sys.exit(app.exec())
