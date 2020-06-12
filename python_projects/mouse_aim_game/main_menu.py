""" Handles the main menu of the game. """

import ui_element
import settings

uielement = ui_element.UIElement(
    center_position=(settings.game_width / 2, settings.game_height / 2),
    font_size=50,
    bg_rgb=None,
    text_rgb=settings.WHITE,
    text="CLICK TO START",
)
