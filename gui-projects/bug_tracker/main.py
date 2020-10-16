from PyQt5 import QtCore, QtGui, QtWidgets




class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.setEnabled(True)
        main_window.resize(690, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.central_widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 165, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.data_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.data_layout.setContentsMargins(0, 0, 0, 0)
        self.data_layout.setObjectName("data_layout")
        self.env_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.env_checkbox.setObjectName("env_checkbox")
        self.data_layout.addWidget(self.env_checkbox, 2, 0, 1, 1)
        self.data_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.data_label.setObjectName("data_label")
        self.data_layout.addWidget(self.data_label, 0, 0, 1, 1)
        self.site_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.site_checkbox.setObjectName("site_checkbox")
        self.data_layout.addWidget(self.site_checkbox, 3, 0, 1, 1)
        self.program_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.program_checkbox.setObjectName("program_checkbox")
        self.data_layout.addWidget(self.program_checkbox, 4, 0, 1, 1)
        self.crash_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.crash_checkbox.setEnabled(False)
        self.crash_checkbox.setObjectName("crash_checkbox")
        self.data_layout.addWidget(self.crash_checkbox, 5, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.central_widget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(180, 20, 159, 131))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.questions_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.questions_layout.setContentsMargins(0, 0, 0, 0)
        self.questions_layout.setObjectName("questions_layout")
        self.profits_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.profits_checkbox.setObjectName("profits_checkbox")
        self.questions_layout.addWidget(self.profits_checkbox, 2, 0, 1, 1)
        self.leak_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.leak_checkbox.setObjectName("leak_checkbox")
        self.questions_layout.addWidget(self.leak_checkbox, 4, 0, 1, 1)
        self.reproducible_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.reproducible_checkbox.setObjectName("reproducible_checkbox")
        self.questions_layout.addWidget(self.reproducible_checkbox, 1, 0, 1, 1)
        self.security_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.security_checkbox.setObjectName("security_checkbox")
        self.questions_layout.addWidget(self.security_checkbox, 3, 0, 1, 1)
        self.questions_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.questions_label.setObjectName("questions_label")
        self.questions_layout.addWidget(self.questions_label, 0, 0, 1, 1)
        self.report_browser = QtWidgets.QTextBrowser(self.central_widget)
        self.report_browser.setGeometry(QtCore.QRect(350, 20, 331, 371))
        self.report_browser.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.report_browser.setObjectName("report_browser")
        self.screenshot_view = QtWidgets.QGraphicsView(self.central_widget)
        self.screenshot_view.setGeometry(QtCore.QRect(10, 280, 191, 111))
        self.screenshot_view.setObjectName("screenshot_view")
        self.submit_button = QtWidgets.QPushButton(self.central_widget)
        self.submit_button.setGeometry(QtCore.QRect(210, 320, 131, 71))
        self.submit_button.setObjectName("submit_button")
        self.screenshot_button = QtWidgets.QPushButton(self.central_widget)
        self.screenshot_button.setGeometry(QtCore.QRect(210, 280, 131, 31))
        self.screenshot_button.setObjectName("screenshot_button")
        self.add_info_box = QtWidgets.QTextEdit(self.central_widget)
        self.add_info_box.setGeometry(QtCore.QRect(10, 160, 331, 111))
        self.add_info_box.setObjectName("add_info_box")
        self.preview_label = QtWidgets.QLabel(self.central_widget)
        self.preview_label.setGeometry(QtCore.QRect(350, 0, 91, 17))
        self.preview_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.preview_label.setObjectName("preview_label")
        main_window.setCentralWidget(self.central_widget)
        self.menu_bar = QtWidgets.QMenuBar(main_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 691, 21))
        self.menu_bar.setObjectName("menu_bar")
        main_window.setMenuBar(self.menu_bar)

        # Updates
        self.program_checkbox.stateChanged.connect(self.check_state)
        self.env_checkbox.stateChanged.connect(self.update_preview)
        self.site_checkbox.stateChanged.connect(self.update_preview)
        self.program_checkbox.stateChanged.connect(self.update_preview)
        self.crash_checkbox.stateChanged.connect(self.update_preview)
        self.reproducible_checkbox.stateChanged.connect(self.update_preview)
        self.profits_checkbox.stateChanged.connect(self.update_preview)
        self.security_checkbox.stateChanged.connect(self.update_preview)
        self.leak_checkbox.stateChanged.connect(self.update_preview)

        self.translate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)


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
        if self.program_checkbox.isChecked():
            self.crash_checkbox.setEnabled(True)
        else:
            self.crash_checkbox.setEnabled(False)
            self.crash_checkbox.setChecked(False)

    def update_preview(self):

        env_details = ""
        issue_type_details = ""
        crash_report_details = ""
        reproducible_details = ""
        profits_details = ""
        security_details = ""
        leak_details = ""
        additional_details = ""

        if self.env_checkbox.isChecked():
            env_details = "Environment: ENV DETAILS"
        else:
            env_details = "Environment: N/A"

        if self.site_checkbox.isChecked():
            issue_type_details = "Issue Type: Website Related"
        elif self.program_checkbox.isChecked():
            issue_type_details = "Issue Type: Program Related"
        elif self.site_checkbox.isChecked() & self.program_checkbox.isChecked():
            issue_type_details = "Issue Type: Website AND Program Related"
        else:
            issue_type_details = "Issue Type: N/A"

        if self.crash_checkbox.isChecked():
            crash_report_details = "Crash Report: Attached"
        else:
            crash_report_details = "Crash Report: N/A"

        if self.reproducible_checkbox.isChecked():
            reproducible_details = "Reproducible: Yes"
        else:
            reproducible_details = "Reproducible: No"

        if self.profits_checkbox.isChecked():
            profits_details = "Affecting Profits: Yes"
        else:
            profits_details = "Affecting Profits: No"

        if self.security_checkbox.isChecked():
            security_details = "Security Risk: Yes"
        else:
            security_details = "Security Risk: No"

        if self.leak_checkbox.isChecked():
            leak_details = "Data Leak: Yes"
        else:
            leak_details = "Data Leak: No"

        self.report_browser.setText(env_details + "\n" + issue_type_details + "\n"
                                    + crash_report_details + "\n" + reproducible_details
                                    + "\n" + profits_details + "\n" + security_details
                                    + "\n" + leak_details + "\n" + additional_details)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    ui.update_preview()
    main_window.show()
    sys.exit(app.exec_())
