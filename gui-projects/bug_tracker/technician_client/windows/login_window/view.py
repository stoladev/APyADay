"""
The View handler for the technician's login verification window.
"""

# pylint: disable=import-error
# Reason: Importing is working fine, but pylint begs to differ. Most likely because of venv.

# pylint: disable=too-few-public-methods
# Reason: Using MVC framework. Further securing of the login verification method through MongoDB
# will inevitably create more use for this View class and additional methods.

from PyQt5 import QtWidgets

from technician_client.modules.managers import verification_manager


class View:
    """
    Handles the view updates depending on model calculations for the verification window.
    """

    def __init__(self, root, model):
        super().__init__()

        self.model = model
        self.root = root

        root.setWindowTitle("Technician Login")

        # Initializations
        root.technician_login_line = QtWidgets.QLineEdit(root)
        root.technician_password_line = QtWidgets.QLineEdit(root)
        root.technician_login_button = QtWidgets.QPushButton(root)
        root.technician_label = QtWidgets.QLabel(root)

        # Text Lines
        root.technician_login_line.setPlaceholderText("Username/Email Address")
        root.technician_password_line.setPlaceholderText("Password")
        root.technician_password_line.setEchoMode(QtWidgets.QLineEdit.Password)

        # Buttons
        root.technician_login_button.setText("Login")
        root.technician_login_button.clicked.connect(self.verify_technician)

        # Layout
        layout = QtWidgets.QVBoxLayout(root)
        layout.addWidget(root.technician_login_line)
        layout.addWidget(root.technician_password_line)
        layout.addWidget(root.technician_login_button)

        root.show()

    def verify_technician(self):
        """
        Verifies the username and password using the verification manager.
        """

        verification_manager.verify_technician(self)
