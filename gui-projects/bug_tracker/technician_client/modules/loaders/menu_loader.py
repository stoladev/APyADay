"""
Loads menus for tables or general context-menu event calls.
"""

from PyQt5.QtWidgets import QMenu, QTableWidget
from pandas.core import indexes

from technician_client.modules.managers import account_manager


# TODO
# Context menu still opens if not right clicking on a cell. Confined to the table widget,
# but should be confined further to the selected index only.


def load_accounts_menu(window, event):
    """
    Loads the QMenu for the accounts table. Works only when activated while mouse is hovering
    over the accounts table.
    :param window: The QMainWindow being used.
    :param event: The context menu event.
    :return: The selected action, or cancels if none selected/clicked off.
    """

    table: QTableWidget = window.accounts_table
    index: indexes = table.selectionModel().selection().indexes()
    mouse_on_table = window.accounts_table.underMouse()

    if index:
        if mouse_on_table:
            menu = QMenu()
            change_account_name_action = menu.addAction("Change Account Name")
            change_email_action = menu.addAction("Change Email")
            delete_action = menu.addAction("Delete")
            action = menu.exec_(window.mapToGlobal(event.pos()))

            if action == change_account_name_action:
                account_manager.change_account_name(window)
            if action == change_email_action:
                account_manager.change_email(window)
            if action == delete_action:
                account_manager.delete_selected_account(window)
