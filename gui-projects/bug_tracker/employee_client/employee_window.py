"""
Initializes window widgets for the employee application. Points to and runs customizations and
specifications of execution/registered events.
"""

import os
import platform
from zipfile import ZipFile

import pyautogui
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QCheckBox,
    QGraphicsPixmapItem,
    QGraphicsScene,
    QGraphicsView,
    QGridLayout,
    QLabel,
    QMainWindow,
    QMenuBar,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QTextBrowser,
    QTextEdit,
    QWidget,
)


class EmployeeMainWindow(QMainWindow):
    """
    Handles the initiation of the main employee window, along with calling any setup
    configurations and/or event updates.
    """

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
        self.grid_layout_widget = QWidget(self.central_widget)
        self.grid_layout_widget_2 = QWidget(self.central_widget)
        self.data_layout = QGridLayout(self.grid_layout_widget)
        self.questions_layout = QGridLayout(self.grid_layout_widget_2)
        self.report_view = QTextBrowser(self.central_widget)
        self.screenshot_view = QGraphicsView(self.central_widget)
        self.generate_button = QPushButton(self.central_widget)
        self.screenshot_button = QPushButton(self.central_widget)
        self.add_info_box = QTextEdit(self.central_widget)
        self.preview_label = QLabel(self.central_widget)
        self.data_label = QLabel(self.grid_layout_widget)
        self.questions_label = QLabel(self.grid_layout_widget_2)
        self.menu_bar = QMenuBar(self)
        self.env_checkbox = QCheckBox(self.grid_layout_widget)
        self.site_checkbox = QCheckBox(self.grid_layout_widget)
        self.program_checkbox = QCheckBox(self.grid_layout_widget)
        self.crash_checkbox = QCheckBox(self.grid_layout_widget)
        self.reproducible_checkbox = QCheckBox(self.grid_layout_widget_2)
        self.profits_checkbox = QCheckBox(self.grid_layout_widget_2)
        self.leak_checkbox = QCheckBox(self.grid_layout_widget_2)
        self.security_checkbox = QCheckBox(self.grid_layout_widget_2)

        # CLEAR ANY CURRENT SCREENSHOTS
        self.report_path = "report/report.txt"
        self.zipfile_path = "report/zipped_report.zip"
        self.screenshot_path = "report/screenshot.png"
        if os.path.exists(self.screenshot_path):
            os.remove(self.screenshot_path)

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
        self.grid_layout_widget.setGeometry(QtCore.QRect(10, 20, 165, 131))
        self.grid_layout_widget_2.setGeometry(QtCore.QRect(180, 20, 159, 131))
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
        self.generate_button.setText("Generate Report")
        self.generate_button.setGeometry(QtCore.QRect(210, 320, 131, 71))
        self.generate_button.pressed.connect(self.generate_report)
        # SCREENSHOT BUTTON
        self.screenshot_button.setText("Take A Screenshot")
        self.screenshot_button.setGeometry(QtCore.QRect(210, 280, 131, 31))
        self.screenshot_button.pressed.connect(self.take_screenshot)

        # TEXT BOX
        self.add_info_box.setPlaceholderText("Additional information...")
        self.add_info_box.setGeometry(QtCore.QRect(10, 160, 331, 111))
        self.add_info_box.textChanged.connect(self.update_preview)

        # PREVIEW LABEL
        self.preview_label.setText("Report Preview")
        self.preview_label.setGeometry(QtCore.QRect(350, 0, 91, 17))
        self.preview_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        # DATA LABEL
        self.data_layout.addWidget(self.data_label, 0, 0, 1, 1)
        # QUESTIONS LABEL
        self.questions_layout.addWidget(self.questions_label, 0, 0, 1, 1)

        # MENU BAR
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 691, 21))
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
        self.program_checkbox.stateChanged.connect(self.check_issue_type)
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

    def check_issue_type(self):
        check_status = self.program_checkbox.isChecked()

        self.crash_checkbox.setEnabled(check_status)

        if self.site_checkbox.isChecked() & self.program_checkbox.isChecked():
            issue_type = "Issue Type:\nWebsite and Program Related\n\n"
        elif self.site_checkbox.isChecked():
            issue_type = "Issue Type:\nWebsite Related\n\n"
        elif self.program_checkbox.isChecked():
            issue_type = "Issue Type:\nProgram Related\n\n"
        else:
            issue_type = ""

        return issue_type

    def update_preview(self):

        issue_type = self.check_issue_type()

        environment = (
            "Environment:\n" + platform.system() + " " + platform.release() + "\n\n"
        )
        additional_details = (
            "Additional Details:\n" + self.add_info_box.toPlainText() + "\n\n"
        )

        main_details = [
            [self.crash_checkbox.isChecked(), "Crash Report:\nAttached\n\n"],
            [self.env_checkbox.isChecked(), environment],
            [self.add_info_box.toPlainText() != "", additional_details],
        ]

        questions = [
            [self.reproducible_checkbox.isChecked(), "Reproducible: "],
            [self.profits_checkbox.isChecked(), "Affecting Profits: "],
            [self.security_checkbox.isChecked(), "Security Risk: "],
            [self.leak_checkbox.isChecked(), "Data Leak: "],
        ]

        report = ""

        for detail in main_details:
            if detail[0]:
                report += detail[1]

        for question in questions:
            if question[0]:
                report += question[1] + "Yes\n"
            else:
                report += question[1] + "No\n"

        self.report_view.setText(issue_type + report)

    def take_screenshot(self):

        if os.path.exists(self.screenshot_path):
            os.remove(self.screenshot_path)

        dialogue = QMessageBox.question(
            self,
            "Confirmation",
            "A screenshot is about to be taken of all your active monitors. Please make sure to "
            "have the website and/or program related issue(s) open and visible.\n\nAre you ready "
            "to take a screenshot?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if dialogue == QMessageBox.Yes:
            pyautogui.screenshot(self.screenshot_path)
            pixmap = QPixmap(self.screenshot_path)
            item = QGraphicsPixmapItem(pixmap)
            scene = QGraphicsScene(self)
            scene.addItem(item)
            self.screenshot_view.setScene(scene)
            self.screenshot_view.ensureVisible(scene.sceneRect())
            self.screenshot_view.fitInView(
                scene.sceneRect(), mode=QtCore.Qt.KeepAspectRatio
            )

            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText("Screenshot successfully taken.")
            msg.exec_()

    def generate_report(self):
        dialogue = QMessageBox.question(
            self,
            "Confirmation",
            "A zip file containing your report and screenshot, if taken, will be generated "
            "in the same directory you are running this executable from.\n\nAre you ready "
            "to generate the report?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if dialogue == QMessageBox.Yes:

            if os.path.exists(self.report_path):
                os.remove(self.report_path)

            data = self.report_view.toPlainText()

            with open(self.report_path, "w") as report:
                report.write(data)

            with ZipFile(self.zipfile_path, "w") as zipObj2:
                zipObj2.write(self.report_path, "report.txt")
                if os.path.exists(self.screenshot_path):
                    zipObj2.write(self.screenshot_path, "screenshot.png")

            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText("Report successfully generated.")
            msg.exec_()
