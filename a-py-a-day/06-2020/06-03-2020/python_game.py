"""
Game concept: mouse aim practice game. Created with Pygame.
"""
# TODO Start screen with a start button
# TODO Countdown timer to main game (3... 2... 1... GO!)
# TODO Leaderboard during countdown

import pygame

# First, you must initialize pygame
pygame.init()

# Sets screen size
game_width, game_height = (800, 600)
screen = pygame.display.set_mode((game_width, game_height))
title = pygame.display.set_caption('Mouse Aim Practice')


def main():
    """
    Main game function. Holds all essential gameplay pieces.
    """
    # Start button for opening game screen
    # start_button = pygame.Rect(0, 250, 200, 50)


main()
pygame.quit()
