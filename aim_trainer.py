import pygame
from Target_Class import Target


def draw_player(x, y):
    """Draw the player sights"""
    # x and y  are - 12 so the sights are centered on the mouse
    screen.blit(player_sights, (x - 12, y - 12))


if __name__ == '__main__':

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

    # Mouse Controls
    pygame.mouse.set_visible(False)
    mouse_click = False

    # Levels
    level = 1

    # Create targets
    t1 = Target("t1", screen, "Images\\bullseye.png")
    t2 = Target("t2", screen, "Images\\bullseye.png")

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
        t1.draw_target(mouse_click)
        t2.draw_target(mouse_click)
        draw_player(mouse_x, mouse_y)
        pygame.display.update()

    pygame.quit()
