""" Handles all target related actions. """

import random
import pygame
from pygame.sprite import Sprite

import settings

target_img = pygame.image.load("./img/target.png")
game_width, game_height = (1800, 900)
screen = settings.screen
clock = settings.clock


def init():
    """
    Begins the Target game.
    """
    playing_target_game = True
    target_x_pos = random.randint(100, game_width - 100)
    target_y_pos = random.randint(100, game_height - 100)
    target_position = (target_x_pos, target_y_pos)
    mouse_pos = pygame.mouse.get_pos()
    mouse_state = None
    target = Target(target_position)

    while playing_target_game:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                playing_target_game = False

            if target.rect.collidepoint(mouse_pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    playing_target_game = False
                # mouse_state = "DOWN"

        target.handle_input(mouse_pos, mouse_state)
        target.draw(screen)
        mouse_state = None

        pygame.display.update()
        clock.tick(60)


class Target(Sprite):
    """All actions regarding the target in the game are handled here.
    """

    def __init__(self, center_position):
        """ The constructor of the class. """

        self.images = [target_img.convert_alpha()]
        self.rects = [self.images[0].get_rect(center=center_position)]

        super().__init__()

    @property
    def image(self):
        """
        Handles the element's sprite size, changing if mouse is hovered over
        it.
        """
        return self.images[0]

    @property
    def rect(self):
        """
        Handles the element's rect size, changing if mouse is hovered over it.
        """
        return self.rects[0]

    def handle_input(self, mouse_pos, mouse_state):
        """Handles all input from the keyboard and mouse.

        Args:
            mouse_state: Checks if the mouse has been pressed.
        """

        if self.rect.collidepoint(mouse_pos):
            print("test")
            if mouse_state == "DOWN":
                print("test")

            else:
                print("noooope")

    def draw(self, surface):
        """
        Draws the target alongside a hitbox generated through rect.
        """

        surface.blit(self.image, self.rect)
