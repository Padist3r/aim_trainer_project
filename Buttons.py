import pygame
import random
import math


class Target:
    """
    This class is responsible for creating and controlling targets.
    """

    @staticmethod
    def get_xy():
        xy = (random.randint(64, 1220), random.randint(64, 660))
        return xy

    @staticmethod
    def mouse_button1():
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                return True
            else:
                return False

    def __init__(self, name, window, image_dir):
        self.name = name
        self.window = window
        self.image = pygame.image.load(image_dir)
        self.xy = (0, 0)
        self.hit_counter = 0
        self.miss_counter = 0

    def draw_target(self):
        image = self.image
        if self.xy == (0, 0):
            self.xy = Target.get_xy()
        else:
            self.window.blit(image, (self.xy[0] - 64, self.xy[1] - 64))
            if Target.is_collide(self):
                self.xy = Target.get_xy()

    def is_collide(self):
        mx, my = pygame.mouse.get_pos()
        distance = \
            math.sqrt(((self.xy[0] - mx) ** 2) + ((self.xy[1] - my) ** 2))
        if distance < 65 and Target.mouse_button1():
            self.hit_counter += 1
            return True
        else:
            return False


