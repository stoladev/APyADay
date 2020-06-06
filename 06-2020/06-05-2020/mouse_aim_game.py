"""
Game concept: mouse aim practice game. Created with Pygame.
"""

# TODO Start screen with a start button
# TODO Countdown timer to main game (3... 2... 1... GO!)
# TODO Leaderboard during countdown
# TODO Random target spawning

import pygame
import random

# First, you must initialize pygame
pygame.init()

# Size
game_width, game_height = (1800, 900)
screen = pygame.display.set_mode((game_width, game_height))
# Title
title = pygame.display.set_caption('Mouse Aim Practice')
# Icon
icon = pygame.image.load('target.png')
pygame.display.set_icon(icon)
# Cursor
pygame.mouse.set_visible(False)
crosshair = pygame.image.load('crosshair.png').convert_alpha()
# Target
target_img = icon
TARGET_X = (game_width * 0.45)
TARGET_Y = (game_height * 0.8)
# Game Overall
RUNNING = True


def target(x_pos, y_pos, width, height):
    """
    Target draw on main screen.
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    screen.blit(target_img, (int(x_pos), int(y_pos)))

    if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
        if click[0] == 1:
            print("On hover")


while RUNNING:
    # Captures all events that happen within the game
    for event in pygame.event.get():
        # Exits the game if the player quits
        if event.type == pygame.QUIT:
            RUNNING = False

    # Fills screen with a color
    screen.fill((153, 153, 153))
    target(100, 100, 50, 50)
    screen.blit(crosshair, (pygame.mouse.get_pos()))
    pygame.display.update()


def main():
    """
    Main game function. Holds all essential gameplay pieces.
    """
    # Start button for opening game screen
    # start_button = pygame.Rect(0, 250, 200, 50)


main()
pygame.quit()
