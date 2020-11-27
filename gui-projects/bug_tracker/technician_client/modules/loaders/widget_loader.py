"""
Loads all specifications for the widgets used within the technician application.
"""

# pylint: disable=import-error
# Reason: Importing is working fine, but pylint begs to differ. Most likely because of venv.

# pylint: disable=too-many-statements
# Reason: This number of statements is necessary because of the scope of the application.
import PyQt5
import PyQt5.QtWidgets as qtW
from PyQt5 import QtCore

from technician_client.modules.loaders import account_loader


def load_tabs(
    tab_widget: qtW.QTabWidget,
    accounts_tab: qtW.QWidget,
    reports_tab: qtW.QWidget,
):
    """
    Loads the tabs for the technician application.
    """

    tab_widget.setGeometry(QtCore.QRect(0, 0, 921, 641))
    tab_widget.setCurrentIndex(1)
    tab_widget.addTab(accounts_tab, "Accounts")
    tab_widget.addTab(reports_tab, "Reports")


def load_account_creation(
    email_line: qtW.QLineEdit,
    account_name_line: qtW.QLineEdit,
    password_line: qtW.QLineEdit,
):
    email_line.setPlaceholderText("Email Address")
    email_line.setGeometry(QtCore.QRect(400, 140, 181, 24))

    account_name_line.setPlaceholderText("Account Name")
    account_name_line.setGeometry(QtCore.QRect(400, 80, 181, 24))

    password_line.setPlaceholderText("Password")
    password_line.setEchoMode(PyQt5.QtWidgets.QLineEdit.Password)
    password_line.setGeometry(QtCore.QRect(400, 110, 181, 24))


def load_account_finder(
    find_account_line: qtW.QLineEdit,
    found_account_line: qtW.QLineEdit,
    found_email_line: qtW.QLineEdit,
    reports_filed_line: qtW.QLineEdit,
    last_login_line: qtW.QLineEdit,
):
    """
    Loads the widgets that are used for account searching.

    :param find_account_line:
    :param found_account_line:
    :param found_email_line:
    :param reports_filed_line:
    :param last_login_line:
    """

    find_account_line.setPlaceholderText("Find Account...")
    find_account_line.setGeometry(QtCore.QRect(10, 410, 381, 24))
    find_account_line.setAlignment(QtCore.Qt.AlignCenter)

    found_account_line.setText("Account Name")
    found_account_line.setGeometry(QtCore.QRect(10, 440, 291, 24))
    found_account_line.setAlignment(QtCore.Qt.AlignCenter)
    found_account_line.setReadOnly(True)

    found_email_line.setText("Email Address")
    found_email_line.setGeometry(QtCore.QRect(10, 470, 291, 24))
    found_email_line.setAlignment(QtCore.Qt.AlignCenter)
    found_email_line.setReadOnly(True)

    reports_filed_line.setText("")
    reports_filed_line.setGeometry(QtCore.QRect(100, 500, 51, 24))
    reports_filed_line.setReadOnly(True)

    last_login_line.setText("")
    last_login_line.setGeometry(QtCore.QRect(230, 500, 161, 24))
    last_login_line.setAlignment(QtCore.Qt.AlignCenter)
    last_login_line.setReadOnly(True)


def load_password_changer(
    new_pass_id_line: qtW.QLineEdit,
    new_password_line: qtW.QLineEdit,
    new_password_2_line: qtW.QLineEdit,
):
    """
    Loads the widgets that are used for changing an account's password.

    :param new_pass_id_line:
    :param new_password_line:
    :param new_password_2_line:
    """

    new_pass_id_line.setPlaceholderText("Account Name")
    new_pass_id_line.setGeometry(QtCore.QRect(401, 310, 181, 24))

    new_password_line.setPlaceholderText("New Password")
    new_password_line.setEchoMode(PyQt5.QtWidgets.QLineEdit.Password)
    new_password_line.setGeometry(QtCore.QRect(401, 340, 181, 24))

    new_password_2_line.setPlaceholderText("Verify New Password")
    new_password_2_line.setEchoMode(PyQt5.QtWidgets.QLineEdit.Password)
    new_password_2_line.setGeometry(QtCore.QRect(401, 370, 181, 24))


def load_report_finder(search_reports_line: qtW.QLineEdit):
    """
    Loads the text lines for the technician application.
    """

    search_reports_line.setPlaceholderText("Search reports for...")
    search_reports_line.setGeometry(QtCore.QRect(340, 190, 241, 24))
    search_reports_line.setAlignment(QtCore.Qt.AlignCenter)


def load_buttons(self):
    """
    Loads the buttons for the technician application.
    """

    self.change_account_button.setText("Change")
    self.change_account_button.setGeometry(QtCore.QRect(310, 440, 80, 24))

    self.change_email_button.setText("Change")
    self.change_email_button.setGeometry(QtCore.QRect(310, 470, 80, 24))

    self.create_account_button.setText("Create")
    self.create_account_button.setGeometry(QtCore.QRect(529, 200, 51, 24))
    self.create_account_button.pressed.connect(self.model.create_new_account)

    self.reset_password_button.setText("Reset")
    self.reset_password_button.setGeometry(QtCore.QRect(530, 400, 51, 24))
    self.reset_password_button.pressed.connect(self.model.reset_account_password)

    self.delete_account_button.setText("Delete Selected Account")
    self.delete_account_button.setGeometry(QtCore.QRect(430, 500, 150, 24))
    self.delete_account_button.pressed.connect(self.model.delete_selected_account)

    self.update_report_button.setText("Update")
    self.update_report_button.setGeometry(QtCore.QRect(500, 500, 80, 24))


def load_labels(self):
    """
    Loads the labels for the technician application.
    """

    self.create_account_label.setText("Create Account")
    self.create_account_label.setGeometry(QtCore.QRect(400, 60, 100, 16))

    self.last_login_label.setText("Last Login:")
    self.last_login_label.setGeometry(QtCore.QRect(160, 500, 71, 16))

    self.reports_filed_label.setText("Reports Filed:")
    self.reports_filed_label.setGeometry(QtCore.QRect(10, 500, 91, 16))

    self.reset_password_label.setText("Reset Password")
    self.reset_password_label.setGeometry(QtCore.QRect(401, 290, 91, 16))

    self.open_reports_label.setGeometry(QtCore.QRect(25, 191, 100, 20))
    self.open_reports_label.setText("Open")

    self.in_progress_label.setGeometry(QtCore.QRect(75, 191, 100, 20))
    self.in_progress_label.setText("In Progress")

    self.closed_label.setGeometry(QtCore.QRect(167, 191, 100, 20))
    self.closed_label.setText("Closed")

    self.not_a_bug_label.setGeometry(QtCore.QRect(228, 191, 100, 20))
    self.not_a_bug_label.setText("Not A Bug")


def load_tables(self):
    """
    Loads the tables for the technician application.
    """

    self.accounts_table.setSelectionBehavior(PyQt5.QtWidgets.QTableView.SelectRows)
    self.accounts_table.setEditTriggers(
        PyQt5.QtWidgets.QAbstractItemView.NoEditTriggers
    )
    self.accounts_table.setSelectionMode(
        PyQt5.QtWidgets.QAbstractItemView.SingleSelection
    )
    self.accounts_table.setGeometry(QtCore.QRect(10, 10, 381, 391))
    self.accounts_table.setRowCount(0)
    self.accounts_table.setColumnCount(3)

    # Columns
    item = PyQt5.QtWidgets.QTableWidgetItem()
    self.accounts_table.setHorizontalHeaderItem(0, item)
    item = PyQt5.QtWidgets.QTableWidgetItem()
    self.accounts_table.setHorizontalHeaderItem(1, item)
    item = PyQt5.QtWidgets.QTableWidgetItem()
    self.accounts_table.setHorizontalHeaderItem(2, item)

    # Column Settings

    # accounts_table.sortItems(2, Qt.DescendingOrder)
    item = self.accounts_table.horizontalHeaderItem(0)
    header = self.accounts_table.horizontalHeader()
    header.setSectionResizeMode(PyQt5.QtWidgets.QHeaderView.ResizeToContents)
    item.setText("Account Name")
    item = self.accounts_table.horizontalHeaderItem(1)
    header.setSectionResizeMode(1, PyQt5.QtWidgets.QHeaderView.Stretch)
    item.setText("Email")
    item = self.accounts_table.horizontalHeaderItem(2)
    item.setText("Reports")

    # Row Settings

    account_loader.load_accounts(self)
    self.accounts_table.setSortingEnabled(True)

    # Reports Table
    self.reports_table.setSelectionBehavior(PyQt5.QtWidgets.QTableView.SelectRows)
    self.reports_table.setEditTriggers(PyQt5.QtWidgets.QAbstractItemView.NoEditTriggers)
    self.reports_table.setSelectionMode(
        PyQt5.QtWidgets.QAbstractItemView.SingleSelection
    )
    self.reports_table.setGeometry(QtCore.QRect(10, 10, 571, 171))
    self.reports_table.setColumnCount(5)
    self.reports_table.setRowCount(0)

    item = PyQt5.QtWidgets.QTableWidgetItem()
    header = self.reports_table.horizontalHeader()
    header.setSectionResizeMode(PyQt5.QtWidgets.QHeaderView.ResizeToContents)
    self.reports_table.setHorizontalHeaderItem(0, item)
    item = PyQt5.QtWidgets.QTableWidgetItem()
    header.setSectionResizeMode(0, PyQt5.QtWidgets.QHeaderView.Stretch)
    self.reports_table.setHorizontalHeaderItem(1, item)
    item = PyQt5.QtWidgets.QTableWidgetItem()
    self.reports_table.setHorizontalHeaderItem(2, item)
    item = PyQt5.QtWidgets.QTableWidgetItem()
    self.reports_table.setHorizontalHeaderItem(3, item)
    self.reports_table.hideColumn(3)
    item = PyQt5.QtWidgets.QTableWidgetItem()
    self.reports_table.setHorizontalHeaderItem(4, item)
    self.reports_table.hideColumn(4)

    item = self.reports_table.horizontalHeaderItem(0)
    item.setText("Submitter")
    item = self.reports_table.horizontalHeaderItem(1)
    item.setText("Issue Type")
    item = self.reports_table.horizontalHeaderItem(2)
    item.setText("Submitted On")
    item = self.reports_table.horizontalHeaderItem(3)
    item.setText("ID")
    item = self.reports_table.horizontalHeaderItem(4)
    item.setText("Report")

    # ACTIONS
    self.reports_table.doubleClicked.connect(self.model.check_report_selection)


def load_text_browsers(self):
    """
    Loads the text browsers for the technician application.
    """

    self.report_text_browser.setGeometry(QtCore.QRect(10, 220, 321, 305))


def load_text_boxes(self):
    """
    Loads the text boxes for the technician application.
    """

    self.technician_report_notes.setGeometry(QtCore.QRect(340, 350, 241, 141))


def load_checkboxes(self):
    """
    Loads the check boxes for the technician application.
    """

    self.open_reports_checkbox.setGeometry(QtCore.QRect(10, 190, 20, 20))
    self.open_reports_checkbox.setChecked(True)

    self.in_progress_reports_checkbox.setGeometry(QtCore.QRect(60, 190, 20, 20))
    self.in_progress_reports_checkbox.setChecked(True)

    self.closed_fixed_reports_checkbox.setGeometry(QtCore.QRect(152, 190, 20, 20))

    self.not_a_bug_reports_checkbox.setGeometry(QtCore.QRect(213, 190, 20, 20))


def load_combo_boxes(self):
    """
    Loads the combo boxes for the technician application.
    """

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


def load_graphics_view(screenshot_view: qtW.QGraphicsView):
    """
    Loads the graphics viewers for the technician application.
    """

    screenshot_view.setGeometry(QtCore.QRect(340, 220, 241, 121))
