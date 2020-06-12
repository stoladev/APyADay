""" Handles the main menu of the game. """

import pygame

import ui_element
import settings

screen = settings.screen


def main_menu_ui_load():
    """Loads all UI elements.
    """

    start_button_x_pos = settings.game_width / 2
    start_button_y_pos = settings.game_height / 2.5

    start_button = ui_element.UIElement(
        center_position=(start_button_x_pos, start_button_y_pos),
        font_size=50,
        text_rgb=settings.WHITE,
        text="CLICK TO START",
    )

    credits_button_x_pos = settings.game_width / 2
    credits_button_y_pos = start_button_y_pos * 2

    credits_button = ui_element.UIElement(
        center_position=(credits_button_x_pos, credits_button_y_pos),
        font_size=20,
        text_rgb=settings.WHITE,
        text="CREDITS",
    )

    settings_button_x_pos = settings.game_width / 2
    settings_button_y_pos = credits_button_y_pos / 0.9

    settings_button = ui_element.UIElement(
        center_position=(settings_button_x_pos, settings_button_y_pos),
        font_size=20,
        text_rgb=settings.WHITE,
        text="SETTINGS",
    )

    screen.fill((settings.MAIN_BG_COLOR))
    start_button.ui_hover_check(pygame.mouse.get_pos())
    credits_button.ui_hover_check(pygame.mouse.get_pos())
    settings_button.ui_hover_check(pygame.mouse.get_pos())
    start_button.draw(screen)
    credits_button.draw(screen)
    settings_button.draw(screen)
