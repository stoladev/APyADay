from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem

from modules.loaders.mongodb_loader import cluster


# TODO
# Make rows read-only
# Center all fields
#
def load_accounts(window):
    table = window.accounts_table
    table.setRowCount(0)
    table.sortItems(2, Qt.DescendingOrder)

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
