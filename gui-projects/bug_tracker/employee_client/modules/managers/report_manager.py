"""
This is the manager of all report-related functions, ranging from checking what type of issue the
report is, to finalizing and uploading the finished report to the appropriate MongoDB.
"""

# pylint: disable=import-error
# Reason: Importing is working fine, but pylint begs to differ. Most likely because of venv.

from PyQt5 import QtWidgets

from employee_client.modules.managers import action_manager


def generate_report(window):
    """
    Generates the report, translating the screenshot (if created) and report files into byte
    code, finally uploading it to MongoDB.

    :param window: The QApplication in use.
    :return: Uploads the report to MongoDB.
    """

    reports = window.database.reports
    account_name = window.account_name
    data = window.report_view.toPlainText()

    encoded_image = action_manager.process_screenshot(window)

    if encoded_image is not None:
        upload_report(window, reports, account_name, data, encoded_image)
    else:
        return


def upload_report(window, reports, account_name, data, encoded_image):
    """
    Uploads the generated report to MongoDB.

    :param window: The QMainWindow in use.
    :param reports: The reports collection used for inserting the new report.
    :param account_name: The account name of the uploader.
    :param data: The data for the report to be uploaded.
    :param encoded_image: The image to upload, which is either 0 or encoded in base64.
    :return: A successful report upload.
    """

    reports.insert(
        {
            "account_name": account_name,
            "report": data,
            "screenshot": encoded_image,
            "submitted_on": 0,
        }
    )

    reports.update(
        {"account_name": account_name, "submitted_on": 0},
        {"$currentDate": {"submitted_on": True}},
    )

    update_reports_filed(window, account_name, reports)

    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Success")
    msg.setText("Report successfully generated.")
    msg.exec_()


def update_reports_filed(window, account_name, reports):
    """
    Updates the number of an account's reports filed by 1.

    :param window: The QMainWindow in use.
    :param account_name: The account name to update the amount of reports they have filed.
    :param reports: The list of reports to count against when updating.
    :return: An increase of 1 to an account's report's filed.
    """

    accounts = window.database.accounts

    matched_reports = reports.find({"account_name": account_name})
    report_count = matched_reports.count()

    accounts.update(
        {"account_name": account_name}, {"$set": {"reports_filed": report_count}}
    )

    print(report_count)
