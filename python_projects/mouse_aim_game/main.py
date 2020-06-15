"""
Game concept: mouse aim practice game. Created with Pygame.
"""

import random
import pygame

import settings
import main_menu
import target_game
import player


# Initializes pygame engine and general settings.
pygame.init()
settings.init()


RUNNING = True
IN_MAIN_MENU = True
PLAYING_TARGET_GAME = False
IN_SETTINGS = False
IN_CREDITS = False

bg = settings.MAIN_BG_COLOR
screen = settings.screen
clock = settings.clock

target = target_game.Target()
player = player.Player()
all_sprites = pygame.sprite.Group()


def catch_events():

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            catch_keypress(event.key)

        # elif event.type == pygame.KEYUP:
        #     control.reset()


def catch_keypress(key):

    if PLAYING_TARGET_GAME:

        mouse_pos = pygame.mouse.get_pos()
        ON_TARGET = target.rect.collidepoint(mouse_pos)

        # Checks if the mouse has been clicked.
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ON_TARGET:
                target.rect.x = random.randint(100, settings.game_width - 100)
                target.rect.y = random.randint(100, settings.game_height - 100)

        if key == pygame.K_ESCAPE:
            # Removes the Target sprite.
            all_sprites.remove(target)
            # Stops the Target Game loop.
            PLAYING_TARGET_GAME = False
            # Puts you into the main menu.
            IN_MAIN_MENU = True


while RUNNING:

    # Resets the game screen per frame to prevent sprite ghosting.
    screen.fill(bg)
    # Resets the click state per frame to prevents click-lag.
    CLICKING = False
    # Draws all the sprites that are in the default group.
    all_sprites.draw(screen)
    # Updates all the sprites that are in the default group.
    all_sprites.update()

    if IN_MAIN_MENU:

        # Switches to appropriate state when UI Element is clicked.
        ui_element_clicked = main_menu.menu()
        if ui_element_clicked == "START TARGET GAME":
            PLAYING_TARGET_GAME = True
        elif ui_element_clicked == "SHOW SETTINGS":
            IN_SETTINGS = True
        elif ui_element_clicked == "SHOW CREDITS":
            IN_CREDITS = True

    if PLAYING_TARGET_GAME:

        # Disables the main menu.
        IN_MAIN_MENU = False
        # Adds the Target sprite to the default group.
        all_sprites.add(player)
        all_sprites.add(target)

    # Updates the display.
    catch_events()
    pygame.display.update()
    # Framerate/refresh rate.
    clock.tick(60)


# Quits game if all else stops running.
pygame.quit()
