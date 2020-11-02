import pygame
import random
import math


class Target:
    """
    This class is responsible for creating and controlling targets.
    """

    @staticmethod
    def get_xy():
        """Generates a random x, y position as a tuple"""
        xy = (random.randint(64, 1220), random.randint(64, 660))
        return xy

    def __init__(self, name, window, image_dir):
        self.name = name
        self.window = window
        self.image = pygame.image.load(image_dir)
        self.xy = (0, 0)
        self.mouse_click = False
        self.hit_counter = 0
        self.miss_counter = 0

    def draw_target(self, mouse_click, no_targets):
        """
        Draws the target object to the screen and moves it if its been clicked.
        :param mouse_click: True is the mouse has been clicked,
         False otherwise.
        :param no_targets:
        :return: The number of targets display to the screen. Determines how
        the miss counter is calculated.
        """
        self.mouse_click = mouse_click
        image = self.image
        if self.xy == (0, 0):
            self.xy = Target.get_xy()
        else:
            self.window.blit(image, (self.xy[0] - 64, self.xy[1] - 64))
            if Target.is_collide(self) and self.mouse_click:
                self.xy = Target.get_xy()
                self.hit_counter += 1
                self.miss_counter -= 1
            if not Target.is_collide(self) and self.mouse_click:
                self.miss_counter += 1 / no_targets

    def is_collide(self):
        """Checks to see if a target has been clicked by the mouse."""
        mx, my = pygame.mouse.get_pos()
        distance = \
            math.sqrt(((self.xy[0] - mx) ** 2) + ((self.xy[1] - my) ** 2))
        if distance < 65:
            return True
        else:
            return False

    def reset(self):
        """Resets the score of the hit and miss counters."""
        self.hit_counter = 0
        self.miss_counter = 0


class Text:
    """
    This class is responsible for creating and displaying all of the text boxes
    that will be rendered to the screen
    """

    def __init__(self, screen, text, font, x, y, colour,
                 colour_change=None, bg_colour=None):
        self.screen = screen
        self.text = text
        self.font = font
        self.x = x
        self.y = y
        self.colour = colour
        self.colour_change = colour_change
        self.bg_colour = bg_colour

    def display_text(self):
        """
        Displays text to the screen and checks if the mouse is hovering over
        it, if it is, it can change the colour of the text to give a more
        responsive feeling interface.
        """
        if self.colour_change is None:
            text = self.font.render(self.text, True, self.colour,
                                    self.bg_colour)
            text_rect = text.get_rect()
            text_rect.center = (self.x, self.y)
            self.screen.blit(text, text_rect)
        else:
            if Text.mouse_over(self):
                text = self.font.render(self.text, True, self.colour_change,
                                        self.bg_colour)
                text_rect = text.get_rect()
                text_rect.center = (self.x, self.y)
                self.screen.blit(text, text_rect)
            else:
                text = self.font.render(self.text, True, self.colour,
                                        self.bg_colour)
                text_rect = text.get_rect()
                text_rect.center = (self.x, self.y)
                self.screen.blit(text, text_rect)

    def mouse_over(self):
        """Checks if the mouse is hovering over a text object."""
        mx, my = pygame.mouse.get_pos()
        distance = \
            math.sqrt(((self.x - mx) ** 2) + ((self.y - my) ** 2))
        if distance < 65:
            return True
        else:
            return False
