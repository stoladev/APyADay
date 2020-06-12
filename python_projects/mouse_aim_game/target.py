""" Handles all target related actions. """

import random
import pygame

target_img = pygame.image.load('./img/target.png')
game_width, game_height = (1800, 900)


class Target():
    """All actions regarding the target in the game are handled here.
    """
    def __init__(self):
        """ The constructor of the class. """

        self.image = target_img.convert_alpha()
        self.rect = self.image.get_rect()

    def handle_input(self, mouse_state):
        """Handles all input from the keyboard and mouse.

        Args:
            mouse_state: Checks if the mouse has been pressed.
        """

        # General settings
        mouse = pygame.mouse.get_pos()

        # Creates new positions
        new_x_pos = random.randint(100, game_width - 100)
        new_y_pos = random.randint(300, game_height - 100)

        # Checks if mouse is on the target
        image_w_check = self.rect.x + self.rect.h > mouse[0] > self.rect.x
        image_h_check = self.rect.y + self.rect.w > mouse[1] > self.rect.y

        if image_w_check and image_h_check:
            if mouse_state == "DOWN":
                self.rect.x = new_x_pos
                self.rect.y = new_y_pos

    def draw(self, surface):
        """ Draws the target alongside a hitbox generated through rect. """

        # Blit at the current position.
        surface.blit(self.image, (self.rect.x, self.rect.y))
