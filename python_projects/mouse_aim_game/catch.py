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

        # Checks if the mouse button has been pressed.
        if event.type == pygame.MOUSEBUTTONDOWN:
            settings.CLICKING = True

        # Checks if a key has been pressed.
        if event.type == pygame.KEYDOWN:

            # WHILE IN THE MAIN MENU
            if settings.IN_MAIN_MENU:

                if event.key == pygame.K_RETURN:
                    settings.PLAYING_TARGET_GAME = True

            # WHILE PLAYING TARGET GAME
            if settings.PLAYING_TARGET_GAME:

                # Takes out of Target Game and puts in Main Menu.
                if event.key == pygame.K_ESCAPE:
                    # Stops the Target Game loop.
                    settings.PLAYING_TARGET_GAME = False
                    # Puts you into the main menu.
                    settings.IN_MAIN_MENU = True

                # MOVEMENT
                # Starts player movement.
                if event.key == pygame.K_LEFT or event.key == ord("a"):
                    PlayerState.walking_left = True
                if event.key == pygame.K_RIGHT or event.key == ord("d"):
                    PlayerState.walking_right = True

        # Checks if a key has been released.
        if event.type == pygame.KEYUP:

            if settings.PLAYING_TARGET_GAME:

                # MOVEMENT
                # Stops player movement.
                if event.key == pygame.K_LEFT or event.key == ord("a"):
                    PlayerState.walking_left = False
                if event.key == pygame.K_RIGHT or event.key == ord("d"):
                    PlayerState.walking_right = False

        # Checks if the game has been exited.
        if event.type == pygame.QUIT:
            pygame.quit()
