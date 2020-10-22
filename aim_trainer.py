import pygame
import random
import math

# Colours to use
black = (0, 0, 0)
white = (255, 255, 255)

# Initialize
pygame.init()

# Create the screen
screen = pygame.display.set_mode((1280, 720))

# Title and Icon
pygame.display.set_caption("Aim Trainer")
icon = pygame.image.load("Images\\aim.png")
pygame.display.set_icon(icon)

# Player Sights
player_sights = pygame.image.load("Images\\sight.png")  # 24px

# Target
load_target = pygame.image.load("Images\\bullseye.png")     # 128px
target_x = 500
target_y = 500

# Hides the OS mouse
pygame.mouse.set_visible(False)
mouse_click = False


def player(x, y):
    """Draw the player sights"""
    # x and y  are - 12 so the sights are centered on the mouse
    screen.blit(player_sights, (x - 12, y - 12))


def draw_target(x, y):
    """Draws the targets"""
    screen.blit(load_target, (x - 64, y - 64))


def is_collision(px, py, tx, ty):
    distance = math.sqrt(((tx - px) ** 2) + ((ty - py) ** 2))
    if distance < 65:
        return True
    else:
        return False


# Game loop
running = True
while running:

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Checks for player inputs and button presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_click = False

    # What gets drawn on the screen (order matters)
    screen.fill(white)

    # This checks to see if you have clicked on the target
    # I still need to figure out how to fully remove target and redraw a new one
    if is_collision(mouse_x, mouse_y, target_x, target_y) and mouse_click:
        pass
    else:
        draw_target(target_x, target_y)

    player(mouse_x, mouse_y)
    pygame.display.update()

pygame.quit()
