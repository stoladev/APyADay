""" All settings related to color, sizings, and alike. """
import pygame

# Loops
RUNNING = True
IN_MAIN_MENU = True
PLAYING_TARGET_GAME = False
IN_SETTINGS = False
IN_CREDITS = False
CLICKING = None

# Sizings
game_width, game_height = (1800, 900)
screen = pygame.display.set_mode((game_width, game_height))
title = pygame.display.set_caption("Mouse Aim Practice")

# Colors
MAIN_BG_COLOR = (75, 85, 130)
BLUE = (106, 159, 181)
WHITE = (255, 255, 255)
ALPHA = (0, 255, 0)

# Clock
clock = pygame.time.Clock()

# Animation Cycles
VELOCITY = 1
ANI = 4


def init():
    """
    Initializes settings for the game.
    """
    cursor_init()


def cursor_init():
    """Initializes the crosshair cursor through set_cursor.
    """
    size = (8, 8)
    hotspot = (4, 4)
    xormasks = (24, 24, 24, 231, 231, 24, 24, 24)
    andmasks = (0, 0, 0, 0, 0, 0, 0, 0)
    pygame.mouse.set_cursor(size, hotspot, xormasks, andmasks)
