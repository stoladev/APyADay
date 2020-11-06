from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from modules.loaders.mongodb_loader import cluster


# TODO
# Make rows read-only
# Center all fields
#
def load_accounts(window):
    table: QTableWidget = window.accounts_table

    selection = table.selectionModel().currentIndex()
    table.clearSelection()

    table.setRowCount(0)

    db = cluster["bug_tracker_db"]
    collection = db.accounts

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
