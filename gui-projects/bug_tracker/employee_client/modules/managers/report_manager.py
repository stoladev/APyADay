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

    issue_type = action_manager.check_issue_type(window)

    if issue_type is None:
        QtWidgets.QMessageBox.warning(
            window,
            "Issue Not Selected",
            "You must specify what "
            "type of issue this bug report is concerning. You can choose between it being a:\n\n"
            "Website Issue\nProgram Issue\n\n...or both.",
        )
        return

    reports = window.database.reports
    account_name = window.account_name

    active_reports = check_open_reports(account_name, reports)

    if active_reports >= 5:
        warning = QtWidgets.QMessageBox()
        warning.warning(
            window,
            "Maximum Reports Reached",
            "You are already at the maximum amount of active bug reports (5).\n\nPlease wait "
            "until 1 or more of your currently open reports are completed/closed.",
        )
        return

    encoded_image = action_manager.process_screenshot(window)

    if encoded_image is not None:
        upload_report(
            window,
            account_name,
            issue_type,
            encoded_image,
        )
    else:
        return


def upload_report(window, account_name, issue_type, encoded_image):
    """
    Uploads the generated report to MongoDB.

    :param window: The QMainWindow in use.
    :param account_name: The account name of the uploader.
    :param issue_type: The report's issue type.
    :param encoded_image: The image to upload, which is either 0 or encoded in base64.
    :return: A successful report upload.
    """

    reports = window.database.reports
    accounts = window.database.accounts
    account = accounts.find_one({"account_name": account_name})
    employee_type = account["employee_type"]
    data = window.report_view.toPlainText()

    reports.insert(
        {
            "account_name": account_name,
            "employee_type": employee_type,
            "issue_type": issue_type,
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

    open_reports = check_open_reports(account_name, reports)
    remaining_reports = str(open_reports) + "/5 open bug reports."

    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Success")
    msg.setText("Report successfully generated.\n\nYou now have " + remaining_reports)
    msg.exec_()


def check_open_reports(account_name, reports):
    """
    Checks the remaining number of reports an account has.
    :param account_name: The account name of the submitter.
    :param reports: The reports collection to count against.
    :return: A string with the calculated reports filed / reports max.
    """

    matched_reports = reports.find({"account_name": account_name})
    report_count = matched_reports.count()

    return report_count


def update_reports_filed(window, account_name, reports):
    """
    Updates the number of an account's reports filed by 1.

    :param window: The QMainWindow in use.
    :param account_name: The account name to update the amount of reports they have filed.
    :param reports: The list of reports to count against when updating.
    :return: An increase of 1 to an account's report's filed.
    """

    accounts = window.database.accounts

    report_count = check_open_reports(account_name, reports)

    accounts.update(
        {"account_name": account_name}, {"$set": {"reports_filed": report_count}}
    )

    print(report_count)
