from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QComboBox,
    QGraphicsView,
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
        self.setEnabled(True)
        self.setFixedSize(593, 558)

        # WIDGET INITIALIZATION
        self.central_widget = QWidget(self)

        # TABS
        self.tab_widget = QTabWidget(self.central_widget)
        self.tab_widget.setGeometry(QtCore.QRect(0, 0, 921, 641))
        self.tab_widget.setCurrentIndex(1)
        self.accounts_tab = QWidget()
        self.reports_tab = QWidget()
        self.reports_tab.setEnabled(False)
        self.tab_widget.addTab(self.accounts_tab, "Accounts")
        self.tab_widget.addTab(self.reports_tab, "Reports")

        # TEXT LINES
        self.email_line = QLineEdit(self.accounts_tab)
        self.email_line.setPlaceholderText("Email Address")
        self.email_line.setEnabled(False)
        self.email_line.setGeometry(QtCore.QRect(400, 200, 181, 24))

        self.username_line = QLineEdit(self.accounts_tab)
        self.username_line.setPlaceholderText("Username")
        self.username_line.setEnabled(False)
        self.username_line.setGeometry(QtCore.QRect(400, 140, 181, 24))

        self.password_line = QLineEdit(self.accounts_tab)
        self.password_line.setPlaceholderText("Password")
        self.password_line.setEnabled(False)
        self.password_line.setGeometry(QtCore.QRect(400, 170, 181, 24))

        self.find_user_line = QLineEdit(self.accounts_tab)
        self.find_user_line.setPlaceholderText("Find User...")
        self.find_user_line.setEnabled(False)
        self.find_user_line.setGeometry(QtCore.QRect(10, 410, 381, 24))
        self.find_user_line.setAlignment(QtCore.Qt.AlignCenter)

        self.found_username_line = QLineEdit(self.accounts_tab)
        self.found_username_line.setText("Username")
        self.found_username_line.setEnabled(False)
        self.found_username_line.setGeometry(QtCore.QRect(10, 440, 291, 24))
        self.found_username_line.setAlignment(QtCore.Qt.AlignCenter)
        self.found_username_line.setReadOnly(True)

        self.found_email_line = QLineEdit(self.accounts_tab)
        self.found_email_line.setText("Email Address")
        self.found_email_line.setEnabled(False)
        self.found_email_line.setGeometry(QtCore.QRect(10, 470, 291, 24))
        self.found_email_line.setAlignment(QtCore.Qt.AlignCenter)
        self.found_email_line.setReadOnly(True)

        self.reports_filed_line = QLineEdit(self.accounts_tab)
        self.reports_filed_line.setText("")
        self.reports_filed_line.setEnabled(False)
        self.reports_filed_line.setGeometry(QtCore.QRect(100, 500, 51, 24))
        self.reports_filed_line.setReadOnly(True)

        self.last_login_line = QLineEdit(self.accounts_tab)
        self.last_login_line.setText("")
        self.last_login_line.setEnabled(False)
        self.last_login_line.setGeometry(QtCore.QRect(230, 500, 161, 24))
        self.last_login_line.setAlignment(QtCore.Qt.AlignCenter)
        self.last_login_line.setReadOnly(True)

        self.technician_login_line = QLineEdit(self.accounts_tab)
        self.technician_login_line.setPlaceholderText("Username/Email Address")
        self.technician_login_line.setGeometry(QtCore.QRect(400, 30, 181, 24))
        self.technician_login_line.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )

        self.technician_password_line = QLineEdit(self.accounts_tab)
        self.technician_password_line.setPlaceholderText("Password")
        self.technician_password_line.setGeometry(QtCore.QRect(400, 60, 181, 24))

        self.new_pass_id_line = QLineEdit(self.accounts_tab)
        self.new_pass_id_line.setPlaceholderText("Username/Email Address")
        self.new_pass_id_line.setEnabled(False)
        self.new_pass_id_line.setGeometry(QtCore.QRect(401, 310, 181, 24))

        self.new_password_line = QLineEdit(self.accounts_tab)
        self.new_password_line.setPlaceholderText("New Password")
        self.new_password_line.setEnabled(False)
        self.new_password_line.setGeometry(QtCore.QRect(401, 340, 181, 24))

        self.search_reports_line = QLineEdit(self.reports_tab)
        self.search_reports_line.setPlaceholderText("Search reports for...")
        self.search_reports_line.setGeometry(QtCore.QRect(340, 190, 241, 24))
        self.search_reports_line.setAlignment(QtCore.Qt.AlignCenter)

        # LABELS
        self.create_user_label = QLabel(self.accounts_tab)
        self.create_user_label.setText("Create User")
        self.create_user_label.setGeometry(QtCore.QRect(400, 120, 71, 16))

        self.last_login_label = QLabel(self.accounts_tab)
        self.last_login_label.setText("Last Login:")
        self.last_login_label.setGeometry(QtCore.QRect(160, 500, 71, 16))

        self.reports_filed_label = QLabel(self.accounts_tab)
        self.reports_filed_label.setText("Reports Filed:")
        self.reports_filed_label.setGeometry(QtCore.QRect(10, 500, 91, 16))

        self.technician_label = QLabel(self.accounts_tab)
        self.technician_label.setText("Technician Login")
        self.technician_label.setGeometry(QtCore.QRect(400, 10, 101, 16))

        self.reset_password_label = QLabel(self.accounts_tab)
        self.reset_password_label.setText("Reset Password")
        self.reset_password_label.setEnabled(False)
        self.reset_password_label.setGeometry(QtCore.QRect(401, 290, 91, 16))

        # BUTTONS

        self.technician_login_button = QPushButton(self.accounts_tab)
        self.technician_login_button.setText("Login")
        self.technician_login_button.setGeometry(QtCore.QRect(529, 90, 51, 24))

        self.change_username_button = QPushButton(self.accounts_tab)
        self.change_username_button.setText("Change")
        self.change_username_button.setEnabled(False)
        self.change_username_button.setGeometry(QtCore.QRect(310, 440, 80, 24))

        self.change_email_button = QPushButton(self.accounts_tab)
        self.change_email_button.setText("Change")
        self.change_email_button.setEnabled(False)
        self.change_email_button.setGeometry(QtCore.QRect(310, 470, 80, 24))

        self.create_user_button = QPushButton(self.accounts_tab)
        self.create_user_button.setText("Create")
        self.create_user_button.setEnabled(False)
        self.create_user_button.setGeometry(QtCore.QRect(529, 260, 51, 24))

        self.reset_password_button = QPushButton(self.accounts_tab)
        self.reset_password_button.setText("Reset")
        self.reset_password_button.setEnabled(False)
        self.reset_password_button.setGeometry(QtCore.QRect(530, 370, 51, 24))

        self.delete_user_button = QPushButton(self.accounts_tab)
        self.delete_user_button.setText("Delete Selected User")
        self.delete_user_button.setEnabled(False)
        self.delete_user_button.setGeometry(QtCore.QRect(450, 500, 131, 24))

        self.update_report_button = QPushButton(self.reports_tab)
        self.update_report_button.setText("PushButton")
        self.update_report_button.setGeometry(QtCore.QRect(500, 500, 80, 24))

        # TABLES
        self.accounts_table = QTableWidget(self.accounts_tab)
        self.accounts_table.setEnabled(False)
        self.accounts_table.setGeometry(QtCore.QRect(10, 10, 381, 391))
        self.accounts_table.setRowCount(0)
        self.accounts_table.setColumnCount(4)
        item = QTableWidgetItem()
        self.accounts_table.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.accounts_table.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.accounts_table.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.accounts_table.setHorizontalHeaderItem(3, item)
        self.accounts_table.setSortingEnabled(True)
        item = self.accounts_table.horizontalHeaderItem(0)
        item.setText("Username")
        item = self.accounts_table.horizontalHeaderItem(1)
        item.setText("Email")
        item = self.accounts_table.horizontalHeaderItem(2)
        item.setText("Reports Filed")
        item = self.accounts_table.horizontalHeaderItem(3)
        item.setText("Last Login")

        self.reports_table = QTableWidget(self.reports_tab)
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

        # TEXT BROWSERS
        self.report_text_browser = QTextBrowser(self.reports_tab)
        self.report_text_browser.setGeometry(QtCore.QRect(10, 190, 321, 331))

        # GRAPHICS VIEW
        self.screenshot_view = QGraphicsView(self.reports_tab)
        self.screenshot_view.setGeometry(QtCore.QRect(340, 220, 241, 121))

        # TEXT BOX
        self.technician_report_notes = QTextEdit(self.reports_tab)
        self.technician_report_notes.setGeometry(QtCore.QRect(340, 350, 241, 141))

        # COMBO BOX
        self.case_status_combo_box = QComboBox(self.reports_tab)
        self.case_status_combo_box.setGeometry(QtCore.QRect(340, 500, 151, 24))
        self.case_status_combo_box.addItem("Case Open")
        self.case_status_combo_box.addItem("Case In Progress")
        self.case_status_combo_box.addItem("Case Closed - Fixed")
        self.case_status_combo_box.addItem("Not A Bug")

        self.worker_type_combo_box = QComboBox(self.accounts_tab)
        self.worker_type_combo_box.setEnabled(False)
        self.worker_type_combo_box.setGeometry(QtCore.QRect(400, 230, 181, 24))
        self.worker_type_combo_box.addItem("Employee")
        self.worker_type_combo_box.addItem("Manager")
        self.worker_type_combo_box.addItem("Supervisor")
        self.worker_type_combo_box.addItem("Department Head")

        QtCore.QMetaObject.connectSlotsByName(self)
        self.setCentralWidget(self.central_widget)

        self.show()


# if __name__ == "__main__":
#     import sys
#
#     app = QApplication(sys.argv)
#     MainWindow = QMainWindow()
#     ui = TechnicianMainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
