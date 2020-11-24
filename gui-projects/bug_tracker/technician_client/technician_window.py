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
import pymongo


class TechnicianMainWindow(PyQt5.QtWidgets.QMainWindow):
    """
    Handles the initiation of the main technician window, along with calling any setup
    configurations and/or event updates.
    """

    def __init__(self):
        super().__init__()

        from technician_client.modules.loaders import widget_loader, report_loader

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

        widget_loader.load_all_widgets(self)
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

        from technician_client.modules.loaders import menu_loader

        menu_loader.load_accounts_menu(self, event)

    def keyPressEvent(self, event):
        """
        Overrides key press events to check for special key presses.
        """

        from technician_client.modules.managers import keypress_manager

        keypress_manager.check_keypress(self, event)

    def mouseDoubleClickEvent(self, event) -> None:
        """
        Overrides the double click event to check for any opening actions.
        """

        mouse_on_graphics_view = self.screenshot_view.underMouse()
        if mouse_on_graphics_view:
            from technician_client.modules.managers import action_manager

            action_manager.open_large_viewer(self)

    def search_accounts_table(self):
        """
        Forwards this self function to a manager.
        """

        from technician_client.modules.managers import selection_manager

        selection_manager.find_account_match(self)

    def check_new_selection(self):
        """
        Forwards this self function to a manager.
        """

        from technician_client.modules.managers import selection_manager

        selection_manager.check_account_selection(self)

    def check_report_selection(self):
        """
        Forwards this self function to a manager.
        """

        from technician_client.modules.managers import selection_manager

        selection_manager.check_report_selection(self)

    def create_new_account(self):
        """
        Forwards this self function to a manager.
        """

        from technician_client.modules.managers import account_manager

        account_manager.create_new_account(self)

    def delete_selected_account(self):
        """
        Forwards this self function to a manager.
        """

        from technician_client.modules.managers import account_manager

        account_manager.delete_selected_account(self)

    def reset_account_password(self):
        """
        Forwards this self function to a manager.
        """

        from technician_client.modules.managers import account_manager

        account_manager.reset_account_password(self)

    def change_account_name(self):
        """
        Forwards this self function to a manager.
        """

        from technician_client.modules.managers import account_manager

        account_manager.change_account_name(self)

    def change_email(self):
        """
        Forwards this self function to a manager.
        """

        from technician_client.modules.managers import account_manager

        account_manager.change_email(self)

    def open_large_viewer(self):
        """
        Forwards this self function to a manager.
        """

        from technician_client.modules.managers import action_manager

        action_manager.open_large_viewer(self)
