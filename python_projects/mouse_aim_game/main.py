"""
Game concept: mouse aim practice game. Created with Pygame.
"""

# Fix ui_element load of fonts
# TODO Start screen with a start button
# TODO Countdown timer to main game (3... 2... 1... GO!)
# TODO Leaderboard during countdown
# TODO Random target spawning

import pygame
from target import Target
import main_menu
import settings

# First, you must initialize pygame
pygame.init()

# General Settings
IS_RUNNING = True
title = pygame.display.set_caption('Mouse Aim Practice')
screen = pygame.display.set_mode((settings.game_width, settings.game_height))
target = Target()
clock = pygame.time.Clock()

# Mouse Cursor (Crosshair)
size = (8, 8)
hotspot = (4, 4)
xormasks = (24, 24, 24, 231, 231, 24, 24, 24)
andmasks = (0, 0, 0, 0, 0, 0, 0, 0)
pygame.mouse.set_cursor(size, hotspot, xormasks, andmasks)

while IS_RUNNING:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            IS_RUNNING = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            target.handle_input(mouse_state="DOWN")

    screen.fill((settings.MAIN_BG_COLOR))
    main_menu.uielement.update(pygame.mouse.get_pos())
    main_menu.uielement.draw(screen)

    # if playing_game:
    #     target.draw(screen)

    pygame.display.update()

    # FPS
    clock.tick(60)
