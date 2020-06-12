"""Creates user interface elements such as buttons."""

import pygame
from pygame.sprite import Sprite
import pygame.freetype


def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Creates an image-like object with text. """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class UIElement(Sprite):
    """ Adds UI elements such as buttons and general text. """
    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb):
        """
        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            bg_rgb (background colour) - tuple (r, g, b)
            text_rgb (text colour) - tuple (r, g, b)
        """
        self.mouse_over = False  # indicates if the mouse over the element

        # create the default image
        default_image = create_surface_with_text(text=text,
                                                 font_size=font_size,
                                                 text_rgb=text_rgb,
                                                 bg_rgb=bg_rgb)

        # create the image that shows when mouse is over the element
        highlighted_image = create_surface_with_text(text=text,
                                                     font_size=font_size * 1.2,
                                                     text_rgb=text_rgb,
                                                     bg_rgb=bg_rgb)

        # add both images and their rects to lists
        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        # calls the init method of the parent sprite class
        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)
