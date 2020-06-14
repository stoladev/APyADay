"""Creates user interface elements such as buttons."""

import pygame
from pygame.sprite import Sprite
import pygame.freetype

import target_game


def create_text_bg(text, font_size, text_rgb):
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
        """
        Adds UI elements such as buttons and general text.

        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            text_rgb (text colour) - tuple (r, g, b)
        """

        self.mouse_over = False  # indicates if the mouse over the element

        # create the default image
        default_image = create_text_bg(
            text=text, font_size=font_size, text_rgb=text_rgb
        )

        # create the image that shows when mouse is over the element
        highlighted_image = create_text_bg(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb
        )

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

    def ui_interactions(self, mouse_pos, mouse_state):
        """
        Updates the UI element sprite.

        Args:
            mouse_pos: mouse position is used for update state.
        """

        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_state == "DOWN":
                # print(self.rect.topleft)
                # print(self.rect.bottomright)
                # print(mouse_pos)
                target_game.init()

        else:
            self.mouse_over = False

    def draw(self, surface):
        """
        Draws element onto a surface
        """
        surface.blit(self.image, self.rect)
