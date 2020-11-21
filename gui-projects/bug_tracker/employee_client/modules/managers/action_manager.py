"""
Handles all actions that do specific operations for checking, generating, updating, or similar.
"""
import base64
import os
import platform
import tempfile

import pyautogui
from PyQt5 import QtCore, QtGui, QtWidgets


def check_issue_type(window):
    """
    Checks the issue type by going through which issue-related checkboxes are checked, or if both
    of them are checked.

    :param window: The QApplication in use.
    :return: Updates the issue type line in the report.
    """

    # check_status = window.program_checkbox.isChecked()
    # window.crash_checkbox.setEnabled(check_status)

    if window.site_checkbox.isChecked() & window.program_checkbox.isChecked():
        issue_type = "Website and Program Related"
    elif window.site_checkbox.isChecked():
        issue_type = "Website Related"
    elif window.program_checkbox.isChecked():
        issue_type = "Program Related"
    else:
        issue_type = None

    if not window.program_checkbox.isChecked():
        window.crash_checkbox.setChecked(False)
        window.crash_checkbox.setEnabled(False)
    else:
        window.crash_checkbox.setEnabled(True)

    return issue_type


def update_preview(window):
    """
    Updates the preview of the review textbox in real-time for the employee to see a visual
    representation of how their final report will look like when sent.

    :param window: The QApplication in use.
    :return: Updates the preview textbox.
    """
    issue_type = check_issue_type(window)

    if issue_type is None:
        issue_type = ""
    else:
        issue_type = "Issue Type:\n" + issue_type + "\n\n"

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
        scene = generate_png(window)

        window.screenshot_view.setScene(scene)
        window.screenshot_view.ensureVisible(scene.sceneRect())
        window.screenshot_view.fitInView(
            scene.sceneRect(), mode=QtCore.Qt.KeepAspectRatio
        )

        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Success")
        msg.setText("Screenshot successfully taken.")
        msg.exec_()


def generate_png(window):
    """
    Generates the image using pyautogui.

    :param window: The QMainWindow in use.
    :return: The compiled scene for display.
    """

    screenshot_path = tempfile.NamedTemporaryFile(
        suffix=".png", prefix=os.path.basename(__file__), delete=True
    ).name
    pyautogui.screenshot(screenshot_path)
    pixmap = QtGui.QPixmap(screenshot_path)
    item = QtWidgets.QGraphicsPixmapItem(pixmap)
    scene = QtWidgets.QGraphicsScene(window)
    scene.addItem(item)

    return scene


def png_to_base64(image):
    """
    Converts a screenshot into bas64 code.

    :param image: The image to convert.
    :return: Base64 code of the image.
    """

    with open(image, "rb") as image_file:
        base_64_data = base64.b64encode(image_file.read())

    return base_64_data


def process_screenshot(window):
    """
    Processes the screenshot, if applicable, to base64 for easier MongoDB upload.
    :param window: The QMainWindow in use.
    :return: Either the encoded image in base64, or null.
    """

    screenshot = window.screenshot_path

    try:
        encoded_image = png_to_base64(screenshot)
        return encoded_image
    except FileNotFoundError:
        msg = QtWidgets.QMessageBox().question(
            window,
            "No Screenshot Attached",
            "Are you sure you want to continue with "
            "the report upload without a screenshot of the issue?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No,
        )
        if msg == QtWidgets.QMessageBox.Yes:
            encoded_image = "N/A"
            return encoded_image
