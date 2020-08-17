""" Handles the main menu of the game. """

import settings
import ui_element

GAME_WIDTH = settings.game_width
GAME_HEIGHT = settings.game_height


def menu():
    """Loads all UI elements.
    """

    start_button_x_pos = GAME_WIDTH / 2
    start_button_y_pos = GAME_HEIGHT / 2.5

    # START BUTTON
    start_button = ui_element.UIElement(
        center_position=(start_button_x_pos, start_button_y_pos),
        font_size=50,
        text_rgb=settings.WHITE,
        text="CLICK TO START",
    )

    credits_button_x_pos = GAME_WIDTH / 2
    credits_button_y_pos = GAME_HEIGHT / 1.5

    # CREDITS BUTTON
    credits_button = ui_element.UIElement(
        center_position=(credits_button_x_pos, credits_button_y_pos),
        font_size=20,
        text_rgb=settings.WHITE,
        text="CREDITS",
    )

    settings_button_x_pos = GAME_WIDTH / 2
    settings_button_y_pos = GAME_HEIGHT / 1.45

    # SETTINGS BUTTON
    settings_button = ui_element.UIElement(
        center_position=(settings_button_x_pos, settings_button_y_pos),
        font_size=20,
        text_rgb=settings.WHITE,
        text="SETTINGS",
    )

    if start_button.update():
        # settings.IN_MAIN_MENU = False
        return "START TARGET GAME"

    if credits_button.update():
        # settings.IN_MAIN_MENU = False
        return "SHOW CREDITS"

    if settings_button.update():
        # settings.IN_MAIN_MENU = False
        return "SHOW SETTINGS"

    return False
