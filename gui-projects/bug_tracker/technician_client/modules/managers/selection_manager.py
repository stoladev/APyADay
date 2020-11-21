"""
Handles selections for both the accounts and reports tables.

TODO Clear find line if an item is clicked manually
"""

# pylint: disable=import-error
# Reason: Importing is working fine, but pylint begs to differ. Most likely because of venv.

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QTextBrowser
from bson import ObjectId

from technician_client.modules.managers import action_manager


def check_account_selection(window):
    """
    Checks the selected account and fills in all fields that find benefit from this information.

    :param window: The QMainWindow in use.
    :return: Any useful data regarding the currently selected account.
    """

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
    """
    Finds an account match using data provided by the finder.

    :param window: The QMainWindow in use.
    :return: Either an account that matches the description, or nothing.
    """

    table = window.accounts_table

    for row in range(table.rowCount()):
        for column in range(table.columnCount()):
            item = table.item(row, column)
            if window.find_account_line.text() == "":
                return clear_account_fields(window)
            if window.find_account_line.text() in item.data(Qt.DisplayRole):
                return table.setCurrentItem(item)
    return None


def clear_account_fields(window):
    """
    Clears the account search fields.

    :param window: The QMainWindow in use.
    :return: Clears the fields and selection on the account table.
    """

    window.found_account_line.setText("")
    window.found_email_line.setText("")
    window.accounts_table.clearSelection()


def check_report_selection(window):
    """
    Loads the double-clicked report's details, such as the report itself along with any images.

    :param window: The QMainWindow in use.
    :return: Detailed report data.
    """

    row = window.reports_table.currentRow()

    report_id = window.reports_table.item(row, 3).text()

    reports = window.database.reports
    print(report_id)
    report = reports.find_one({"_id": ObjectId(report_id)})

    if report:
        report_browser: QTextBrowser = window.report_text_browser
        report_browser.setText(report["report"])

        encoded_image = report["screenshot"]
        action_manager.load_screenshot(window, encoded_image)
