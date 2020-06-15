""" Handles the main menu of the game. """

import settings
import ui_element


def menu():
    """Loads all UI elements.
    """

    start_button_x_pos = settings.game_width / 2
    start_button_y_pos = settings.game_height / 2.5

    # START BUTTON
    start_button = ui_element.UIElement(
        center_position=(start_button_x_pos, start_button_y_pos),
        font_size=50,
        text_rgb=settings.WHITE,
        text="CLICK TO START",
    )

    credits_button_x_pos = settings.game_width / 2
    credits_button_y_pos = start_button_y_pos * 2

    # CREDITS BUTTON
    credits_button = ui_element.UIElement(
        center_position=(credits_button_x_pos, credits_button_y_pos),
        font_size=20,
        text_rgb=settings.WHITE,
        text="CREDITS",
    )

    settings_button_x_pos = settings.game_width / 2
    settings_button_y_pos = credits_button_y_pos * 1.03

    # SETTINGS BUTTON
    settings_button = ui_element.UIElement(
        center_position=(settings_button_x_pos, settings_button_y_pos),
        font_size=20,
        text_rgb=settings.WHITE,
        text="SETTINGS",
    )

    if start_button.update():
        return "START TARGET GAME"

    if credits_button.update():
        return "SHOW CREDITS"

    if settings_button.update():
        return "SHOW SETTINGS"

    return False
