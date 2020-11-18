"""
Initializes window widgets for the employee application. Points to and runs customizations and
specifications of execution/registered events.
"""

# pylint: disable=import-error
# Reason: Importing is working fine, but pylint begs to differ. Most likely because of venv.

# pylint: disable=too-many-instance-attributes
# Reason: All these instances are necessary for the QMainWindow, since there is only 1.

import os
import tempfile

import pymongo
from PyQt5.QtWidgets import (
    QCheckBox,
    QGraphicsView,
    QGridLayout,
    QLabel,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QTextBrowser,
    QTextEdit,
    QWidget,
)

from employee_client.modules.loaders import widget_loader
from employee_client.modules.managers import action_manager, report_manager


class EmployeeMainWindow(QMainWindow):
    """
    Handles the initiation of the main employee window, along with calling any setup
    configurations and/or event updates.
    """

    def __init__(self, account_name):
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

        # TEMPORARY PNG FILE
        self.screenshot_path = tempfile.NamedTemporaryFile(
            suffix=".png", prefix=os.path.basename(__file__), delete=True
        ).name

        # MongoDB Connection
        mongodb_url = open("../mongo_cluster.txt", "r")
        connection = mongodb_url.read()
        cluster = pymongo.MongoClient(connection)
        self.database = cluster["bug_tracker_db"]

        # General activations
        widget_loader.load_all_widgets(self)
        self.account_name = account_name
        self.update_preview()

    def size_policy_setup(self):
        """
        Sets up the sizing policy for general options.
        """
        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)

    def generate_report(self):
        """
        Hands of the report generation to the report manager.
        """
        report_manager.generate_report(self)

    def take_screenshot(self):
        """
        Hands of taking the screenshot to the action manager.
        """
        action_manager.take_screenshot(self)

    def update_preview(self):
        """
        Hands off updating the preview for the report to the action manager.
        """
        action_manager.update_preview(self)

    def check_issue_type(self):
        """
        Hands off checking the issue type to the action manager.
        """
        action_manager.check_issue_type(self)
