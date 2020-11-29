"""
The data model used for the technician's login verification window.
"""


# pylint: disable=too-few-public-methods
# Reason: Using MVC framework. Further securing of the login verification method through MongoDB
# will inevitably create more use for this Model class and additional methods.


class Model:
    """
    Handles all data manipulations for the technician's login verification window.
    """

    def __init__(self, root, database):
        self.root = root
        self.database = database
