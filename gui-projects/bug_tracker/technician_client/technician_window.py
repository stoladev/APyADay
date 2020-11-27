"""
Initializes window widgets for the technician application. Points to and runs customizations and
specifications of execution/registered events.
"""

# pylint: disable=import-error
# Reason: Importing is working fine, but pylint begs to differ. Most likely because of venv.

# pylint: disable=too-many-instance-attributes
# Reason: This number of attributes is necessary because of the scope of the application.

# pylint: disable=invalid-name
# Reason: The 2 invalid names are overrides.

# pylint: disable=too-many-statements
# Reason: This number of statements is necessary because of the scope of the application.

import PyQt5.QtWidgets
import pymongo


class TechnicianMainWindow(PyQt5.QtWidgets.QMainWindow):
    """
    Handles the initiation of the main technician window, along with calling any setup
    configurations and/or event updates.
    """

    def __init__(self):
        super().__init__()

        # MongoDB Connection
        mongodb_url = open("../mongo_cluster.txt", "r")
        connection = mongodb_url.read()
        cluster = pymongo.MongoClient(connection)
        self.database = cluster["bug_tracker_db"]
