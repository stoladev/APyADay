import bcrypt
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox

from modules.loaders import account_loader, mongodb_loader
from modules.managers import verification_manager


def create_new_account(window):
    account_name = window.account_name_line.text()
    email = window.email_line.text()
    worker_type = window.worker_type_combo_box.currentText()
    password = window.password_line.text()

    if verification_manager.verify_inputs(window, account_name, password, email):

        db = mongodb_loader.cluster["bug_tracker_db"]
        accounts = db.accounts

        if accounts.find_one({"account_name": account_name}) is not None:
            msg = QMessageBox()
            msg.warning(
                window,
                "Account Exists",
                "Name Issue - an account with this name already exists.",
            )
            return

        if accounts.find_one({"email": email}) is not None:
            msg = QMessageBox()
            msg.warning(
                window,
                "Email In Use",
                "Email Issue - an account with this email already exists.",
            )
            return

        hash_pass = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        question = QMessageBox().question(
            window,
            "Confirmation",
            "You are about to create an account with the following details:\n\n"
            "Account Name: "
            + account_name
            + "\nEmail: "
            + email
            + "\nWorker Type: "
            + worker_type,
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes,
        )

        if question == QMessageBox.No:
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

        msg = QMessageBox()
        msg.about(window, "Success", "The account has been successfully created.")
        account_loader.load_accounts(window)


def reset_account_password(window, **kwargs):
    username = kwargs.get("account", None)
    password = window.new_password_line.text()
    password_verified = window.new_password_2_line.text()

    if not verification_manager.verify_new_password(window, password):
        return

    if password != password_verified:
        msg = QMessageBox()
        msg.warning(
            window, "Mismatch", "The new password doesn't match its verification."
        )
        return

    account_name = window.new_pass_id_line.text()
    hash_pass = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    db = mongodb_loader.cluster["bug_tracker_db"]
    accounts = db.accounts
    account = accounts.find_one({"account_name": account_name})

    if account is None:
        msg = QMessageBox()
        msg.warning(
            window,
            "Account Not Found",
            "No account has been found with the provided account name.",
        )
        return

    accounts.update(account, {"$set": {"password": hash_pass}})

    msg = QMessageBox()
    msg.about(
        window,
        "Success",
        account_name + "'s password has been successfully reset.",
    )

    account_loader.load_accounts(window)


def delete_selected_account(window):
    table = window.accounts_table

    if table.currentItem() is None:
        msg = QMessageBox()
        msg.warning(
            window, "No Account Selected", "Please select an account to delete."
        )
        return
    else:
        row = table.currentItem().row()
        account_name = table.item(row, 0).text()
        email = table.item(row, 1).text()

        question = QMessageBox().question(
            window,
            "Confirmation",
            "You are about to delete:\n\n"
            "Account Name: " + account_name + "\n"
            "Email: " + email + "\n\n"
            "Are you sure you want to delete this account?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes,
        )

        if question == QMessageBox.No:
            return

        db = mongodb_loader.cluster["bug_tracker_db"]
        accounts = db.accounts

        accounts.remove({"account_name": account_name})

        account_loader.load_accounts(window)

        next_index = table.model().index(row, 0)
        table.setCurrentIndex(next_index)
        if table.currentItem() is None:
            next_index = table.model().index(row - 1, 0)
            table.setCurrentIndex(next_index)


def change_account_name(window):
    account_name: QLineEdit = window.found_account_line.text()

    if account_name is None:
        msg = QMessageBox()
        msg.warning(
            window,
            "No Account Selected",
            "Please make sure you have selected an account from the list.",
        )
        return

    db = mongodb_loader.cluster["bug_tracker_db"]
    accounts = db.accounts
    account = accounts.find_one({"account_name": account_name})

    if account is None:
        msg = QMessageBox()
        msg.warning(
            window,
            "Account Not Found",
            "No account has been found with the provided account name.",
        )
        return

    new_account_name, ok = QInputDialog.getText(
        window, "New Account Name", "New Account Name:"
    )

    if not ok:
        return

    if verification_manager.verify_new_account_name(window, new_account_name):
        accounts.update(account, {"$set": {"account_name": new_account_name}})

    msg = QMessageBox()
    msg.about(
        window,
        "Success",
        account_name + "'s password has been successfully reset.",
    )

    account_loader.load_accounts(window)


# def change_email(window):
