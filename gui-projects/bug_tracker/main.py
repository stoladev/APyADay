from PyQt5 import QtCore, QtGui, QtWidgets
import platform


# noinspection PyAttributeOutsideInit,PyShadowingNames
class Ui_main_window(object):
    def setupUi(self, main_window):

        # GENERAL SETTINGS
        main_window.setObjectName("main_window")
        main_window.setEnabled(True)
        main_window.setFixedSize(690, 400)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(size_policy)
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        main_window.setCentralWidget(self.central_widget)

        # LAYOUTS
        # Grid Layouts
        self.gridLayoutWidget = QtWidgets.QWidget(self.central_widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 165, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.central_widget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(180, 20, 159, 131))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        # Data Layout
        self.data_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.data_layout.setContentsMargins(0, 0, 0, 0)
        self.data_layout.setObjectName("data_layout")
        # Questions Layout
        self.questions_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.questions_layout.setContentsMargins(0, 0, 0, 0)
        self.questions_layout.setObjectName("questions_layout")

        # TEXT BROWSER
        self.report_browser = QtWidgets.QTextBrowser(self.central_widget)
        self.report_browser.setGeometry(QtCore.QRect(350, 20, 331, 371))
        self.report_browser.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.report_browser.setObjectName("report_browser")

        # GRAPHICS VIEWER
        self.screenshot_view = QtWidgets.QGraphicsView(self.central_widget)
        self.screenshot_view.setGeometry(QtCore.QRect(10, 280, 191, 111))
        self.screenshot_view.setObjectName("screenshot_view")

        # BUTTONS
        # Submit Button
        self.submit_button = QtWidgets.QPushButton(self.central_widget)
        self.submit_button.setGeometry(QtCore.QRect(210, 320, 131, 71))
        self.submit_button.setObjectName("submit_button")
        # Screenshot Button
        self.screenshot_button = QtWidgets.QPushButton(self.central_widget)
        self.screenshot_button.setGeometry(QtCore.QRect(210, 280, 131, 31))
        self.screenshot_button.setObjectName("screenshot_button")

        # TEXT BOX
        self.add_info_box = QtWidgets.QTextEdit(self.central_widget)
        self.add_info_box.setGeometry(QtCore.QRect(10, 160, 331, 111))
        self.add_info_box.setObjectName("add_info_box")

        # LABELS
        # Preview Label
        self.preview_label = QtWidgets.QLabel(self.central_widget)
        self.preview_label.setGeometry(QtCore.QRect(350, 0, 91, 17))
        self.preview_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.preview_label.setObjectName("preview_label")
        # Data Label
        self.data_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.data_layout.addWidget(self.data_label, 0, 0, 1, 1)
        self.data_label.setObjectName("data_label")
        # Questions Label
        self.questions_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.questions_label.setObjectName("questions_label")
        self.questions_layout.addWidget(self.questions_label, 0, 0, 1, 1)

        # MENU BAR
        self.menu_bar = QtWidgets.QMenuBar(main_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 691, 21))
        self.menu_bar.setObjectName("menu_bar")
        main_window.setMenuBar(self.menu_bar)

        # CHECKBOXES
        # Environment Checkbox
        self.env_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.env_checkbox.setObjectName("env_checkbox")
        self.data_layout.addWidget(self.env_checkbox, 2, 0, 1, 1)
        # Site Checkbox
        self.site_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.site_checkbox.setObjectName("site_checkbox")
        self.data_layout.addWidget(self.site_checkbox, 3, 0, 1, 1)
        # Program Checkbox
        self.program_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.program_checkbox.setObjectName("program_checkbox")
        self.data_layout.addWidget(self.program_checkbox, 4, 0, 1, 1)
        # Crash Checkbox
        self.crash_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.crash_checkbox.setObjectName("crash_checkbox")
        self.data_layout.addWidget(self.crash_checkbox, 5, 0, 1, 1)
        self.crash_checkbox.setEnabled(False)
        # Reproducible Checkbox
        self.reproducible_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.reproducible_checkbox.setObjectName("reproducible_checkbox")
        self.questions_layout.addWidget(self.reproducible_checkbox, 1, 0, 1, 1)
        # Profits Checkbox
        self.profits_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.profits_checkbox.setObjectName("profits_checkbox")
        self.questions_layout.addWidget(self.profits_checkbox, 2, 0, 1, 1)
        # Leak Checkbox
        self.leak_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.leak_checkbox.setObjectName("leak_checkbox")
        self.questions_layout.addWidget(self.leak_checkbox, 4, 0, 1, 1)
        # Security Checkbox
        self.security_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.security_checkbox.setObjectName("security_checkbox")
        self.questions_layout.addWidget(self.security_checkbox, 3, 0, 1, 1)

        self.state_update()

        self.translate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

        # UPDATES
    def state_update(self):
        # Checkbox Updates
        self.program_checkbox.stateChanged.connect(self.check_state)
        self.env_checkbox.stateChanged.connect(self.update_preview)
        self.site_checkbox.stateChanged.connect(self.update_preview)
        self.program_checkbox.stateChanged.connect(self.update_preview)
        self.crash_checkbox.stateChanged.connect(self.update_preview)
        self.reproducible_checkbox.stateChanged.connect(self.update_preview)
        self.profits_checkbox.stateChanged.connect(self.update_preview)
        self.security_checkbox.stateChanged.connect(self.update_preview)
        self.leak_checkbox.stateChanged.connect(self.update_preview)
        # Textbox Update
        self.add_info_box.textChanged.connect(self.update_preview)

    def translate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Bug Reporter 9001"))
        self.env_checkbox.setText(_translate("main_window", "Environment"))
        self.data_label.setText(_translate("main_window", "Need-To-Know Data"))
        self.site_checkbox.setText(_translate("main_window", "Website Issue"))
        self.program_checkbox.setText(_translate("main_window", "Program Issue"))
        self.crash_checkbox.setText(_translate("main_window", "Crash Report"))
        self.profits_checkbox.setText(_translate("main_window", "Affecting Profits?"))
        self.leak_checkbox.setText(_translate("main_window", "Data Leak?"))
        self.reproducible_checkbox.setText(_translate("main_window", "Reproducible?"))
        self.security_checkbox.setText(_translate("main_window", "Security Risk?"))
        self.questions_label.setText(_translate("main_window", "Questionaire"))
        self.submit_button.setText(_translate("main_window", "Submit Bug Report"))
        self.screenshot_button.setText(_translate("main_window", "Take A Screenshot"))
        self.add_info_box.setPlaceholderText(_translate("main_window", "Additional information..."))
        self.preview_label.setText(_translate("main_window", "Report Preview"))

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

        self.report_browser.setText(env_details + issue_type_details
                                    + reproducible_details
                                    + profits_details + security_details
                                    + leak_details + additional_details + crash_report_details)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    ui.update_preview()
    main_window.show()
    sys.exit(app.exec_())
