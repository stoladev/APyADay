"""
Loads all data regarding accounts.
"""

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from technician_client.modules.loaders.mongodb_loader import cluster


# TODO
# Make rows read-only
# Center all fields
#
def load_accounts(window):
    """
    Loads/reloads the accounts for the accounts table, grabbing the necessary data from MongoDB.
    :param window: The QMainWindow in use.
    :return: Returns all existing accounts with their current data.
    """
    table: QTableWidget = window.accounts_table

    selection = table.selectionModel().currentIndex()
    table.clearSelection()

    table.setRowCount(0)

    database = cluster["bug_tracker_db"]
    collection = database.accounts

    accounts = collection.find({})

    i = 0
    for document in accounts:
        table.insertRow(i)
        table.setItem(i, 0, QTableWidgetItem(document["account_name"]))
        table.setItem(i, 1, QTableWidgetItem(document["email"]))
        table.setItem(i, 2, QTableWidgetItem(str(document["reports_filed"])))
        i += 1

    if selection is not None:
        table.setCurrentIndex(selection)
