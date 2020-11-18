"""
This is the manager of all report-related functions, ranging from checking what type of issue the
report is, to finalizing and uploading the finished report to the appropriate MongoDB.
"""

from PyQt5 import QtWidgets


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
        upload_report(window)


def upload_report(window):
    """
    Uploads the report, first checking too see if there's a duplicate.

    :param window: The QMainWindow in use.
    :return: An uploaded or replaced report.
    """
    account_name = window.account_name
    data = window.report_view.toPlainText()
    reports = window.database.reports

    reports.insert({"report": data, "account_name": account_name})

    update_reports_filed(window)

    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Success")
    msg.setText("Report successfully generated.")
    msg.exec_()


def update_reports_filed(window):
    """
    Updates the number of an account's reports filed by 1.

    :param window: The QMainWindow in use.

    :return: An increase of 1 to an account's report's filed.
    """
    account_name = window.account_name
    reports = window.database.reports
    accounts = window.database.accounts

    matched_reports = reports.find({"account_name": account_name})
    report_count = matched_reports.count()

    accounts.update(
        {"account_name": account_name}, {"$set": {"reports_filed": report_count}}
    )

    print(report_count)
