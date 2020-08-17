""" Handles the player model and all of its actions. """

import os
import pygame
from pygame.sprite import Sprite

import settings

ANI = 4
ALPHA = settings.ALPHA


class Player(Sprite):
    """
    Handles all of the player's data, including but not limited to its
    location, health, size, bank, and items.
    """

    velocity = 3
    walking_up = False
    walking_down = False
    walking_left = False
    walking_right = False

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("./img/player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = 50, 50

    def update(self):
        """
        Updates the Player sprite.
        """

        # MOVEMENT
        if self.walking_up:
            # if self.velocity <= 3:
            #     self.velocity += 1
            self.rect.y -= 1 * self.velocity

        if self.walking_down:
            # if self.velocity <= 3:
            #     self.velocity += 1
            self.rect.y += 1 * self.velocity

        if self.walking_left:
            # if self.velocity <= 3:
            #     self.velocity += 1
            self.rect.x -= 1 * self.velocity

        if self.walking_right:
            # if self.velocity <= 3:
            #     self.velocity += 1
            self.rect.x += 1 * self.velocity
