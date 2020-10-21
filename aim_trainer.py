import pygame
import random

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


# Hides the OS mouse
pygame.mouse.set_visible(False)


def player(x, y):
    """Draw the player sights"""
    # x and y  are - 12 so the sights are centered on the mouse
    screen.blit(player_sights, (x - 12, y - 12))


# Game loop
running = True
while running:

    # Checks for player inputs and button presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # What gets drawn on the screen (order matters)
    screen.fill(white)
    player(mouse_x, mouse_y)
    pygame.display.update()


pygame.quit()
