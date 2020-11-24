"""
Manages all interactions with an account, from creation to modification to deletion.
"""

# pylint: disable=import-error
# Reason: Importing is working fine, but pylint begs to differ. Most likely because of venv.

import PyQt5
import PyQt5.QtWidgets as qtW
import bcrypt

import technician_client.modules.loaders
from technician_client.modules.managers import verification_manager


def create_new_account(window, account_name, email, worker_type, password):
    """
    Creates a new account using the information in the respective textbox lines.

    :param window: The QMainWindow in use.
    :param account_name: The account name to create.
    :param email: The email of the new account.
    :param worker_type: The Type of account to create.
    :param password: The password of the new account.
    """

    if verification_manager.verify_inputs(window, account_name, password, email):

        accounts = window.database.accounts

        if accounts.find_one({"account_name": account_name}) is not None:
            msg = qtW.QMessageBox()
            msg.warning(
                window,
                "Account Exists",
                "Name Issue - an account with this name already exists.",
            )
            return

        if accounts.find_one({"email": email}) is not None:
            msg = qtW.QMessageBox()
            msg.warning(
                window,
                "Email In Use",
                "Email Issue - an account with this email already exists.",
            )
            return

        hash_pass = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        question = qtW.QMessageBox().question(
            window,
            "Confirmation",
            "You are about to create an account with the following details:\n\n"
            "Account Name: "
            + account_name
            + "\nEmail: "
            + email
            + "\nWorker Type: "
            + worker_type,
            qtW.QMessageBox.Yes | qtW.QMessageBox.No,
            qtW.QMessageBox.Yes,
        )

        if question == qtW.QMessageBox.No:
            return

        accounts.insert(
            {
                "account_name": account_name,
                "email": email,
                "employee_type": worker_type,
                "password": hash_pass,
                "reports_filed": 0,
                "last_login": 0,
            }
        )

        msg = qtW.QMessageBox()
        msg.about(window, "Success", "The account has been successfully created.")
        technician_client.modules.loaders.account_loader.load_accounts(window)


def reset_account_password(
    window, password, password_verified, hash_pass, account_name
):
    """
    Resets an account's password using the textbox line data.

    :param window: The QMainWindow in use.
    :param password: The first password field that contains the new password.
    :param password_verified: The second password field, identical to the first one.
    :param hash_pass: The hash_pass created by bcrypt.
    :param account_name: The account name of the account to change the password of.
    """

    if not verification_manager.verify_new_password(window, password):
        return

    if password != password_verified:
        PyQt5.QtWidgets.QMessageBox().warning(
            window, "Mismatch", "The new password doesn't match its verification."
        )
        return

    accounts = window.database.accounts
    account = accounts.find_one({"account_name": account_name})

    accounts.update(account, {"$set": {"password": hash_pass}})

    if account is None:
        PyQt5.QtWidgets.QMessageBox().warning(
            window,
            "Account Not Found",
            "No account has been found with the provided account name.",
        )
        return

    msg = qtW.QMessageBox()
    msg.about(
        window,
        "Success",
        account_name + "'s password has been successfully reset.",
    )

    technician_client.modules.loaders.account_loader.load_accounts(window)


def delete_selected_account(window, table: qtW.QTableWidget):
    """
    Deletes the selected account.

    :param window: The QMainWindow in use.
    :param table: The accounts table to delete the selected user from.
    """

    if table.currentItem() is None:
        msg = qtW.QMessageBox()
        msg.warning(
            window, "No Account Selected", "Please select an account to delete."
        )
        return

    row = table.currentItem().row()
    account_name = table.item(row, 0).text()
    email = table.item(row, 1).text()

    question = qtW.QMessageBox().question(
        window,
        "Confirmation",
        "You are about to delete:\n\n"
        "Account Name: " + account_name + "\n"
        "Email: " + email + "\n\n"
        "Are you sure you want to delete this account?",
        qtW.QMessageBox.Yes | qtW.QMessageBox.No,
        qtW.QMessageBox.Yes,
    )

    if question == qtW.QMessageBox.No:
        return

    accounts = window.database.accounts
    accounts.remove({"account_name": account_name})

    technician_client.modules.loaders.account_loader.load_accounts(window)

    next_index = table.model().index(row, 0)
    table.setCurrentIndex(next_index)
    if table.currentItem() is None:
        next_index = table.model().index(row - 1, 0)
        table.setCurrentIndex(next_index)


def change_account_name(window, account_name):
    """
    Changes the selected account name.

    :param window: The QMainWindow in use.
    :param account_name: The account name to change the selected account to.
    """

    if account_name is None:
        msg = qtW.QMessageBox()
        msg.warning(
            window,
            "No Account Selected",
            "Please make sure you have selected an account from the list.",
        )
        return

    accounts = window.database.accounts
    account = accounts.find_one({"account_name": account_name})

    if account is None:
        msg = qtW.QMessageBox()
        msg.warning(
            window,
            "Account Not Found",
            "No account has been found with the provided account name.",
        )
        return

    new_account_name, ok_button_pressed = qtW.QInputDialog.getText(
        window, "Prompt", "New Account Name:"
    )

    if not ok_button_pressed:
        return

    if not verification_manager.verify_new_account_name(window, new_account_name):
        return

    accounts.update(account, {"$set": {"account_name": new_account_name}})

    msg = qtW.QMessageBox()
    msg.about(
        window,
        "Success",
        account_name
        + "'s username has been successfully changed to "
        + new_account_name
        + ".",
    )

    technician_client.modules.loaders.account_loader.load_accounts(window)


def change_email(window, email):
    """
    Changes the selected account's email.

    :param window: The QMainWindow in use.
    :param email: The email to change the selected account to.
    """

    if email is None:
        msg = qtW.QMessageBox()
        msg.warning(
            window,
            "No Account Selected",
            "Please make sure you have selected an account from the list.",
        )
        return

    accounts = window.database.accounts
    account = accounts.find_one({"email": email})

    if account is None:
        msg = qtW.QMessageBox()
        msg.warning(
            window,
            "Account Not Found",
            "No account has been found with the provided account name.",
        )
        return

    new_email_name, okay_button_pressed = qtW.QInputDialog.getText(
        window, "Prompt", "New Email:"
    )

    if not okay_button_pressed:
        return

    if not verification_manager.verify_new_email(window, new_email_name):
        return

    accounts.update(account, {"$set": {"email": new_email_name}})

    msg = qtW.QMessageBox()
    msg.about(
        window,
        "Success",
        email + "'s email has been successfully reset to " + new_email_name + ".",
    )

    technician_client.modules.loaders.account_loader.load_accounts(window)
