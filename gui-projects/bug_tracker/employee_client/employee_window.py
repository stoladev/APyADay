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

from employee_client.modules.loaders import widget_loader


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
        widget_loader.load_all_widgets(self)
        self.update_preview()

    def size_policy_setup(self):
        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)

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
