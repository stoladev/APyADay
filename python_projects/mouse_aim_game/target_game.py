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
    mouse_state = None
    target = Target()

    while playing_target_game:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                playing_target_game = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_state = "DOWN"

        screen.fill((settings.MAIN_BG_COLOR))
        target.draw(screen)
        target.handle_input(mouse_state)
        mouse_state = None

        pygame.display.flip()
        clock.tick(60)


class Target(Sprite):
    """All actions regarding the target in the game are handled here.
    """

    def __init__(self):
        """ The constructor of the class. """

        target_x_pos = random.randint(100, game_width - 100)
        target_y_pos = random.randint(100, game_height - 100)
        target_position = (target_x_pos, target_y_pos)

        self.images = [target_img.convert_alpha()]
        self.rects = [self.images[0].get_rect(center=target_position)]

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

    def handle_input(self, mouse_state):
        """Handles all input from the keyboard and mouse.

        Args:
            mouse_state: Checks if the mouse has been pressed.
        """

        mouse_pos = pygame.mouse.get_pos()
        mouse_on_target = self.rect.collidepoint(mouse_pos)
        target_clicked = mouse_state == "DOWN"

        if mouse_on_target and target_clicked:
            self.update()
            print("boob")

    def update(self):
        """
        Updates the sprite's position.
        """
        new_x_pos = random.randint(100, game_width - 100)
        new_y_pos = random.randint(100, game_height - 100)
        new_position = (new_x_pos, new_y_pos)

        self.images = [target_img.convert_alpha()]
        self.rects = [self.images[0].get_rect(center=new_position)]

        self.draw(screen)

    def draw(self, surface):
        """
        Draws the target alongside a hitbox generated through rect.
        """

        surface.blit(self.image, self.rect)
