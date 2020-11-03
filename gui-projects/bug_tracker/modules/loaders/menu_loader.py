from PyQt5.QtWidgets import QMenu, QTableWidget
from pandas.core import indexes

# TODO
# Context menu still opens if not right clicking on a cell. Confined to the table widget,
# but should be confined further to the selected index only.
# If multiple accounts selected, only show the delete option.
from modules.managers import account_manager


def load_accounts_menu(window, event):
    table: QTableWidget = window.accounts_table
    index: indexes = table.selectionModel().selection().indexes()
    mouse_on_table = window.accounts_table.underMouse()

    # FIGURE THIS OUT, KING.
    if index:
        if mouse_on_table:
            row = table.rowAt(event.y())
            menu = QMenu()
            delete_action = menu.addAction("Delete")
            action = menu.exec_(window.mapToGlobal(event.pos()))

            if action == delete_action:
                account_manager.delete_selected_account(window)
