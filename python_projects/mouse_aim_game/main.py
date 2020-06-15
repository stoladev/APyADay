"""
Game concept: mouse aim practice game. Created with Pygame.
"""

import pygame

import settings
import catch
import main_menu
import player
import target_game


# Initializes pygame engine and general settings.
pygame.init()
settings.init()


clock = settings.clock
bg = settings.MAIN_BG_COLOR
screen = settings.screen

target = target_game.Target()
player = player.Player()
all_sprites = pygame.sprite.Group()


while settings.RUNNING:

    # Resets the game screen per frame to prevent sprite ghosting.
    screen.fill(bg)

    # Catches user's inputs.
    catch.catch_events()

    if settings.IN_MAIN_MENU:

        # Switches to appropriate state when UI Element is clicked.
        ui_element_clicked = main_menu.menu()
        if ui_element_clicked == "START TARGET GAME":
            settings.PLAYING_TARGET_GAME = True
        elif ui_element_clicked == "SHOW SETTINGS":
            settings.IN_SETTINGS = True
        elif ui_element_clicked == "SHOW CREDITS":
            settings.IN_CREDITS = True

    if settings.PLAYING_TARGET_GAME:

        # De-loads the main menu.
        settings.IN_MAIN_MENU = False
        # Adds the Player sprite to the default group.
        all_sprites.add(target)
        # Adds the Target sprite to the default group.
        all_sprites.add(player)

    # UPDATES
    # Checks if any sprites need to be updated.
    all_sprites.update()
    # Draws/all the sprites that are in the default group.
    all_sprites.draw(screen)
    # Updates the game's display.
    pygame.display.update()

    # RESETS
    # Empties all sprites loaded by loops that are no longer running.
    all_sprites.empty()
    # Resets the click state per frame to prevents click-lag.
    # Must be reset outside of event check.
    settings.CLICKING = False

    # REFRESH RATE
    clock.tick(60)

# Quits game if all else stops running.
pygame.quit()
