from PyQt5 import QtCore

from modules.managers import account_manager


def check_keypress(window, event):
    return_key_pressed = event.key() == QtCore.Qt.Key_Return
    del_key_pressed = event.key() == QtCore.Qt.Key_Delete

    if del_key_pressed:
        account_manager.delete_selected_account(window)

    if return_key_pressed:
        # Create Account
        if window.account_name_line.hasFocus():
            window.password_line.setFocus()
            return
        if window.password_line.hasFocus():
            window.email_line.setFocus()
            return
        if (window.email_line.hasFocus()) | (window.create_account_button.hasFocus()):
            window.create_new_account()

        # Reset Password
        if window.new_pass_id_line.hasFocus():
            window.new_password_line.setFocus()
            return
        if window.new_password_line.hasFocus():
            window.new_password_2_line.setFocus()
            return
        if (window.new_password_2_line.hasFocus()) | (
            window.reset_password_button.hasFocus()
        ):
            window.reset_account_password()
