"""
Handles all actions that do specific operations for checking, generating, updating, or similar.
"""

import base64
import os
import tempfile

from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets


def load_screenshot(window, encoded_image):
    """
    Loads the screenshot from the selected report.

    :param window: The QMainWindow in use.
    :param encoded_image: The base64 encoded image to decode and open in the preview.
    :return: A loaded screenshot for the screenshot viewer (QGraphicsView).
    """

    scene = decode_screenshot(window, encoded_image)

    window.screenshot_view.setScene(scene)
    window.screenshot_view.ensureVisible(scene.sceneRect())
    window.screenshot_view.fitInView(scene.sceneRect(), mode=QtCore.Qt.KeepAspectRatio)


def decode_screenshot(window, encoded_image):
    """
    Decodes the screenshot from base64 to a temporary .png.
    :param window: The QMainWindow in use.
    :param encoded_image: The base64 encoded image to decode for the preview window.
    :return: A compiled scene for use in the screenshot viewer.
    """

    window.screenshot_path = tempfile.NamedTemporaryFile(
        suffix=".png", prefix=os.path.basename(__file__), delete=True
    ).name

    base64_to_png(window.screenshot_path, encoded_image)

    pixmap = QtGui.QPixmap(window.screenshot_path)
    item = QtWidgets.QGraphicsPixmapItem(pixmap)
    scene = QtWidgets.QGraphicsScene(window)
    scene.addItem(item)

    return scene


def base64_to_png(screenshot_path, encoded_image):
    """
    Converts base64 data to a PNG file.

    :param screenshot_path: The path of the temporary screenshot png.
    :param encoded_image: The base64 data to convert.
    :return: A written image.
    """

    with open(screenshot_path, "wb") as image_file:
        return image_file.write(base64.decodebytes(encoded_image))


def open_large_viewer(window):
    screenshot_path = window.screenshot_path
    image = Image.open(screenshot_path, mode="r")
    image.show()
    print("Image opened.")
