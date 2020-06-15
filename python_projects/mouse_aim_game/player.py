""" Handles the player model and all of its actions. """

import pygame
from pygame.sprite import Sprite

# all_sprites = pygame.sprite.Group()


class Player(Sprite):
    """
    Handles all of the player's data, including but not limited to its
    location, health, size, bank, and items.
    """

    def __init__(self):

        Sprite.__init__(self)

        self.image = pygame.image.load("./img/player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = 500, 500

    # def update(self):

