import re

import bcrypt
from PyQt5.QtWidgets import QMessageBox

from modules.mongo_connection import cluster


def create_account(window):
    account_name = window.account_name_line.text()
    email = window.email_line.text()
    employee_type = window.worker_type_combo_box.currentText()
    password = window.password_line.text()

    if verify_inputs(window, account_name, password, email):
        insert_new_account(window, account_name, email, password, employee_type)


def insert_new_account(window, account_name, email, password, worker_type):
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
        QMessageBox.No,
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
        msg.about(
            window, "Account Created", "The account has been successfully created."
        )
    else:
        msg = QMessageBox()
        msg.critical(window, "Error!", "An account with this name already exists.")
        return

    print("Account created.")


def verify_inputs(window, account_name, password, email):
    if verify_new_account_name(window, account_name):
        if verify_new_password(window, password):
            if verify_new_email(window, email):
                return True
    return False


def verify_new_account_name(window, account_name):
    symbols = len(set(re.findall(r"[~!@#$%^&*()+=`]", account_name)))

    error_found = False
    error_message = "The account name is invalid.\n\nErrors:\n"

    if len(account_name) < 6:
        error_message += "short account name length (6-char minimum)\n"
        error_found = True

    if symbols > 0:
        error_message += "incompatible symbol found"
        error_found = True

    if error_found:
        msg = QMessageBox()
        msg.critical(window, "Error!", error_message)
        return False

    return True


def verify_new_password(window, password):
    upper = len(set(re.findall(r"[A-Z]", password)))
    lower = len(set(re.findall(r"[a-z]", password)))
    nums = len(set(re.findall(r"[0-9]", password)))
    symbols = len(set(re.findall(r"[~!@#$%^&*()_+=\-`]", password)))

    error_found = False
    error_message = "The password is insecure.\n\nErrors:\n"

    if len(password) < 12:
        error_message += "short password length (12-char minimum)\n"
        error_found = True

    if upper < 1:
        error_message += "no uppercase letters (A-Z)\n"
        error_found = True

    if lower < 1:
        error_message += "no lowercase letters (a-z)\n"
        error_found = True

    if nums < 1:
        error_message += "no numbers (0-9)\n"
        error_found = True

    if symbols < 1:
        error_message += "no symbols (!@#$%^&*)"
        error_found = True

    if error_found:
        msg = QMessageBox()
        msg.critical(window, "Error!", error_message)
        return False

    return True


def verify_new_email(window, email):
    symbols = len(set(re.findall(r"[~!#$%^&*()+=`]", email)))

    error_found = False
    error_message = "The email is incomplete.\n\nErrors:\n"

    if (email.find("@") == -1) | (email.endswith("@")) | (email.startswith("@")):
        error_message += "missing/misplaced @\n"
        error_found = True

    if (email.find(".") == -1) | (email.endswith(".")) | (email.startswith(".")):
        error_message += "missing/misplaced period\n"
        error_found = True

    if (email.find("@.") != -1) | (email.find(".@") != -1):
        error_message += "@. or .@ found, which is incompatible\n"
        error_found = True

    if symbols > 0:
        error_message += "incompatible symbol found"
        error_found = True

    if error_found:
        msg = QMessageBox()
        msg.critical(window, "Error!", error_message)
        return False

    return True
