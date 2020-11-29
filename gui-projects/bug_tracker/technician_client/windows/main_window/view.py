"""
The View handler for the technician's main report window.
"""

# pylint: disable=import-error
# Reason: Importing is working fine, but pylint begs to differ. Most likely because of venv.

# pylint: disable=too-many-statements
# Reason: The statements are required for all of the widget initializations.

# pylint: disable=too-few-public-methods
# Reason: The View will include more methods later on during the structuring process.

from PyQt5 import QtWidgets

from technician_client.modules.loaders import report_loader, widget_loader


class View:
    """
    Handles the view updates depending on model calculations for the main report window.
    """

    def __init__(self, root, model):
        super().__init__()

        self.root = root
        root.model = model

        # General Settings
        root.setWindowTitle("Main Technician Window")
        root.screenshot_path = ""
        root.in_screenshot_mode = False
        root.setFixedSize(593, 558)
        root.central_widget = QtWidgets.QWidget(root)

        # Tab Initialization
        root.tab_widget = QtWidgets.QTabWidget(root.central_widget)
        root.accounts_tab = QtWidgets.QWidget()
        root.accounts_table = QtWidgets.QTableWidget(root.accounts_tab)
        root.reports_tab = QtWidgets.QWidget()

        # Create Account
        root.account_name_line = QtWidgets.QLineEdit(root.accounts_tab)
        root.password_line = QtWidgets.QLineEdit(root.accounts_tab)
        root.email_line = QtWidgets.QLineEdit(root.accounts_tab)
        root.worker_type_combo_box = QtWidgets.QComboBox(root.accounts_tab)
        root.create_account_button = QtWidgets.QPushButton(root.accounts_tab)

        # Reset Password
        root.new_pass_id_line = QtWidgets.QLineEdit(root.accounts_tab)
        root.new_password_line = QtWidgets.QLineEdit(root.accounts_tab)
        root.new_password_2_line = QtWidgets.QLineEdit(root.accounts_tab)
        root.reset_password_button = QtWidgets.QPushButton(root.accounts_tab)

        # Delete Selected Account
        root.delete_account_button = QtWidgets.QPushButton(root.accounts_tab)

        # Account Search
        root.find_account_line = QtWidgets.QLineEdit(root.accounts_tab)
        root.found_account_line = QtWidgets.QLineEdit(root.accounts_tab)
        root.change_account_button = QtWidgets.QPushButton(root.accounts_tab)
        root.found_email_line = QtWidgets.QLineEdit(root.accounts_tab)
        root.change_email_button = QtWidgets.QPushButton(root.accounts_tab)
        root.reports_filed_line = QtWidgets.QLineEdit(root.accounts_tab)
        root.last_login_line = QtWidgets.QLineEdit(root.accounts_tab)

        # Report Search
        root.reports_table = QtWidgets.QTableWidget(root.reports_tab)
        root.search_reports_line = QtWidgets.QLineEdit(root.reports_tab)
        root.open_reports_checkbox = QtWidgets.QCheckBox(root.reports_tab)
        root.open_reports_label = QtWidgets.QLabel(root.reports_tab)
        root.in_progress_reports_checkbox = QtWidgets.QCheckBox(root.reports_tab)
        root.in_progress_label = QtWidgets.QLabel(root.reports_tab)
        root.closed_fixed_reports_checkbox = QtWidgets.QCheckBox(root.reports_tab)
        root.closed_label = QtWidgets.QLabel(root.reports_tab)
        root.not_a_bug_reports_checkbox = QtWidgets.QCheckBox(root.reports_tab)
        root.not_a_bug_label = QtWidgets.QLabel(root.reports_tab)

        # Report View
        root.report_text_browser = QtWidgets.QTextBrowser(root.reports_tab)
        root.screenshot_view = QtWidgets.QGraphicsView(root.reports_tab)
        root.technician_report_notes = QtWidgets.QTextEdit(root.reports_tab)
        root.case_status_combo_box = QtWidgets.QComboBox(root.reports_tab)
        root.update_report_button = QtWidgets.QPushButton(root.reports_tab)

        # Labels
        root.reset_password_label = QtWidgets.QLabel(root.accounts_tab)
        root.reports_filed_label = QtWidgets.QLabel(root.accounts_tab)
        root.last_login_label = QtWidgets.QLabel(root.accounts_tab)
        root.create_account_label = QtWidgets.QLabel(root.accounts_tab)

        self.load_all_widgets()
        report_loader.load_reports(root)

        root.show()

        # Button actions on Accounts Tab
        root.change_account_button.pressed.connect(model.change_account_name)
        root.change_email_button.pressed.connect(model.change_email)

        # Checks for item selection changes
        root.accounts_table.itemSelectionChanged.connect(model.check_new_selection)

        # Checks for input in find_account_line
        root.find_account_line.textChanged.connect(model.search_accounts_table)

    def load_all_widgets(self):
        """
        Mass-loads all the widgets.
        """

        widget_loader.load_tabs(
            self.root.tab_widget, self.root.accounts_tab, self.root.reports_tab
        )

        widget_loader.load_account_creation(
            self.root.email_line, self.root.account_name_line, self.root.password_line
        )

        widget_loader.load_account_finder(
            self.root.find_account_line,
            self.root.found_account_line,
            self.root.found_email_line,
            self.root.reports_filed_line,
            self.root.last_login_line,
        )

        widget_loader.load_password_changer(
            self.root.new_pass_id_line,
            self.root.new_password_line,
            self.root.new_password_2_line,
        )

        widget_loader.load_report_finder(self.root.search_reports_line)

        widget_loader.load_buttons(self.root)
        widget_loader.load_labels(self.root)
        widget_loader.load_tables(self.root)
        widget_loader.load_text_browsers(self.root)
        widget_loader.load_text_boxes(self.root)
        widget_loader.load_checkboxes(self.root)
        widget_loader.load_combo_boxes(self.root)
        widget_loader.load_graphics_view(self.root.screenshot_view)

        self.root.setCentralWidget(self.root.central_widget)
