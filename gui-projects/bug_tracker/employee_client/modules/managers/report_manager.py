"""
This is the manager of all report-related functions, ranging from checking what type of issue the
report is, to finalizing and uploading the finished report to the appropriate MongoDB.
"""

import os
import platform

import pyautogui
from PyQt5 import QtCore, QtGui, QtWidgets


def check_issue_type(window):
    """
    Checks the issue type by going through which issue-related checkboxes are checked, or if both
    of them are checked.

    :param window: The QApplication in use.
    :return: Updates the issue type line in the report.
    """
    check_status = window.program_checkbox.isChecked()

    window.crash_checkbox.setEnabled(check_status)

    if window.site_checkbox.isChecked() & window.program_checkbox.isChecked():
        issue_type = "Issue Type:\nWebsite and Program Related\n\n"
    elif window.site_checkbox.isChecked():
        issue_type = "Issue Type:\nWebsite Related\n\n"
    elif window.program_checkbox.isChecked():
        issue_type = "Issue Type:\nProgram Related\n\n"
    else:
        issue_type = ""

    return issue_type


def update_preview(window):
    """
    Updates the preview of the review textbox in real-time for the employee to see a visual
    representation of how their final report will look like when sent.

    :param window: The QApplication in use.
    :return: Updates the preview textbox.
    """
    issue_type = check_issue_type(window)

    environment = (
        "Environment:\n" + platform.system() + " " + platform.release() + "\n\n"
    )
    additional_details = (
        "Additional Details:\n" + window.add_info_box.toPlainText() + "\n\n"
    )

    main_details = [
        [window.crash_checkbox.isChecked(), "Crash Report:\nAttached\n\n"],
        [window.env_checkbox.isChecked(), environment],
        [window.add_info_box.toPlainText() != "", additional_details],
    ]

    questions = [
        [window.reproducible_checkbox.isChecked(), "Reproducible: "],
        [window.profits_checkbox.isChecked(), "Affecting Profits: "],
        [window.security_checkbox.isChecked(), "Security Risk: "],
        [window.leak_checkbox.isChecked(), "Data Leak: "],
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

    window.report_view.setText(issue_type + report)


def take_screenshot(window):
    """
    Takes a screenshot of the employee's entire desktop view (no matter how many monitors are
    being utilized).

    :param window: The QApplication in use.
    :return: Attaches the new screenshot into the screenshot preview viewer.
    """

    dialogue = QtWidgets.QMessageBox.question(
        window,
        "Confirmation",
        "A screenshot is about to be taken of all your active monitors. Please make sure to "
        "have the website and/or program related issue(s) open and visible.\n\nAre you ready "
        "to take a screenshot?",
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
    )
    if dialogue == QtWidgets.QMessageBox.Yes:
        pyautogui.screenshot(window.screenshot_path)
        pixmap = QtGui.QPixmap(window.screenshot_path)
        item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene = QtWidgets.QGraphicsScene(window)
        scene.addItem(item)
        window.screenshot_view.setScene(scene)
        window.screenshot_view.ensureVisible(scene.sceneRect())
        window.screenshot_view.fitInView(
            scene.sceneRect(), mode=QtCore.Qt.KeepAspectRatio
        )

        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Success")
        msg.setText("Screenshot successfully taken.")
        msg.exec_()


def generate_report(window):
    """
    Generates the report, translating the screenshot (if created) and report files into byte
    code, finally uploading it to MongoDB.

    :param window: The QApplication in use.
    :return: Uploads the report to MongoDB.
    """
    dialogue = QtWidgets.QMessageBox.question(
        window,
        "Confirmation",
        "A zip file containing your report and screenshot, if taken, will be generated "
        "in the same directory you are running this executable from.\n\nAre you ready "
        "to generate the report?",
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
    )
    if dialogue == QtWidgets.QMessageBox.Yes:

        if os.path.exists(window.report_path):
            os.remove(window.report_path)

        data = window.report_view.toPlainText()

        # with open(window.report_path, "w") as report:
        #     report.write(data)
        #
        # with ZipFile(window.zipfile_path, "w") as zip_object:
        #     zip_object.write(window.report_path, "report.txt")
        #     if os.path.exists(window.screenshot_path):
        #         zip_object.write(window.screenshot_path, "screenshot.png")

        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Success")
        msg.setText("Report successfully generated.")
        msg.exec_()
