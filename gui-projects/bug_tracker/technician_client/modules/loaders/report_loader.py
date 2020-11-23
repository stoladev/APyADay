"""
Loads all data regarding reports.
"""

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


def load_reports(window):
    """
    Loads/reloads the accounts for the accounts table, grabbing the necessary data from MongoDB.

    :param window: The QMainWindow in use.
    :return: Returns all existing accounts with their current data.
    """
    table: QTableWidget = window.reports_table

    selection = table.selectionModel().currentIndex()
    table.clearSelection()

    table.setRowCount(0)

    collection = window.database.reports

    reports = collection.find({})

    i = 0
    for document in reports:
        submitter = document["account_name"] + " (" + document["employee_type"] + ")"
        table.insertRow(i)
        table.setItem(i, 0, QTableWidgetItem(submitter))
        table.setItem(i, 1, QTableWidgetItem(document["issue_type"]))
        table.setItem(i, 2, QTableWidgetItem(str(document["submitted_on"])))
        table.setItem(i, 3, QTableWidgetItem(str(document["_id"])))
        table.setItem(i, 4, QTableWidgetItem(document["report"]))
        i += 1

    if selection is not None:
        table.setCurrentIndex(selection)
