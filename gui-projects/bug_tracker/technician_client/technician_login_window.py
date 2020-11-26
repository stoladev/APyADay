# TODO
# Simplify MongoDB load and make it more secure.
from PyQt5.QtWidgets import (
    QDialog,
)

from technician_client.modules.managers import verification_manager


class TechnicianLoginWindow(QDialog):
    def __init__(self):
        super().__init__()

    def verify_technician(self):
        verification_manager.verify_technician(self)
