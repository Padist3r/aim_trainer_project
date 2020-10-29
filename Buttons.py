import pygame
import random
import math
import time


class Target:
    """
    This class is responsible for creating and controlling targets.
    """

    @staticmethod
    def get_xy():
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
        mx, my = pygame.mouse.get_pos()
        distance = \
            math.sqrt(((self.xy[0] - mx) ** 2) + ((self.xy[1] - my) ** 2))
        if distance < 65:
            return True
        else:
            return False


class Text:
    """
    This class is responsible for creating and displaying all of the text boxes
    that will be rendered to the screen
    """

    def __init__(self, screen, text, font, x, y, colour, bg_colour=None):
        self.screen = screen
        self.text = text
        self.font = font
        self.x = x
        self.y = y
        self.colour = colour
        self.bg_colour = bg_colour

    def display_text(self):
        text = self.font.render(self.text, True, self.colour, self.bg_colour)
        text_rect = text.get_rect()
        text_rect.center = (self.x, self.y)
        self.screen.blit(text, text_rect)
