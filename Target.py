import pygame


class Target:
    """
    This class will be responsible for creating and controlling targets.
    """
    def __init__(self, name, window, image_dir):
        self.name = name
        self.window = window
        self.image = pygame.image.load(image_dir)

    def draw_target(self, x, y):
        self.window.blit(self.image, x, y)
