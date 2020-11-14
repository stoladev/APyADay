from PyQt5 import QtCore


def load_all_widgets(window):
    """
    Loads all of the application's widgets' properties.
    """
    load_menu_bar(window)
    load_layouts(window)
    load_viewers(window)
    load_text_boxes(window)
    load_labels(window)
    load_buttons(window)
    load_checkboxes(window)


def load_menu_bar(window):
    """
    Loads the menu bar's custom properties.
    """
    window.menu_bar.setGeometry(QtCore.QRect(0, 0, 691, 21))
    window.setMenuBar(window.menu_bar)


def load_layouts(window):
    """
    Loads all layouts' custom properties.
    """
    # GRID LAYOUT
    window.grid_layout_widget.setGeometry(QtCore.QRect(10, 20, 165, 131))
    window.grid_layout_widget_2.setGeometry(QtCore.QRect(180, 20, 159, 131))
    # DATA LAYOUT
    window.data_label.setText("Need-To-Know Data")
    window.data_layout.setContentsMargins(0, 0, 0, 0)
    # QUESTIONS LAYOUT
    window.questions_label.setText("Questionaire")
    window.questions_layout.setContentsMargins(0, 0, 0, 0)


def load_viewers(window):
    """
    Loads all viewers' custom properties.
    """
    # TEXT VIEWER
    window.report_view.setGeometry(QtCore.QRect(350, 20, 331, 371))
    window.report_view.setLayoutDirection(QtCore.Qt.RightToLeft)
    # GRAPHICS VIEWER
    window.screenshot_view.setGeometry(QtCore.QRect(10, 280, 191, 111))


def load_buttons(window):
    """
    Loads all buttons' custom properties.
    """
    # SUBMIT BUTTON
    window.generate_button.setText("Generate Report")
    window.generate_button.setGeometry(QtCore.QRect(210, 320, 131, 71))
    window.generate_button.pressed.connect(window.generate_report)
    # SCREENSHOT BUTTON
    window.screenshot_button.setText("Take A Screenshot")
    window.screenshot_button.setGeometry(QtCore.QRect(210, 280, 131, 31))
    window.screenshot_button.pressed.connect(window.take_screenshot)


def load_text_boxes(window):
    """
    Loads all text boxes' custom properties.
    """
    # ADDITIONAL INFO TEXT BOX
    window.add_info_box.setPlaceholderText("Additional information...")
    window.add_info_box.setGeometry(QtCore.QRect(10, 160, 331, 111))
    window.add_info_box.textChanged.connect(window.update_preview)


def load_labels(window):
    """
    Loads all labels' custom properties.
    """
    # PREVIEW LABEL
    window.preview_label.setText("Report Preview")
    window.preview_label.setGeometry(QtCore.QRect(350, 0, 91, 17))
    window.preview_label.setLayoutDirection(QtCore.Qt.RightToLeft)
    # DATA LABEL
    window.data_layout.addWidget(window.data_label, 0, 0, 1, 1)
    # QUESTIONS LABEL
    window.questions_layout.addWidget(window.questions_label, 0, 0, 1, 1)


def load_checkboxes(window):
    """
    Loads all checkboxes' custom properties.
    """
    # ENVIRONMENT CHECKBOX
    window.env_checkbox.setText("Environment")
    window.data_layout.addWidget(window.env_checkbox, 2, 0, 1, 1)
    window.env_checkbox.stateChanged.connect(window.update_preview)
    # SITE CHECKBOX
    window.site_checkbox.setText("Website Issue")
    window.data_layout.addWidget(window.site_checkbox, 3, 0, 1, 1)
    window.site_checkbox.stateChanged.connect(window.update_preview)
    # PROGRAM CHECKBOX
    window.program_checkbox.setText("Program Issue")
    window.data_layout.addWidget(window.program_checkbox, 4, 0, 1, 1)
    window.program_checkbox.stateChanged.connect(window.check_issue_type)
    window.program_checkbox.stateChanged.connect(window.update_preview)
    # CRASH CHECKBOX
    window.crash_checkbox.setText("Crash Report")
    window.data_layout.addWidget(window.crash_checkbox, 5, 0, 1, 1)
    window.crash_checkbox.setEnabled(False)
    window.crash_checkbox.stateChanged.connect(window.update_preview)
    # REPRODUCIBLE CHECKBOX
    window.reproducible_checkbox.setText("Reproducible?")
    window.questions_layout.addWidget(window.reproducible_checkbox, 1, 0, 1, 1)
    window.reproducible_checkbox.stateChanged.connect(window.update_preview)
    # PROFITS CHECKBOX
    window.profits_checkbox.setText("Affecting Profits?")
    window.questions_layout.addWidget(window.profits_checkbox, 2, 0, 1, 1)
    window.profits_checkbox.stateChanged.connect(window.update_preview)
    # LEAK CHECKBOX
    window.leak_checkbox.setText("Data Leak?")
    window.questions_layout.addWidget(window.leak_checkbox, 4, 0, 1, 1)
    window.leak_checkbox.stateChanged.connect(window.update_preview)
    # SECURITY CHECKBOX
    window.security_checkbox.setText("Security Risk?")
    window.questions_layout.addWidget(window.security_checkbox, 3, 0, 1, 1)
    window.security_checkbox.stateChanged.connect(window.update_preview)
