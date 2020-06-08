"""
Game concept: mouse aim practice game. Created with Pygame.
"""

# TODO Create sprite class for Target
# TODO Update blit location
# TODO Add blit "explosion" on click using 3 additional blits
# TODO Update "explosion" blit twice (3 phases) and remove 3rd phase
# TODO Start screen with a start button
# TODO Countdown timer to main game (3... 2... 1... GO!)
# TODO Leaderboard during countdown
# TODO Random target spawning

import random
import pygame

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
TARGET_WIDTH = (game_width * 0.45)
TARGET_HEIGHT = (game_height * 0.8)
# Game Overall


def x_y_generator():
    """
    Generates x and y coordinates for new location of the target.
    """


def target(width, height):
    """
    Draws the target on the main screen.
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    x_pos = random.randint(50, 1750)
    y_pos = random.randint(300, 800)
    screen.blit(target_img, (x_pos, y_pos))
    pygame.display.flip()
    print('Loaded')
    if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
        if click[0] == 1:
            print('Img clicked')


def main():
    """
    Main game function. Holds all essential gameplay pieces.
    """
    is_running = True
    target_up = True
    while is_running:
        # Captures all events that happen within the game
        for event in pygame.event.get():
            # Exits the game if the player quits
            if event.type == pygame.QUIT:
                is_running = False

        screen.fill((153, 153, 153))
        screen.blit(crosshair, (pygame.mouse.get_pos()))
        if target_up:
            target(TARGET_WIDTH, TARGET_HEIGHT)
            target_up = False
            # target_up = False
        pygame.display.update()
        # Fills screen with a color
        # pygame.display.update()

        # if not target(TARGET_WIDTH, TARGET_HEIGHT):
        #     pygame.display.update()
        #     target_up = False

    # Start button for opening game screen
    # start_button = pygame.Rect(0, 250, 200, 50)


main()
pygame.quit()
