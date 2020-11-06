from PyQt5.QtWidgets import (
    QComboBox,
    QGraphicsView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QTableWidget,
    QTextBrowser,
    QTextEdit,
    QWidget,
)

from technician_client.modules.loaders import menu_loader, widget_loader
from technician_client.modules.managers import (
    account_manager,
    keypress_manager,
    selection_manager,
)


class TechnicianMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # General Settings
        self.setWindowTitle("Login Window")
        self.setFixedSize(593, 558)
        self.central_widget = QWidget(self)

        # Tab Initialization
        self.tab_widget = QTabWidget(self.central_widget)
        self.accounts_tab = QWidget()
        self.accounts_table = QTableWidget(self.accounts_tab)
        self.reports_tab = QWidget()

        # Create Account
        self.account_name_line = QLineEdit(self.accounts_tab)
        self.password_line = QLineEdit(self.accounts_tab)
        self.email_line = QLineEdit(self.accounts_tab)
        self.worker_type_combo_box = QComboBox(self.accounts_tab)
        self.create_account_button = QPushButton(self.accounts_tab)

        # Reset Password
        self.new_pass_id_line = QLineEdit(self.accounts_tab)
        self.new_password_line = QLineEdit(self.accounts_tab)
        self.new_password_2_line = QLineEdit(self.accounts_tab)
        self.reset_password_button = QPushButton(self.accounts_tab)

        # Delete Selected Account
        self.delete_account_button = QPushButton(self.accounts_tab)

        # Account Search
        self.find_account_line = QLineEdit(self.accounts_tab)
        self.found_account_line = QLineEdit(self.accounts_tab)
        self.change_account_button = QPushButton(self.accounts_tab)
        self.found_email_line = QLineEdit(self.accounts_tab)
        self.change_email_button = QPushButton(self.accounts_tab)
        self.reports_filed_line = QLineEdit(self.accounts_tab)
        self.last_login_line = QLineEdit(self.accounts_tab)

        # Report Search
        self.reports_table = QTableWidget(self.reports_tab)
        self.search_reports_line = QLineEdit(self.reports_tab)

        # Report View
        self.report_text_browser = QTextBrowser(self.reports_tab)
        self.screenshot_view = QGraphicsView(self.reports_tab)
        self.technician_report_notes = QTextEdit(self.reports_tab)
        self.case_status_combo_box = QComboBox(self.reports_tab)
        self.update_report_button = QPushButton(self.reports_tab)

        # Labels
        self.reset_password_label = QLabel(self.accounts_tab)
        self.reports_filed_label = QLabel(self.accounts_tab)
        self.last_login_label = QLabel(self.accounts_tab)
        self.create_account_label = QLabel(self.accounts_tab)

        widget_loader.load_all_widgets(self)

        self.show()

        # Button actions on Accounts Tab
        self.change_account_button.pressed.connect(self.change_account_name)
        self.change_email_button.pressed.connect(self.change_email)

        # Checks for item selection changes
        self.accounts_table.itemSelectionChanged.connect(self.check_new_selection)

        # Checks for input in find_account_line
        self.find_account_line.textChanged.connect(self.search_accounts_table)

    def contextMenuEvent(self, event):
        menu_loader.load_accounts_menu(self, event)

    def keyPressEvent(self, event):
        keypress_manager.check_keypress(self, event)

    def search_accounts_table(self):
        selection_manager.find_account_match(self)

    def check_new_selection(self):
        selection_manager.check_account_selection(self)

    def create_new_account(self):
        account_manager.create_new_account(self)

    def delete_selected_account(self):
        account_manager.delete_selected_account(self)

    def reset_account_password(self):
        account_manager.reset_account_password(self)

    def change_account_name(self):
        account_manager.change_account_name(self)

    def change_email(self):
        account_manager.change_email(self)
