"""Creates user interface elements such as buttons."""

import pygame
from pygame.sprite import Sprite
import pygame.freetype

import settings

screen = settings.screen


def create_text(text, font_size, text_rgb):
    """
    Creates an image-like object with text.
    """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb)
    return surface.convert_alpha()


class UIElement(Sprite):
    """
    Adds UI elements such as buttons and general text.

    __init__ Args:
            center_position: (x, y) of where to place element.
            text: what the element says.
            font_size: text size.
            text_rgb: text color in rgb.

    """

    def __init__(self, center_position, text, font_size, text_rgb):

        self.mouse_over = False  # indicates if the mouse over the element

        # create the default image
        default_image = create_text(text, font_size, text_rgb)
        default_image_rect = default_image.get_rect(center=center_position)

        # create the image that shows when mouse is over the element
        hovered_image = create_text(text, font_size * 1.5, text_rgb)
        hovered_image_rect = hovered_image.get_rect(center=center_position)

        # add both images and their rects to lists
        self.images = [default_image, hovered_image]
        self.rects = [default_image_rect, hovered_image_rect]

        # calls the init method of the parent sprite class
        super().__init__()

    def update(self):
        """
        Updates the UI element sprite.

        Args:
            clicking: checks if mouse is being clicked.
        """
        mouse_pos = pygame.mouse.get_pos()
        mouse_on_element = self.rect.collidepoint(mouse_pos)

        if mouse_on_element:
            self.mouse_over = True
            screen.blit(self.image, self.rect)

            if self.clicked:
                return True

        else:
            screen.blit(self.image, self.rect)
            return False

        return False

    def clicked(self, clicked):
        """
        Checks if the UI Element has been clicked.
        """
        if clicked:
            return True

        return False

    @property
    def image(self):
        """
        Handles the element's sprite size, changing if mouse is hovered over
        it.
        """
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        """
        Handles the element's rect size, changing if mouse is hovered over it.
        """
        return self.rects[1] if self.mouse_over else self.rects[0]

