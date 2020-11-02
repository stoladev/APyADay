from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit

from modules.loaders import mongodb_loader


def check_account_selection(window):
    row = window.accounts_table.currentRow()
    selected_account_name = window.accounts_table.item(row, 0).text()
    found_account_line: QLineEdit = window.found_account_line
    found_email_line: QLineEdit = window.found_email_line
    reports_filed_line: QLineEdit = window.reports_filed_line
    last_login_line: QLineEdit = window.last_login_line

    db = mongodb_loader.cluster["bug_tracker_db"]
    accounts = db.accounts
    selected_account = accounts.find_one({"account_name": selected_account_name})

    if selected_account:
        found_account_line.setText(selected_account["account_name"])
        found_email_line.setText(selected_account["email"])
        reports_filed_line.setText(str(selected_account["reports_filed"]))
        last_login_line.setText(str(selected_account["last_login"]))


def search_accounts_table(window):
    # TODO
    # Grab the current items in the table
    # Check for the nearest match in the item list according to find_account_line
    # Hide the rest of the results, auto select the best fit
    # THIS IS JUST A PROTOTYPE. CLEAN UP THIS CODE LATER

    table = window.accounts_table

    for row in range(table.rowCount()):
        for column in range(table.columnCount()):
            item = table.item(row, column)
            if window.find_account_line.text() == "":
                return clear_found_fields(window)
            if window.find_account_line.text() in item.data(Qt.DisplayRole):
                return table.setCurrentItem(item)
    return print("Nothing found.")


def clear_found_fields(window):
    window.found_account_line.setText("")
    window.found_email_line.setText("")
    window.accounts_table.clearSelection()
