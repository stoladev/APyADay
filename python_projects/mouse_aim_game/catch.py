""" Catches user's interactions. """

import pygame

import target_game
import settings
import player

PlayerState = player.Player
player = player.Player()
target = target_game.Target()
all_sprites = pygame.sprite.Group()


def catch_events():
    """
    Catches all events that occur during the game.
    """

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            settings.CLICKING = True

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            catch_keypress(event.key)

        if event.type == pygame.KEYUP:
            catch_keyrelease(event.key)

        # elif event.type == pygame.KEYUP:
        #     control.reset()


def catch_keypress(key):
    """
    Catches all keypresses that occur during the game.

    Args:
        key: The key that was pressed.
    """

    if settings.PLAYING_TARGET_GAME:

        # Checks if the mouse has been clicked.

        # Takes you out of the Target Game and puts you into the main menu.
        if key == pygame.K_ESCAPE:
            # Stops the Target Game loop.
            settings.PLAYING_TARGET_GAME = False
            # Puts you into the main menu.
            settings.IN_MAIN_MENU = True

        # MOVEMENT
        # Starts player movement.
        if key == pygame.K_w:
            PlayerState.walking_up = True
        if key == pygame.K_s:
            PlayerState.walking_down = True
        if key == pygame.K_a:
            PlayerState.walking_left = True
        if key == pygame.K_d:
            PlayerState.walking_right = True


def catch_keyrelease(key):
    """
    Catches all key releases that occur during the game.

    Args:
        key: The key that was released.
    """

    if settings.PLAYING_TARGET_GAME:

        # MOVEMENT
        # Stops player movement.
        if key == pygame.K_w:
            PlayerState.walking_up = False
        if key == pygame.K_s:
            PlayerState.walking_down = False
        if key == pygame.K_a:
            PlayerState.walking_left = False
        if key == pygame.K_d:
            PlayerState.walking_right = False
