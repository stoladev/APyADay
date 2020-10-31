from PyQt5.QtGui import QContextMenuEvent, QMouseEvent
from PyQt5.QtWidgets import QMenu, QTableWidget
from pandas.core import indexes

# TODO
# Context menu still opens if not right clicking on a cell. Confined to the table widget,
# but should be confined further to the selected index only.
# If multiple accounts selected, only show the delete option.
from modules.managers import account_manager


def accounts_menu(window, event):
    table: QTableWidget = window.accounts_table
    index: indexes = table.selectionModel().selection().indexes()
    mouse_press: QMouseEvent = event.MouseButtonPress
    event: QContextMenuEvent = event

    # row = self.tableWidget.rowAt(event.y())

    # FIGURE THIS OUT, KING.
    if index:
        if mouse_press.NonClientAreaMouseButtonPress:
            print("yo")
        # for i in index:
        #     row, column = i.row(), i.column()
        row = table.rowAt(event.y())
        menu = QMenu()
        open_action = menu.addAction("Open")
        delete_action = menu.addAction("Delete")
        rename_action = menu.addAction("Rename")
        action = menu.exec_(window.mapToGlobal(event.pos()))

        if action == open_action:
            window.openAction(table.rowAt(event.y()))

        if action == delete_action:
            account_manager.delete_selected_account(window)


def openAction(self, row, column):
    if self._slideShowWin:
        self._slideShowWin.showImageByPath(self._twoDLst[row][column])
        self._animateUpOpen()


# TODO
# Delete multiple accounts when selected.
def deleteSelected(self):
    # TODO
    pass
