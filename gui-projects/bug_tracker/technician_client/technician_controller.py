import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from technician_client.modules.loaders import menu_loader
from technician_client.modules.managers import action_manager, keypress_manager
from technician_client.technician_model import Model
from technician_client.technician_view import LoginView, MainView


class TechnicianController:
    def __init__(self):
        self.login_window = QtWidgets.QDialog()
        self.main_window = None
        self.model = Model(self.login_window)
        self.view = LoginView(self.login_window, self.model)

    def run(self):
        if self.login_window.exec_() == QtWidgets.QDialog.Accepted:
            self.main_window = MainWindow()
            self.model = Model(self.main_window)
            self.view = MainView(self.main_window, self.model)


# TODO
# Create a LoginWindow class to replace above init
# Move below class to separate files


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, event):
        """
        Overrides context menu events to load the account table's menu.
        """

        menu_loader.load_accounts_menu(self, event)

    def keyPressEvent(self, event):
        """
        Overrides key press events to check for special key presses.
        """

        keypress_manager.check_keypress(self, event)

    def mouseDoubleClickEvent(self, event) -> None:
        """
        Overrides the double click event to check for any opening actions.
        """

        mouse_on_graphics_view = self.root.screenshot_view.underMouse()
        if mouse_on_graphics_view:
            action_manager.open_large_viewer(self.root)

    # technician_login_window = TechnicianLoginWindow()
    #
    #     run_main_window()
    # else:
    #     return
    #
    # print("loaded")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = TechnicianController()
    c.run()
    sys.exit(app.exec_())
