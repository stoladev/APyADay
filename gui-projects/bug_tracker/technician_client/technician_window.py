from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QComboBox,
    QGraphicsView,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QTextBrowser,
    QTextEdit,
    QWidget,
)


class TechnicianMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # GENERAL SETTINGS
        self.setWindowTitle("Login Window")
        self.setFixedSize(593, 558)
        self.central_widget = QWidget(self)

        # WIDGET INITIALIZATION
        # Tab Initialization
        self.tab_widget = QTabWidget(self.central_widget)
        self.accounts_tab = QWidget()
        self.reports_tab = QWidget()
        self.load_tabs()

        # Text Line Initialization
        self.new_password_line = QLineEdit(self.accounts_tab)
        self.search_reports_line = QLineEdit(self.reports_tab)
        self.new_pass_id_line = QLineEdit(self.accounts_tab)
        self.last_login_line = QLineEdit(self.accounts_tab)
        self.reports_filed_line = QLineEdit(self.accounts_tab)
        self.found_email_line = QLineEdit(self.accounts_tab)
        self.found_username_line = QLineEdit(self.accounts_tab)
        self.find_user_line = QLineEdit(self.accounts_tab)
        self.password_line = QLineEdit(self.accounts_tab)
        self.username_line = QLineEdit(self.accounts_tab)
        self.email_line = QLineEdit(self.accounts_tab)
        self.load_text_lines()

        # Button Initialization
        self.update_report_button = QPushButton(self.reports_tab)
        self.delete_user_button = QPushButton(self.accounts_tab)
        self.reset_password_button = QPushButton(self.accounts_tab)
        self.create_user_button = QPushButton(self.accounts_tab)
        self.change_email_button = QPushButton(self.accounts_tab)
        self.change_username_button = QPushButton(self.accounts_tab)
        self.load_buttons()

        # Label initialization
        self.reset_password_label = QLabel(self.accounts_tab)
        self.reports_filed_label = QLabel(self.accounts_tab)
        self.last_login_label = QLabel(self.accounts_tab)
        self.create_user_label = QLabel(self.accounts_tab)
        self.load_labels()

        # Table Initialization
        self.accounts_table = QTableWidget(self.accounts_tab)
        self.reports_table = QTableWidget(self.reports_tab)
        self.load_tables()

        # Text Browser Initialization
        self.report_text_browser = QTextBrowser(self.reports_tab)
        self.load_text_browsers()

        # Text Box Initialization
        self.technician_report_notes = QTextEdit(self.reports_tab)
        self.load_text_boxes()

        # Combo Box Initialization
        self.case_status_combo_box = QComboBox(self.reports_tab)
        self.worker_type_combo_box = QComboBox(self.accounts_tab)
        self.load_combo_boxes()

        # Graphics View Initialization
        self.screenshot_view = QGraphicsView(self.reports_tab)
        self.load_graphics_view()

        self.disable_client()
        self.setCentralWidget(self.central_widget)

        self.show()

    def load_tabs(self):
        self.tab_widget.setGeometry(QtCore.QRect(0, 0, 921, 641))
        self.tab_widget.setCurrentIndex(1)
        self.tab_widget.addTab(self.accounts_tab, "Accounts")
        self.tab_widget.addTab(self.reports_tab, "Reports")

    def load_text_lines(self):
        self.email_line.setPlaceholderText("Email Address")
        self.email_line.setGeometry(QtCore.QRect(400, 140, 181, 24))

        self.username_line.setPlaceholderText("Username")
        self.username_line.setGeometry(QtCore.QRect(400, 80, 181, 24))

        self.password_line.setPlaceholderText("Password")
        self.password_line.setEchoMode(QLineEdit.Password)
        self.password_line.setGeometry(QtCore.QRect(400, 110, 181, 24))

        self.find_user_line.setPlaceholderText("Find User...")
        self.find_user_line.setGeometry(QtCore.QRect(10, 410, 381, 24))
        self.find_user_line.setAlignment(QtCore.Qt.AlignCenter)

        self.found_username_line.setText("Username")
        self.found_username_line.setGeometry(QtCore.QRect(10, 440, 291, 24))
        self.found_username_line.setAlignment(QtCore.Qt.AlignCenter)
        self.found_username_line.setReadOnly(True)

        self.found_email_line.setText("Email Address")
        self.found_email_line.setGeometry(QtCore.QRect(10, 470, 291, 24))
        self.found_email_line.setAlignment(QtCore.Qt.AlignCenter)
        self.found_email_line.setReadOnly(True)

        self.reports_filed_line.setText("")
        self.reports_filed_line.setGeometry(QtCore.QRect(100, 500, 51, 24))
        self.reports_filed_line.setReadOnly(True)

        self.last_login_line.setText("")
        self.last_login_line.setGeometry(QtCore.QRect(230, 500, 161, 24))
        self.last_login_line.setAlignment(QtCore.Qt.AlignCenter)
        self.last_login_line.setReadOnly(True)

        self.new_pass_id_line.setPlaceholderText("Username/Email Address")
        self.new_pass_id_line.setGeometry(QtCore.QRect(401, 310, 181, 24))

        self.new_password_line.setPlaceholderText("New Password")
        self.new_password_line.setEchoMode(QLineEdit.Password)
        self.new_password_line.setGeometry(QtCore.QRect(401, 340, 181, 24))

        self.search_reports_line.setPlaceholderText("Search reports for...")
        self.search_reports_line.setGeometry(QtCore.QRect(340, 190, 241, 24))
        self.search_reports_line.setAlignment(QtCore.Qt.AlignCenter)

    def load_buttons(self):
        self.change_username_button.setText("Change")
        self.change_username_button.setGeometry(QtCore.QRect(310, 440, 80, 24))

        self.change_email_button.setText("Change")
        self.change_email_button.setGeometry(QtCore.QRect(310, 470, 80, 24))

        self.create_user_button.setText("Create")
        self.create_user_button.setGeometry(QtCore.QRect(529, 200, 51, 24))

        self.reset_password_button.setText("Reset")
        self.reset_password_button.setGeometry(QtCore.QRect(530, 370, 51, 24))

        self.delete_user_button.setText("Delete Selected User")
        self.delete_user_button.setGeometry(QtCore.QRect(450, 500, 131, 24))

        self.update_report_button.setText("Update")
        self.update_report_button.setGeometry(QtCore.QRect(500, 500, 80, 24))

    def load_labels(self):
        self.create_user_label.setText("Create User")
        self.create_user_label.setGeometry(QtCore.QRect(400, 60, 71, 16))

        self.last_login_label.setText("Last Login:")
        self.last_login_label.setGeometry(QtCore.QRect(160, 500, 71, 16))

        self.reports_filed_label.setText("Reports Filed:")
        self.reports_filed_label.setGeometry(QtCore.QRect(10, 500, 91, 16))

        self.reset_password_label.setText("Reset Password")
        self.reset_password_label.setGeometry(QtCore.QRect(401, 290, 91, 16))

    def load_tables(self):
        self.accounts_table.setGeometry(QtCore.QRect(10, 10, 381, 391))
        self.accounts_table.setRowCount(0)
        self.accounts_table.setColumnCount(3)

        # Columns
        item = QTableWidgetItem()
        self.accounts_table.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.accounts_table.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.accounts_table.setHorizontalHeaderItem(2, item)

        # Column Settings
        item = self.accounts_table.horizontalHeaderItem(0)
        header = self.accounts_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        item.setText("Username")
        item = self.accounts_table.horizontalHeaderItem(1)
        header = self.accounts_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        item.setText("Email")
        item = self.accounts_table.horizontalHeaderItem(2)
        item.setText("Last Login")

        self.accounts_table.setSortingEnabled(True)

        # Reports Table
        self.reports_table.setGeometry(QtCore.QRect(10, 10, 571, 171))
        self.reports_table.setColumnCount(4)
        self.reports_table.setRowCount(0)
        item = QTableWidgetItem()
        self.reports_table.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.reports_table.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.reports_table.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.reports_table.setHorizontalHeaderItem(3, item)
        item = self.reports_table.horizontalHeaderItem(0)
        item.setText("Submitter")
        item = self.reports_table.horizontalHeaderItem(1)
        item.setText("Issue Type")
        item = self.reports_table.horizontalHeaderItem(2)
        item.setText("Severity")
        item = self.reports_table.horizontalHeaderItem(3)
        item.setText("Reported On")

    def load_text_browsers(self):
        self.report_text_browser.setGeometry(QtCore.QRect(10, 190, 321, 331))

    def load_text_boxes(self):
        self.technician_report_notes.setGeometry(QtCore.QRect(340, 350, 241, 141))

    def load_combo_boxes(self):
        self.case_status_combo_box.setGeometry(QtCore.QRect(340, 500, 151, 24))
        self.case_status_combo_box.addItem("Case Open")
        self.case_status_combo_box.addItem("Case In Progress")
        self.case_status_combo_box.addItem("Case Closed - Fixed")
        self.case_status_combo_box.addItem("Not A Bug")

        self.worker_type_combo_box.setGeometry(QtCore.QRect(400, 170, 181, 24))
        self.worker_type_combo_box.addItem("Employee")
        self.worker_type_combo_box.addItem("Manager")
        self.worker_type_combo_box.addItem("Supervisor")
        self.worker_type_combo_box.addItem("Department Head")

    def load_graphics_view(self):
        self.screenshot_view.setGeometry(QtCore.QRect(340, 220, 241, 121))

    def disable_client(self):
        self.reports_tab.setEnabled(False)

        self.accounts_table.setEnabled(False)

        self.create_user_label.setEnabled(False)
        self.username_line.setEnabled(False)
        self.password_line.setEnabled(False)
        self.create_user_button.setEnabled(False)
        self.email_line.setEnabled(False)
        self.worker_type_combo_box.setEnabled(False)

        self.reset_password_label.setEnabled(False)
        self.reset_password_button.setEnabled(False)
        self.new_pass_id_line.setEnabled(False)
        self.new_password_line.setEnabled(False)

        self.find_user_line.setEnabled(False)
        self.found_email_line.setEnabled(False)
        self.found_username_line.setEnabled(False)
        self.last_login_label.setEnabled(False)
        self.last_login_line.setEnabled(False)
        self.reports_filed_label.setEnabled(False)
        self.reports_filed_line.setEnabled(False)
        self.change_email_button.setEnabled(False)
        self.change_username_button.setEnabled(False)

        self.delete_user_button.setEnabled(False)

        # Disable Technician Login Info; changes Login to Logout if switching tech

    def enable_client(self):
        self.reports_tab.setEnabled(True)

        self.accounts_table.setEnabled(True)

        self.create_user_label.setEnabled(True)
        self.username_line.setEnabled(True)
        self.password_line.setEnabled(True)
        self.create_user_button.setEnabled(True)
        self.email_line.setEnabled(True)
        self.worker_type_combo_box.setEnabled(True)

        self.reset_password_label.setEnabled(True)
        self.reset_password_button.setEnabled(True)
        self.new_pass_id_line.setEnabled(True)
        self.new_password_line.setEnabled(True)

        self.find_user_line.setEnabled(True)
        self.found_email_line.setEnabled(True)
        self.found_username_line.setEnabled(True)
        self.last_login_label.setEnabled(True)
        self.last_login_line.setEnabled(True)
        self.reports_filed_label.setEnabled(True)
        self.reports_filed_line.setEnabled(True)
        self.change_email_button.setEnabled(True)
        self.change_username_button.setEnabled(True)

        self.delete_user_button.setEnabled(True)

        # Disable Technician Login Info; changes Login to Logout if switching tech
        self.technician_label.setEnabled(False)
        self.technician_login_line.setEnabled(False)
        self.technician_password_line.setEnabled(False)
        self.technician_login_button.setText("Logout")

        # elif account is None:
        #     hash_pass = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        #     accounts.insert({"username": username, "password": hash_pass})
        #     print("Account created.")

    # def create_user(self):
