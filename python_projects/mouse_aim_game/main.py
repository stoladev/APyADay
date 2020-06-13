"""
Game concept: mouse aim practice game. Created with Pygame.
"""

# TODO Fix the target reloading on click
# TODO Create seperate todo list file for the game
# TODO Create seperate input_handler class
# TODO Transfer Target into Sprite group
# TODO Countdown timer to main game (3... 2... 1... GO!)
# TODO Leaderboard during countdown
# TODO Random target spawning

import pygame

import main_menu
import settings

pygame.init()
settings.init()

main_menu.init()

pygame.quit()
