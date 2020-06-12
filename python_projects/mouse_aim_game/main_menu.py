""" Handles the main menu of the game. """

import ui_element
import settings
import pygame

screen = settings.screen


def ui_load():
    """Loads all UI elements.
    """

    start_button = ui_element.UIElement(
        center_position=(settings.game_width / 2, settings.game_height / 2),
        font_size=50,
        bg_rgb=None,
        text_rgb=settings.WHITE,
        text="CLICK TO START",
    )

    screen.fill((settings.MAIN_BG_COLOR))
    start_button.update(pygame.mouse.get_pos())
    start_button.draw(screen)
