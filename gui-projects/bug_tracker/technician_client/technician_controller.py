import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from technician_client.technician_model import Model
from technician_client.technician_view import View


class TechnicianController:
    def __init__(self):
        self.root = QtWidgets.QDialog()
        self.model = Model()
        self.view = View(self.root, self.model)

    @staticmethod
    def run():
        sys.exit(app.exec_())

    # technician_login_window = TechnicianLoginWindow()
    #
    # if technician_login_window.exec_() == QDialog.Accepted:
    #     run_main_window()
    # else:
    #     return
    #
    # print("loaded")
    # technician_main_window = TechnicianMainWindow()
    # technician_main_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = TechnicianController()
    c.run()
