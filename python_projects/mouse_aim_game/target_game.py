""" Handles all target related actions. """

import random
import pygame
from pygame.sprite import Sprite

import settings

game_width, game_height = (settings.game_width, settings.game_height)
screen = settings.screen


class Target(Sprite):
    """
    Handles the Target, the main point of the game.
    """

    def __init__(self):

        Sprite.__init__(self)

        random_x_pos = random.randint(100, game_width - 100)
        random_y_pos = random.randint(100, game_height - 100)
        self.image = pygame.image.load("./img/target.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random_x_pos, random_y_pos)
