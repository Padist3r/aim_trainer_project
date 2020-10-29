import pygame
import time
from Buttons import Target, Text


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
    main_text = Text(screen, "Aim Training Program", main_font,
                     main_pos_x, main_pos_y, white, red)
    main_text2 = Text(screen, "Aim Training Program", main_font,
                      main_pos_x, main_pos_y, red, white)
    # Start Button
    start_text = Text(screen, "START", main_font, main_pos_x, start_pos_y,
                      black)
    start_text2 = Text(screen, "START", main_font, main_pos_x, start_pos_y,
                       gray)

    if game_state == "start":
        screen.fill(white)
        if collision(main_pos_x, main_pos_y, 700, 64, mouse_x, mouse_y):
            main_text2.display_text()
        else:
            main_text.display_text()

        if collision(main_pos_x, start_pos_y, 180, 64, mouse_x, mouse_y):
            start_text2.display_text()
        else:
            start_text.display_text()

        if collision(res_x // 2, res_y // 1.5, 180, 64, mouse_x, mouse_y)\
                and mouse_click:
            game_state = "play"

        draw_player(mouse_x, mouse_y)


def play_screen():
    global game_state
    global score
    global timer
    # Score text
    score_text = Text(screen, f"Score: {str(score)}", score_font,
                      100, 30, black)
    miss_text = Text(screen, f"Misses: {str(misses)}", score_font,
                     91, 60, black)
    # Time remaining text
    time_text = Text(screen, f"Remaining Time: {str(timer)}", score_font,
                     1100, 30, black)

    if game_state == "play":
        # What gets drawn on the screen (order matters)

        screen.fill(white)
        score_text.display_text()
        miss_text.display_text()
        time_text.display_text()
        t1.draw_target(mouse_click, 2)
        t2.draw_target(mouse_click, 2)
        draw_player(mouse_x, mouse_y)

        if timer == -1:
            timer = reset_time
            game_state = "start"


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

    # Clock and Time
    Clock = pygame.time.Clock()
    CLOCK_TICK = pygame.USEREVENT + 1
    pygame.time.set_timer(CLOCK_TICK, 1000)
    reset_time = 11
    timer = reset_time

    # Title and Icon
    pygame.display.set_caption("Aim Trainer")
    icon = pygame.image.load("Images\\aim.png")
    pygame.display.set_icon(icon)

    # Player Sights
    player_sights = pygame.image.load("Images\\sight.png")  # 24px

    # Mouse Controls
    pygame.mouse.set_visible(False)

    # Game State and Levels
    game_state = "start"
    level = 1

    # Create targets
    t1 = Target("t1", screen, "Images\\bullseye.png")
    t2 = Target("t2", screen, "Images\\bullseye.png")

    # Game loop
    running = True
    while running:
        mouse_click = False
        # Counts the hits and misses
        score = t1.hit_counter + t2.hit_counter
        misses = int(round(t1.miss_counter + t2.miss_counter))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Checks for player inputs and button presses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_state = "start"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_click = True
                continue
            else:
                mouse_click = False
            if event.type == CLOCK_TICK and game_state == "play":
                timer -= 1
                print(timer)

        if game_state == "start":
            start_screen()
        if game_state == "play":
            play_screen()

        pygame.display.update()

        Clock.tick(60)

    pygame.quit()
