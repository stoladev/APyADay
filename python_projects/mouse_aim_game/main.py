"""
Game concept: mouse aim practice game. Created with Pygame.
"""

# TODO Create seperate todo list file for the game
# TODO Create seperate input_handler class
# TODO Transfer Target into Sprite group
# TODO Countdown timer to main game (3... 2... 1... GO!)
# TODO Leaderboard during countdown
# TODO Random target spawning

import pygame

import target
import main_menu
import settings

pygame.init()
settings.cursor_init()

IS_RUNNING = True
title = pygame.display.set_caption("Mouse Aim Practice")
target = target.Target()
clock = pygame.time.Clock()
screen = settings.screen

while IS_RUNNING:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            IS_RUNNING = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            target.handle_input(mouse_state="DOWN")

    main_menu.main_menu_ui_load()

    # if playing_game:
    # target.draw(screen)

    pygame.display.update()

    # FPS
    clock.tick(60)

pygame.quit()
