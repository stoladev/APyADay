import PyQt5
from PyQt5 import QtWidgets

from technician_client.modules.loaders import report_loader, widget_loader
from technician_client.modules.managers import verification_manager


class LoginView:
    def __init__(self, root, model):
        super().__init__()

        self.model = model
        self.root = root

        root.setWindowTitle("Technician Login")

        # Initializations
        root.technician_login_line = QtWidgets.QLineEdit(root)
        root.technician_password_line = QtWidgets.QLineEdit(root)
        root.technician_login_button = QtWidgets.QPushButton(root)
        root.technician_label = QtWidgets.QLabel(root)

        # Text Lines
        root.technician_login_line.setPlaceholderText("Username/Email Address")
        root.technician_password_line.setPlaceholderText("Password")
        root.technician_password_line.setEchoMode(QtWidgets.QLineEdit.Password)

        # Buttons
        root.technician_login_button.setText("Login")
        root.technician_login_button.clicked.connect(self.verify_technician)

        # Layout
        layout = QtWidgets.QVBoxLayout(root)
        layout.addWidget(root.technician_login_line)
        layout.addWidget(root.technician_password_line)
        layout.addWidget(root.technician_login_button)

        root.show()

    def verify_technician(self):
        verification_manager.verify_technician(self)

    def exec_main_window(self):
        print("Haha 101")


class MainView:
    def __init__(self, root, model):
        super().__init__()

        self.root = root
        root.model = model

        # General Settings
        root.setWindowTitle("Main Technician Window")
        root.screenshot_path = ""
        root.in_screenshot_mode = False
        root.setFixedSize(593, 558)
        root.central_widget = PyQt5.QtWidgets.QWidget(root)

        # Tab Initialization
        root.tab_widget = PyQt5.QtWidgets.QTabWidget(root.central_widget)
        root.accounts_tab = PyQt5.QtWidgets.QWidget()
        root.accounts_table = PyQt5.QtWidgets.QTableWidget(root.accounts_tab)
        root.reports_tab = PyQt5.QtWidgets.QWidget()

        # Create Account
        root.account_name_line = PyQt5.QtWidgets.QLineEdit(root.accounts_tab)
        root.password_line = PyQt5.QtWidgets.QLineEdit(root.accounts_tab)
        root.email_line = PyQt5.QtWidgets.QLineEdit(root.accounts_tab)
        root.worker_type_combo_box = PyQt5.QtWidgets.QComboBox(root.accounts_tab)
        root.create_account_button = PyQt5.QtWidgets.QPushButton(root.accounts_tab)

        # Reset Password
        root.new_pass_id_line = PyQt5.QtWidgets.QLineEdit(root.accounts_tab)
        root.new_password_line = PyQt5.QtWidgets.QLineEdit(root.accounts_tab)
        root.new_password_2_line = PyQt5.QtWidgets.QLineEdit(root.accounts_tab)
        root.reset_password_button = PyQt5.QtWidgets.QPushButton(root.accounts_tab)

        # Delete Selected Account
        root.delete_account_button = PyQt5.QtWidgets.QPushButton(root.accounts_tab)

        # Account Search
        root.find_account_line = PyQt5.QtWidgets.QLineEdit(root.accounts_tab)
        root.found_account_line = PyQt5.QtWidgets.QLineEdit(root.accounts_tab)
        root.change_account_button = PyQt5.QtWidgets.QPushButton(root.accounts_tab)
        root.found_email_line = PyQt5.QtWidgets.QLineEdit(root.accounts_tab)
        root.change_email_button = PyQt5.QtWidgets.QPushButton(root.accounts_tab)
        root.reports_filed_line = PyQt5.QtWidgets.QLineEdit(root.accounts_tab)
        root.last_login_line = PyQt5.QtWidgets.QLineEdit(root.accounts_tab)

        # Report Search
        root.reports_table = PyQt5.QtWidgets.QTableWidget(root.reports_tab)
        root.search_reports_line = PyQt5.QtWidgets.QLineEdit(root.reports_tab)
        root.open_reports_checkbox = PyQt5.QtWidgets.QCheckBox(root.reports_tab)
        root.open_reports_label = PyQt5.QtWidgets.QLabel(root.reports_tab)
        root.in_progress_reports_checkbox = PyQt5.QtWidgets.QCheckBox(root.reports_tab)
        root.in_progress_label = PyQt5.QtWidgets.QLabel(root.reports_tab)
        root.closed_fixed_reports_checkbox = PyQt5.QtWidgets.QCheckBox(root.reports_tab)
        root.closed_label = PyQt5.QtWidgets.QLabel(root.reports_tab)
        root.not_a_bug_reports_checkbox = PyQt5.QtWidgets.QCheckBox(root.reports_tab)
        root.not_a_bug_label = PyQt5.QtWidgets.QLabel(root.reports_tab)

        # Report View
        root.report_text_browser = PyQt5.QtWidgets.QTextBrowser(root.reports_tab)
        root.screenshot_view = PyQt5.QtWidgets.QGraphicsView(root.reports_tab)
        root.technician_report_notes = PyQt5.QtWidgets.QTextEdit(root.reports_tab)
        root.case_status_combo_box = PyQt5.QtWidgets.QComboBox(root.reports_tab)
        root.update_report_button = PyQt5.QtWidgets.QPushButton(root.reports_tab)

        # Labels
        root.reset_password_label = PyQt5.QtWidgets.QLabel(root.accounts_tab)
        root.reports_filed_label = PyQt5.QtWidgets.QLabel(root.accounts_tab)
        root.last_login_label = PyQt5.QtWidgets.QLabel(root.accounts_tab)
        root.create_account_label = PyQt5.QtWidgets.QLabel(root.accounts_tab)

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
