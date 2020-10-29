import pygame
from Buttons import Target


def draw_player(x, y):
    """Draw the player sights"""
    # x and y  are - 12 so the sights are centered on the mouse
    screen.blit(player_sights, (x - 12, y - 12))


def collision(x, y, w, h, mx, my):
    """
    Checks to see if the mouse is hovering over an object.
    :param x: pos x of object
    :param y: pos y of object
    :param w: width of object
    :param h: height of object
    :param mx: mouse pos x
    :param my: mouse pos y
    """
    if (x - w // 2) <= mx <= (x + w // 2) and (y - h // 2) <= my <=\
            (y + h // 2):
        return True
    else:
        return False


def start_screen():
    global game_state
    # Text Positions
    main_pos_x = res_x // 2
    main_pos_y = res_y // 3
    start_pos_y = res_y // 1.5
    # Main Title Text
    main_text = main_font.render("Aim Training Program", True, white, red)
    text_rect = main_text.get_rect()
    text_rect.center = (main_pos_x, main_pos_y)
    # Start Button
    start_text = main_font.render("START", True, red)
    start_rect = start_text.get_rect()
    start_rect.center = (main_pos_x, start_pos_y)

    if game_state == "start":
        screen.fill(white)
        if collision(main_pos_x, main_pos_y, 700, 64, mouse_x, mouse_y):
            main_text = main_font.render("Aim Training Program", True,
                                         red, white)
            screen.blit(main_text, text_rect)
        else:
            main_text = main_font.render("Aim Training Program", True,
                                         white, red)
            screen.blit(main_text, text_rect)

        if collision(main_pos_x, start_pos_y, 180, 64, mouse_x, mouse_y):
            start_text = main_font.render("START", True, gray)
            screen.blit(start_text, start_rect)
        else:
            start_text = main_font.render("START", True, black)
            screen.blit(start_text, start_rect)

        if collision(res_x // 2, res_y // 1.5, 180, 64, mouse_x, mouse_y)\
                and mouse_click:
            game_state = "play"

        draw_player(mouse_x, mouse_y)


def play_screen():
    global score
    global misses
    # Score text positions
    score_pos_x = 100
    score_pos_y = 30
    miss_pos_x = 118
    miss_pos_y = 60
    # Score text
    score_text = score_font.render(f"Score: {str(score)}", True, black)
    score_rect = score_text.get_rect()
    score_rect.center = (score_pos_x, score_pos_y)
    miss_text = score_font.render(f"Misses: {str(misses)}", True, black)
    miss_rect = miss_text.get_rect()
    miss_rect.center = (miss_pos_x, miss_pos_y)

    if game_state == "play":
        # What gets drawn on the screen (order matters)

        screen.fill(white)
        screen.blit(score_text, score_rect)
        screen.blit(miss_text, miss_rect)
        t1.draw_target()
        t2.draw_target()
        draw_player(mouse_x, mouse_y)


if __name__ == '__main__':

    # Initialize
    pygame.init()

    # Colours to use
    black = (0, 0, 0)
    white = (255, 255, 255)
    gray = (100, 100, 100)
    red = (255, 0, 0)
    blue = (0, 0, 255)

    # Fonts
    main_font = pygame.font.SysFont("Consolas", 64)
    score_font = pygame.font.SysFont("Consolas", 32)

    # Create the screen
    res_x = 1280
    res_y = 720
    screen = pygame.display.set_mode((res_x, res_y))

    # Title and Icon
    pygame.display.set_caption("Aim Trainer")
    icon = pygame.image.load("Images\\aim.png")
    pygame.display.set_icon(icon)

    # Player Sights
    player_sights = pygame.image.load("Images\\sight.png")  # 24px

    # Mouse Controls
    pygame.mouse.set_visible(False)
    mouse_click = False

    # Game State and Levels
    game_state = "play"
    level = 1
    misses = 0

    # Create targets
    t1 = Target("t1", screen, "Images\\bullseye.png")
    t2 = Target("t2", screen, "Images\\bullseye.png")

    # Game loop
    running = True
    while running:
        score = t1.hit_counter + t2.hit_counter
        if t1.miss_counter and t2.miss_counter:
            misses += 1
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Checks for player inputs and button presses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_state = "start"
        if game_state == "start":
            start_screen()
        elif game_state == "play":
            play_screen()
        pygame.display.update()

    pygame.quit()
