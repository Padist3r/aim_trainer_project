import pygame
import random
import math


def random_xy():
    x = random.randint(65, 1220)
    y = random.randint(65, 670)
    return x, y


def draw_player(x, y):
    """Draw the player sights"""
    # x and y  are - 12 so the sights are centered on the mouse
    screen.blit(player_sights, (x - 12, y - 12))


def draw_target(x, y, mx, my):
    """
    Draws the target and checks to see if its been clicked on. If it has,
    it gets moved to a random location.
    :param x: Position x of the target.
    :param y: Position y of the target.
    :param mx: Position x of the mouse.
    :param my: Position y of the mouse.
    :return: None
    """
    global target_on
    global target_x
    global target_y

    if target_on:
        screen.blit(load_target, (x - 64, y - 64))

    if is_collision(mx, my, x, y):
        target_on = False
        target_x, target_y = random_xy()
    else:
        target_on = True


def is_collision(mx, my, tx, ty):
    """Checks to see if an object has been clicked on"""
    distance = math.sqrt(((tx - mx) ** 2) + ((ty - my) ** 2))
    if distance < 65 and mouse_click:
        return True
    else:
        return False


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
target_on = True
target_x, target_y = random_xy()
target_x2, target_y2 = random_xy()

# Hides the OS mouse
pygame.mouse.set_visible(False)
mouse_click = False

# Levels
level = 1


# Game loop
running = True
while running:

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Checks for player inputs and button presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the left mouse button is clicked
            if event.button == 1:
                mouse_click = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_click = False

    # What gets drawn on the screen (order matters)
    screen.fill(white)
    draw_target(target_x, target_y, mouse_x, mouse_y)
    draw_player(mouse_x, mouse_y)
    pygame.display.update()

pygame.quit()
