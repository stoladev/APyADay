import bcrypt
from PyQt5.QtWidgets import QMessageBox

from modules.loaders import account_loader
from modules.loaders.mongodb_loader import cluster
from modules.managers.verification_manager import verify_inputs


def create_new_account(window):
    account_name = window.account_name_line.text()
    email = window.email_line.text()
    worker_type = window.worker_type_combo_box.currentText()
    password = window.password_line.text()

    if verify_inputs(window, account_name, password, email):
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

        db = cluster["bug_tracker_db"]
        accounts = db.accounts

        if accounts.find_one({"account_name": account_name}) is None:
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
        else:
            msg = QMessageBox()
            msg.warning(
                window, "Account Exists", "An account with this name already exists."
            )
            return


def reset_account_password(window):
    account_name = window.new_pass_id_line.text()
    password = window.password_line.text()
    hash_pass = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    db = cluster["bug_tracker_db"]
    accounts = db.accounts

    account = accounts.find_one({"account_name": account_name})
    if account is not None:
        accounts.update(account, {"password": hash_pass, "reports_filed": 10})
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

        db = cluster["bug_tracker_db"]
        accounts = db.accounts

        accounts.remove({"account_name": account_name})

        account_loader.load_accounts(window)

        next_index = table.model().index(row, 0)
        table.setCurrentIndex(next_index)
        if table.currentItem() is None:
            next_index = table.model().index(row - 1, 0)
            table.setCurrentIndex(next_index)
