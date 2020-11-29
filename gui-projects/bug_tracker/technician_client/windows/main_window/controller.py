"""
Initializes window widgets for the technician application. Points to and runs customizations and
specifications of execution/registered events.
"""

# pylint: disable=import-error
# Reason: Importing is working fine, but pylint begs to differ. Most likely because of venv.

# pylint: disable=invalid-name
# Reason: Invalid names in this case are overrides.

# pylint: disable=unused-argument
# Reason: The event argument that is unused must be called in the function override.


from PyQt5 import QtWidgets

from technician_client.modules.loaders import menu_loader
from technician_client.modules.managers import action_manager, keypress_manager


class Controller(QtWidgets.QMainWindow):
    """
    The main window's controller.
    """

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

    def mouseDoubleClickEvent(self, event):
        """
        Overrides the double click event to check for any opening actions.
        """

        mouse_on_graphics_view = self.screenshot_view.underMouse()
        if mouse_on_graphics_view:
            action_manager.open_large_viewer(self)
