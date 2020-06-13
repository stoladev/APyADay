""" Handles the main menu of the game. """

import pygame

import ui_element
import settings

screen = settings.screen


def init():
    """
    Draws the main menu screen.
    """
    in_main_menu = True
    mouse_state = None
    while in_main_menu:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                in_main_menu = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_state = "DOWN"

        ui_elements_load(mouse_state)
        mouse_state = None

        pygame.display.update()
        settings.clock.tick(60)


def ui_elements_load(mouse_state):
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
    settings_button_y_pos = credits_button_y_pos / 0.9

    # SETTINGS BUTTON
    settings_button = ui_element.UIElement(
        center_position=(settings_button_x_pos, settings_button_y_pos),
        font_size=20,
        text_rgb=settings.WHITE,
        text="SETTINGS",
    )

    screen.fill((settings.MAIN_BG_COLOR))

    mouse_pos = pygame.mouse.get_pos()
    start_button.ui_interactions(mouse_pos, mouse_state)
    credits_button.ui_interactions(mouse_pos, mouse_state)
    settings_button.ui_interactions(mouse_pos, mouse_state)

    start_button.draw(screen)
    credits_button.draw(screen)
    settings_button.draw(screen)
