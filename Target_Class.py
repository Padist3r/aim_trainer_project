import pygame
import random
import math


class Target:
    """
    This class is responsible for creating and controlling targets.
    """
    def __init__(self, name, window, image_dir):
        self.name = name
        self.window = window
        self.image = pygame.image.load(image_dir)
        self.move = True
        self.xy = ()
        self.mouse_is_clicked = False

    def draw_target(self, is_click):
        image = self.image
        self.mouse_is_clicked = is_click
        self.xy = Target.get_xy(self)
        self.move = False
        self.window.blit(image, (self.xy[0] - 64, self.xy[1] - 64))
        if Target.is_collide(self) is True:
            self.move = True
            self.xy = Target.get_xy(self)

    def get_xy(self):
        if self.move is True:
            xy = (random.randint(64, 1220), random.randint(64, 660))
            return xy
        else:
            xy = self.xy
            return xy

    def is_collide(self):
        mx, my = pygame.mouse.get_pos()
        distance = \
            math.sqrt(((self.xy[0] - mx) ** 2) + ((self.xy[1] - my) ** 2))
        if distance < 65 and self.mouse_is_clicked:
            return True
        else:
            return False
