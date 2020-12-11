"""
The data model used for the technician's main report window.
"""

# pylint: disable=import-error
# Reason: Importing is working fine, but pylint begs to differ. Most likely because of venv.

import bcrypt

from technician_client.modules.managers import (
    account_manager,
    action_manager,
    selection_manager,
)


class Model:
    """
    Handles all data manipulations for the technician's main report window.
    """

    def __init__(self, root, database):
        self.root = root
        self.database = database

    def search_accounts_table(self):
        """
        Forwards this self function to a manager.
        """

        selection_manager.find_account_match(self.root)

    def check_new_selection(self):
        """
        Forwards this self function to a manager.
        """

        selection_manager.check_account_selection(self.root)

    def check_report_selection(self):
        """
        Forwards this self function to a manager.
        """

        row = self.root.reports_table.currentRow()
        report_browser = self.root.report_text_browser

        report_id = self.root.reports_table.item(row, 3).text()
        submitter_text = "Submitter: " + self.root.reports_table.item(row, 0).text()
        report_text = self.root.reports_table.item(row, 4).text()

        selection_manager.check_report_selection(
            self.root, report_id, report_browser, submitter_text, report_text
        )

    def create_new_account(self):
        """
        Forwards this self function to a manager.
        """

        account_name = self.root.account_name_line.text()
        email = self.root.email_line.text()
        worker_type = self.root.worker_type_combo_box.currentText()
        password = self.root.password_line.text()

        account_manager.create_new_account(
            self.root, account_name, email, worker_type, password
        )

    def delete_selected_account(self):
        """
        Forwards this self function to a manager.
        """

        table = self.root.accounts_table

        account_manager.delete_selected_account(self.root, table)

    def reset_account_password(self):
        """
        Forwards this self function to a manager.
        """

        password = self.root.new_password_line.text()
        password_verified = self.root.new_password_2_line.text()

        account_name = self.root.new_pass_id_line.text()
        hash_pass = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        account_manager.reset_account_password(
            self.root,
            password,
            password_verified,
            hash_pass,
            account_name,
        )

    def change_account_name(self):
        """
        Forwards this self function to a manager.
        """

        account_name = self.root.found_account_line.text()

        account_manager.change_account_name(self.root, account_name)

    def change_email(self):
        """
        Forwards this self function to a manager.
        """

        email = self.root.found_email_line.text()

        account_manager.change_email(self.root, email)

    def open_large_viewer(self):
        """
        Forwards this self function to a manager.
        """

        action_manager.open_large_viewer(self.root)

    def update_report(self):
        """
        Updates the report with any new data made by the technician.
        """
       