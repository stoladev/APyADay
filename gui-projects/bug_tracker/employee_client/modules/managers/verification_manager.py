"""
Handles verifications ranging from acceptable new inputs to connecting with MongoDB to verify
authenticity of existing details.

TODO Connect to MongoDB in a more secure manner
"""

import bcrypt
from PyQt5.QtWidgets import QMessageBox


def verify_employee(window, account, password):
    """
    Verifies if an employee exists, and checks the password against the found account.

    :param window: The QMainWindow in use.
    :param account: The name to check against the password.
    :param password: The password to verify if an account is found.
    :return: A successful or failed login to the main application.
    """

    if account:
        key = password.encode("utf-8")
        salt = account["password"]
        lock = account["password"]
        if bcrypt.hashpw(key, salt) == lock:
            update_timestamp(window, account)
            window.accept()
        else:
            QMessageBox.warning(
                window,
                "Incorrect Password",
                "The password you've provided is incorrect.",
            )
    else:
        QMessageBox.warning(window, "No Match", "No matching account found.")


def update_timestamp(window, account):
    """
    Updates the login timestamp for the account that is logging in through MongoDB.

    :param window: The QMainWindow in use.
    :param account: The account to update.
    :return: A success or failure on update.
    """

    account_list = window.database.accounts
    account_list.update(
        account,
        {"$currentDate": {"last_login": True}},
    )
