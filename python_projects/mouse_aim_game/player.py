""" Handles the player model and all of its actions. """

import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    """
    Handles all of the player's data, including but not limited to its
    location, health, size, bank, and items.
    """

    walking_up = False
    walking_down = False
    walking_left = False
    walking_right = False

    def __init__(self):

        Sprite.__init__(self)

        self.image = pygame.image.load("./img/player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = 50, 50

    def update(self):
        """
        Updates the Player sprite.
        """

        # MOVEMENT
        if self.walking_up:
            self.rect.y -= 5
        if self.walking_down:
            self.rect.y += 5
        if self.walking_left:
            self.rect.x -= 5
        if self.walking_right:
            self.rect.x += 5
