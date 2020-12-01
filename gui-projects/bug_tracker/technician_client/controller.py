"""
The main controller for all technician related actions.
"""

# pylint: disable=import-error
# Reason: Importing is working fine, but pylint begs to differ. Most likely because of venv.

import sys

import pymongo
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from technician_client.windows import login_window, main_window


class Controller:
    """
    The main controller that runs all necessary actions to provide the technician's report center.
    """

    def __init__(self):
        self.database = self.connect_to_database()
        self.main_window = None

        self.login_window = login_window.Controller()
        self.model = login_window.Model(self.login_window, self.database)
        self.view = login_window.View(self.login_window, self.model)

    def run(self):
        """
        Checks for QDialog to be accepted, which then returns the main window of the report center.
        """

        if self.login_window.exec_() == QtWidgets.QDialog.Accepted:
            self.main_window = main_window.Controller()
            self.model = main_window.Model(self.main_window, self.database)
            self.view = main_window.View(self.main_window, self.model)
            sys.exit(app.exec_())

    @staticmethod
    def connect_to_database():
        """
        Connects to the Mongo database, using this cluster for all data pulls/pushes.
        """

        mongodb_url = open("../mongo_cluster.txt", "r")
        connection = mongodb_url.read()
        cluster = pymongo.MongoClient(connection)

        return cluster["bug_tracker_db"]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    controller.run()
