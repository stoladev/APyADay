import re

import bcrypt
from PyQt5.QtWidgets import QMessageBox

from modules.loaders import mongodb_loader


def verify_inputs(window, account_name, password, email):
    if verify_new_account_name(window, account_name):
        if verify_new_password(window, password):
            if verify_new_email(window, email):
                return True
    return False


def verify_technician(window):
    username = window.technician_login_line.text()
    password = window.technician_password_line.text()

    db = mongodb_loader.cluster["bug_tracker_db"]
    accounts = db.technicians

    account = accounts.find_one({"username": username})

    if account:
        key = password.encode("utf-8")
        salt = account["password"]
        lock = account["password"]
        if bcrypt.hashpw(key, salt) == lock:
            window.accept()
        else:
            QMessageBox.warning(
                window,
                "Incorrect Password",
                "The password you've provided is incorrect.",
            )
    else:
        QMessageBox.warning(window, "No Match", "No matching account found.")


def verify_new_account_name(window, account_name):
    symbols = len(set(re.findall(r"[~!@#$%^&*()+=`]", account_name)))

    error_found = False
    error_message = "The account name is invalid.\n\nErrors:\n"

    if (len(account_name) < 6) | (len(account_name) > 15):
        error_message += "account name length (6-15 chars)\n"
        error_found = True

    if symbols > 0:
        error_message += "incompatible symbol found"
        error_found = True

    if error_found:
        msg = QMessageBox()
        msg.warning(window, "Invalid Field", error_message)
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
        msg.warning(window, "Invalid Field", error_message)
        return False

    return True


# TODO
# Improve on new email verification method
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
        msg.warning(window, "Invalid Field", error_message)
        return False

    return True
