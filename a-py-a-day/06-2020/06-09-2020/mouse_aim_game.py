"""
Game concept: mouse aim practice game. Created with Pygame.
"""

# TODO Start screen with a start button
# TODO Countdown timer to main game (3... 2... 1... GO!)
# TODO Leaderboard during countdown
# TODO Random target spawning

import pygame
from target import Target

# First, you must initialize pygame
pygame.init()

# General Settings
IS_RUNNING = True
game_width, game_height = (1800, 900)
title = pygame.display.set_caption('Mouse Aim Practice')
screen = pygame.display.set_mode((game_width, game_height))
target = Target()
clock = pygame.time.Clock()

# Mouse Cursor (Crosshair)
mouse_size = (8, 8)
mouse_hotspot = (4, 4)
mouse_img = (24, 24, 24, 231, 231, 24, 24, 24)
mouse_andmask = (0, 0, 0, 0, 0, 0, 0, 0)
pygame.mouse.set_cursor(mouse_size, mouse_hotspot, mouse_img, mouse_andmask)

while IS_RUNNING:
    # Captures all events that happen within the game
    for event in pygame.event.get():
        # Exits the game if the player quits
        if event.type == pygame.QUIT:
            IS_RUNNING = False

    target.handle_keys()

    # Draws
    screen.fill((153, 153, 153))
    target.draw(screen)
    pygame.display.update()

    # FPS
    clock.tick(60)
