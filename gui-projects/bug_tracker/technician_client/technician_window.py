"""
Initializes window widgets for the technician application. Points to and runs customizations and
specifications of execution/registered events.
"""

# pylint: disable=import-error
# Reason: Importing is working fine, but pylint begs to differ. Most likely because of venv.

# pylint: disable=too-many-instance-attributes
# Reason: This number of attributes is necessary because of the scope of the application.

# pylint: disable=invalid-name
# Reason: The 2 invalid names are overrides.

# pylint: disable=too-many-statements
# Reason: This number of statements is necessary because of the scope of the application.

import PyQt5.QtWidgets
import bcrypt
import pymongo

from technician_client.modules.loaders import menu_loader, report_loader, widget_loader
from technician_client.modules.managers import (
    account_manager,
    action_manager,
    keypress_manager,
    selection_manager,
)


class TechnicianMainWindow(PyQt5.QtWidgets.QMainWindow):
    """
    Handles the initiation of the main technician window, along with calling any setup
    configurations and/or event updates.
    """

    def __init__(self):
        super().__init__()

        # MongoDB Connection
        mongodb_url = open("../mongo_cluster.txt", "r")
        connection = mongodb_url.read()
        cluster = pymongo.MongoClient(connection)
        self.database = cluster["bug_tracker_db"]

        # General Settings
        self.setWindowTitle("Login Window")
        self.screenshot_path = ""
        self.in_screenshot_mode = False
        self.setFixedSize(593, 558)
        self.central_widget = PyQt5.QtWidgets.QWidget(self)

        # Tab Initialization
        self.tab_widget = PyQt5.QtWidgets.QTabWidget(self.central_widget)
        self.accounts_tab = PyQt5.QtWidgets.QWidget()
        self.accounts_table = PyQt5.QtWidgets.QTableWidget(self.accounts_tab)
        self.reports_tab = PyQt5.QtWidgets.QWidget()

        # Create Account
        self.account_name_line = PyQt5.QtWidgets.QLineEdit(self.accounts_tab)
        self.password_line = PyQt5.QtWidgets.QLineEdit(self.accounts_tab)
        self.email_line = PyQt5.QtWidgets.QLineEdit(self.accounts_tab)
        self.worker_type_combo_box = PyQt5.QtWidgets.QComboBox(self.accounts_tab)
        self.create_account_button = PyQt5.QtWidgets.QPushButton(self.accounts_tab)

        # Reset Password
        self.new_pass_id_line = PyQt5.QtWidgets.QLineEdit(self.accounts_tab)
        self.new_password_line = PyQt5.QtWidgets.QLineEdit(self.accounts_tab)
        self.new_password_2_line = PyQt5.QtWidgets.QLineEdit(self.accounts_tab)
        self.reset_password_button = PyQt5.QtWidgets.QPushButton(self.accounts_tab)

        # Delete Selected Account
        self.delete_account_button = PyQt5.QtWidgets.QPushButton(self.accounts_tab)

        # Account Search
        self.find_account_line = PyQt5.QtWidgets.QLineEdit(self.accounts_tab)
        self.found_account_line = PyQt5.QtWidgets.QLineEdit(self.accounts_tab)
        self.change_account_button = PyQt5.QtWidgets.QPushButton(self.accounts_tab)
        self.found_email_line = PyQt5.QtWidgets.QLineEdit(self.accounts_tab)
        self.change_email_button = PyQt5.QtWidgets.QPushButton(self.accounts_tab)
        self.reports_filed_line = PyQt5.QtWidgets.QLineEdit(self.accounts_tab)
        self.last_login_line = PyQt5.QtWidgets.QLineEdit(self.accounts_tab)

        # Report Search
        self.reports_table = PyQt5.QtWidgets.QTableWidget(self.reports_tab)
        self.search_reports_line = PyQt5.QtWidgets.QLineEdit(self.reports_tab)
        self.open_reports_checkbox = PyQt5.QtWidgets.QCheckBox(self.reports_tab)
        self.open_reports_label = PyQt5.QtWidgets.QLabel(self.reports_tab)
        self.in_progress_reports_checkbox = PyQt5.QtWidgets.QCheckBox(self.reports_tab)
        self.in_progress_label = PyQt5.QtWidgets.QLabel(self.reports_tab)
        self.closed_fixed_reports_checkbox = PyQt5.QtWidgets.QCheckBox(self.reports_tab)
        self.closed_label = PyQt5.QtWidgets.QLabel(self.reports_tab)
        self.not_a_bug_reports_checkbox = PyQt5.QtWidgets.QCheckBox(self.reports_tab)
        self.not_a_bug_label = PyQt5.QtWidgets.QLabel(self.reports_tab)

        # Report View
        self.report_text_browser = PyQt5.QtWidgets.QTextBrowser(self.reports_tab)
        self.screenshot_view = PyQt5.QtWidgets.QGraphicsView(self.reports_tab)
        self.technician_report_notes = PyQt5.QtWidgets.QTextEdit(self.reports_tab)
        self.case_status_combo_box = PyQt5.QtWidgets.QComboBox(self.reports_tab)
        self.update_report_button = PyQt5.QtWidgets.QPushButton(self.reports_tab)

        # Labels
        self.reset_password_label = PyQt5.QtWidgets.QLabel(self.accounts_tab)
        self.reports_filed_label = PyQt5.QtWidgets.QLabel(self.accounts_tab)
        self.last_login_label = PyQt5.QtWidgets.QLabel(self.accounts_tab)
        self.create_account_label = PyQt5.QtWidgets.QLabel(self.accounts_tab)

        self.load_all_widgets()
        report_loader.load_reports(self)

        self.show()

        # Button actions on Accounts Tab
        self.change_account_button.pressed.connect(self.change_account_name)
        self.change_email_button.pressed.connect(self.change_email)

        # Checks for item selection changes
        self.accounts_table.itemSelectionChanged.connect(self.check_new_selection)

        # Checks for input in find_account_line
        self.find_account_line.textChanged.connect(self.search_accounts_table)

    def contextMenuEvent(self, event):
        """
        Overrides context menu events to load the account table's menu.
        """

        menu_loader.load_accounts_menu(self, event)

    def keyPressEvent(self, event):
        """
        Overrides key press events to check for special key presses.
        """

        keypress_manager.check_keypress(self, event)

    def mouseDoubleClickEvent(self, event) -> None:
        """
        Overrides the double click event to check for any opening actions.
        """

        mouse_on_graphics_view = self.screenshot_view.underMouse()
        if mouse_on_graphics_view:
            action_manager.open_large_viewer(self)

    def search_accounts_table(self):
        """
        Forwards this self function to a manager.
        """

        selection_manager.find_account_match(self)

    def check_new_selection(self):
        """
        Forwards this self function to a manager.
        """

        selection_manager.check_account_selection(self)

    def check_report_selection(self):
        """
        Forwards this self function to a manager.
        """

        row = self.reports_table.currentRow()
        report_browser = self.report_text_browser

        report_id = self.reports_table.item(row, 3).text()
        submitter_text = "Submitter: " + self.reports_table.item(row, 0).text()
        report_text = self.reports_table.item(row, 4).text()

        selection_manager.check_report_selection(
            self, report_id, report_browser, submitter_text, report_text
        )

    def create_new_account(self):
        """
        Forwards this self function to a manager.
        """

        account_name = self.account_name_line.text()
        email = self.email_line.text()
        worker_type = self.worker_type_combo_box.currentText()
        password = self.password_line.text()

        account_manager.create_new_account(
            self, account_name, email, worker_type, password
        )

    def delete_selected_account(self):
        """
        Forwards this self function to a manager.
        """

        table = self.accounts_table

        account_manager.delete_selected_account(self, table)

    def reset_account_password(self):
        """
        Forwards this self function to a manager.
        """

        password = self.new_password_line.text()
        password_verified = self.new_password_2_line.text()

        account_name = self.new_pass_id_line.text()
        hash_pass = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        account_manager.reset_account_password(
            self,
            password,
            password_verified,
            hash_pass,
            account_name,
        )

    def change_account_name(self):
        """
        Forwards this self function to a manager.
        """

        account_name = self.found_account_line.text()

        account_manager.change_account_name(self, account_name)

    def change_email(self):
        """
        Forwards this self function to a manager.
        """

        email = self.found_email_line.text()

        account_manager.change_email(self, email)

    def open_large_viewer(self):
        """
        Forwards this self function to a manager.
        """

        action_manager.open_large_viewer(self)

    def load_all_widgets(self):
        """
        Mass-loads all the widgets.
        """

        widget_loader.load_tabs(self.tab_widget, self.accounts_tab, self.reports_tab)

        widget_loader.load_account_creation(
            self.email_line, self.account_name_line, self.password_line
        )

        widget_loader.load_account_finder(
            self.find_account_line,
            self.found_account_line,
            self.found_email_line,
            self.reports_filed_line,
            self.last_login_line,
        )

        widget_loader.load_password_changer(
            self.new_pass_id_line, self.new_password_line, self.new_password_2_line
        )

        widget_loader.load_report_finder(self.search_reports_line)

        widget_loader.load_buttons(self)
        widget_loader.load_labels(self)
        widget_loader.load_tables(self)
        widget_loader.load_text_browsers(self)
        widget_loader.load_text_boxes(self)
        widget_loader.load_checkboxes(self)
        widget_loader.load_combo_boxes(self)
        widget_loader.load_graphics_view(self.screenshot_view)

        self.setCentralWidget(self.central_widget)
