import platform
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QSizePolicy, QWidget,
                             QGridLayout, QTextBrowser, QGraphicsView, QTextEdit, QLabel,
                             QMenuBar, QCheckBox)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # GENERAL SETTINGS
        self.setWindowTitle("Report Window")
        self.setEnabled(True)
        self.setFixedSize(690, 400)
        self.central_widget = QWidget(self)
        self.central_widget.setObjectName("central_widget")
        self.setCentralWidget(self.central_widget)

        # WIDGET INITIALIZATION
        self.gridLayoutWidget = QWidget(self.central_widget)
        self.gridLayoutWidget_2 = QWidget(self.central_widget)
        self.data_layout = QGridLayout(self.gridLayoutWidget)
        self.questions_layout = QGridLayout(self.gridLayoutWidget_2)
        self.report_view = QTextBrowser(self.central_widget)
        self.screenshot_view = QGraphicsView(self.central_widget)
        self.submit_button = QPushButton(self.central_widget)
        self.screenshot_button = QPushButton(self.central_widget)
        self.add_info_box = QTextEdit(self.central_widget)
        self.preview_label = QLabel(self.central_widget)
        self.data_label = QLabel(self.gridLayoutWidget)
        self.questions_label = QLabel(self.gridLayoutWidget_2)
        self.menu_bar = QMenuBar(self)
        self.env_checkbox = QCheckBox(self.gridLayoutWidget)
        self.site_checkbox = QCheckBox(self.gridLayoutWidget)
        self.program_checkbox = QCheckBox(self.gridLayoutWidget)
        self.crash_checkbox = QCheckBox(self.gridLayoutWidget)
        self.reproducible_checkbox = QCheckBox(self.gridLayoutWidget_2)
        self.profits_checkbox = QCheckBox(self.gridLayoutWidget_2)
        self.leak_checkbox = QCheckBox(self.gridLayoutWidget_2)
        self.security_checkbox = QCheckBox(self.gridLayoutWidget_2)

        # ACTIVATION
        self.widget_setup()
        self.update_preview()

    def size_policy_setup(self):
        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)

    def widget_setup(self):
        # GRID LAYOUT
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 165, 131))
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(180, 20, 159, 131))
        # DATA LAYOUT
        self.data_label.setText("Need-To-Know Data")
        self.data_layout.setContentsMargins(0, 0, 0, 0)
        # QUESTIONS LAYOUT
        self.questions_label.setText("Questionaire")
        self.questions_layout.setContentsMargins(0, 0, 0, 0)

        # TEXT VIEWER
        self.report_view.setGeometry(QtCore.QRect(350, 20, 331, 371))
        self.report_view.setLayoutDirection(QtCore.Qt.RightToLeft)
        # GRAPHICS VIEWER
        self.screenshot_view.setGeometry(QtCore.QRect(10, 280, 191, 111))

        # SUBMIT BUTTON
        self.submit_button.setText("Submit Bug Report")
        self.submit_button.setGeometry(QtCore.QRect(210, 320, 131, 71))
        # SCREENSHOT BUTTON
        self.screenshot_button.setText("Take A Screenshot")
        self.screenshot_button.setGeometry(QtCore.QRect(210, 280, 131, 31))

        # TEXT BOX
        self.add_info_box.setPlaceholderText("Additional information...")
        self.add_info_box.setGeometry(QtCore.QRect(10, 160, 331, 111))
        self.add_info_box.textChanged.connect(self.update_preview)

        # PREVIEW LABEL
        self.preview_label.setText("Report Preview")
        self.preview_label.setGeometry(QtCore.QRect(350, 0, 91, 17))
        self.preview_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        # DATA LABEL
        self.data_label.setObjectName("data_label")
        self.data_layout.addWidget(self.data_label, 0, 0, 1, 1)
        # QUESTIONS LABEL
        self.questions_label.setObjectName("questions_label")
        self.questions_layout.addWidget(self.questions_label, 0, 0, 1, 1)

        # MENU BAR
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 691, 21))
        self.menu_bar.setObjectName("menu_bar")
        self.setMenuBar(self.menu_bar)

        # ENVIRONMENT CHECKBOX
        self.env_checkbox.setText("Environment")
        self.data_layout.addWidget(self.env_checkbox, 2, 0, 1, 1)
        self.env_checkbox.stateChanged.connect(self.update_preview)
        # SITE CHECKBOX
        self.site_checkbox.setText("Website Issue")
        self.data_layout.addWidget(self.site_checkbox, 3, 0, 1, 1)
        self.site_checkbox.stateChanged.connect(self.update_preview)
        # PROGRAM CHECKBOX
        self.program_checkbox.setText("Program Issue")
        self.data_layout.addWidget(self.program_checkbox, 4, 0, 1, 1)
        self.program_checkbox.stateChanged.connect(self.check_state)
        self.program_checkbox.stateChanged.connect(self.update_preview)
        # CRASH CHECKBOX
        self.crash_checkbox.setText("Crash Report")
        self.data_layout.addWidget(self.crash_checkbox, 5, 0, 1, 1)
        self.crash_checkbox.setEnabled(False)
        self.crash_checkbox.stateChanged.connect(self.update_preview)
        # REPRODUCIBLE CHECKBOX
        self.reproducible_checkbox.setText("Reproducible?")
        self.questions_layout.addWidget(self.reproducible_checkbox, 1, 0, 1, 1)
        self.reproducible_checkbox.stateChanged.connect(self.update_preview)
        # PROFITS CHECKBOX
        self.profits_checkbox.setText("Affecting Profits?")
        self.profits_checkbox.setObjectName("profits_checkbox")
        self.questions_layout.addWidget(self.profits_checkbox, 2, 0, 1, 1)
        self.profits_checkbox.stateChanged.connect(self.update_preview)
        # LEAK CHECKBOX
        self.leak_checkbox.setText("Data Leak?")
        self.questions_layout.addWidget(self.leak_checkbox, 4, 0, 1, 1)
        self.leak_checkbox.stateChanged.connect(self.update_preview)
        # SECURITY CHECKBOX
        self.security_checkbox.setText("Security Risk?")
        self.questions_layout.addWidget(self.security_checkbox, 3, 0, 1, 1)
        self.security_checkbox.stateChanged.connect(self.update_preview)

        QtCore.QMetaObject.connectSlotsByName(self)

    def check_state(self):
        check_status = self.program_checkbox.isChecked()

        self.crash_checkbox.setEnabled(check_status)
        self.crash_checkbox.setChecked(check_status)

    def update_preview(self):

        if self.env_checkbox.isChecked():
            env = platform.platform() + "\nPython " + platform.python_version()
            env_details = "Environment:\n" + env + "\n\n"
        else:
            env_details = ""

        if self.site_checkbox.isChecked() & self.program_checkbox.isChecked():
            issue_type_details = "Issue Type:\nWebsite AND Program Related\n\n"
        elif self.site_checkbox.isChecked():
            issue_type_details = "Issue Type:\nWebsite Related\n\n"
        elif self.program_checkbox.isChecked():
            issue_type_details = "Issue Type:\nProgram Related\n\n"
        else:
            issue_type_details = ""

        if self.reproducible_checkbox.isChecked():
            reproducible_details = "Reproducible: Yes\n"
        else:
            reproducible_details = "Reproducible: No\n"

        if self.profits_checkbox.isChecked():
            profits_details = "Affecting Profits: Yes\n"
        else:
            profits_details = "Affecting Profits: No\n"

        if self.security_checkbox.isChecked():
            security_details = "Security Risk: Yes\n"
        else:
            security_details = "Security Risk: No\n"

        if self.leak_checkbox.isChecked():
            leak_details = "Data Leak: Yes\n"
        else:
            leak_details = "Data Leak: No\n"

        if not self.add_info_box.toPlainText() == "":
            additional_details = "\nAdditional Details: \n" + self.add_info_box.toPlainText() + "\n"
        else:
            additional_details = "\nNo additional details provided.\n"

        if self.crash_checkbox.isChecked():
            crash_report_details = "\nCrash Report: Attached"
        else:
            crash_report_details = ""

        self.report_view.setText(env_details + issue_type_details
                                 + reproducible_details
                                 + profits_details + security_details
                                 + leak_details + additional_details + crash_report_details)
