"""
Handles selections for both the accounts and reports tables.

TODO Clear find line if an item is clicked manually
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit


def check_account_selection(window):
    row = window.accounts_table.currentRow()
    selected_account_name = window.accounts_table.item(row, 0).text()
    found_account_line: QLineEdit = window.found_account_line
    found_email_line: QLineEdit = window.found_email_line
    reports_filed_line: QLineEdit = window.reports_filed_line
    last_login_line: QLineEdit = window.last_login_line
    new_pass_id_line: QLineEdit = window.new_pass_id_line

    accounts = window.database.accounts
    selected_account = accounts.find_one({"account_name": selected_account_name})

    if selected_account:
        found_account_line.setText(selected_account["account_name"])
        new_pass_id_line.setText(selected_account["account_name"])
        found_email_line.setText(selected_account["email"])
        reports_filed_line.setText(str(selected_account["reports_filed"]))
        last_login_line.setText(str(selected_account["last_login"]))


def find_account_match(window):
    table = window.accounts_table

    for row in range(table.rowCount()):
        for column in range(table.columnCount()):
            item = table.item(row, column)
            if window.find_account_line.text() == "":
                return clear_account_fields(window)
            if window.find_account_line.text() in item.data(Qt.DisplayRole):
                return table.setCurrentItem(item)


def clear_account_fields(window):
    window.found_account_line.setText("")
    window.found_email_line.setText("")
    window.accounts_table.clearSelection()
