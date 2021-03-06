import pygame
from classes import Target, Text


def draw_player(x, y):
    """Draw the player sights"""
    # x and y  are - 12 so the sights are centered on the mouse
    screen.blit(player_sights, (x - 12, y - 12))


def start_screen():
    """Displays the start screen"""

    global game_state
    # Set up text
    main_text = Text(screen, "Aim Training Program", main_font, center_x, y_top
                     , white, black, red)
    start_text = Text(screen, "START", main_font, center_x, y_bottom,
                      black, gray)
    options_text = Text(screen, "OPTIONS", score_font, center_x, y_very_bottom
                        , black, gray)
    # Draw to screen

    screen.fill(white)
    t1.draw_target()
    t1.move_target()
    t2.draw_target()
    t2.move_target()
    t3.draw_target()
    t3.move_target()
    t4.draw_target()
    t4.move_target()
    main_text.display_text()
    start_text.display_text()
    options_text.display_text()
    draw_player(mouse_x, mouse_y)
    if start_text.mouse_over() and mouse_click:
        game_state = "play"
        # resetting target positions from the start screen
        t1.xy, t2.xy, t3.xy, t4.xy = [0, 0], [0, 0], [0, 0], [0, 0]
    if options_text.mouse_over() and mouse_click:
        game_state = "options"


def play_screen():
    """Displays the play screen"""

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
                     res_x - 200, 30, black)

    # Draw to the screen
    screen.fill(white)
    score_text.display_text()
    miss_text.display_text()
    time_text.display_text()
    t1.draw_target(mouse_click, 2)
    t1.move_target()
    t2.draw_target(mouse_click, 2)
    t2.move_target()
    draw_player(mouse_x, mouse_y)

    if timer == -1:
        timer = reset_time
        game_state = "score"


def score_screen():
    """Displays the score screen."""

    global game_state
    global score
    global misses

    # Calculates the accuracy
    if score == 0:
        accuracy = 0.0
    elif misses == 0:
        accuracy = 100.0
    else:
        accuracy = 100 - ((misses / score) * (100 // 1))

    # Set up for text
    times_up_text = Text(screen, "TIMES UP!", main_font, 640, 100, black, red)
    score_text = Text(screen, f"Targets hit: {score}!", score_font,
                      640, 250, black)
    miss_text = Text(screen, f"Targets missed: {misses}!", score_font,
                     613, 300, black)
    accuracy_text = Text(screen,
                         f"Overall Accuracy: {round(accuracy, 2)}%",
                         score_font, 613, 350, black)
    restart_text = Text(screen, "Restart", score_font, 440, 500, black, gray)
    return_text = Text(screen, "Return", score_font, 840, 500, black, gray)

    # Draw to the screen
    screen.fill(white)

    times_up_text.display_text()
    score_text.display_text()
    miss_text.display_text()
    accuracy_text.display_text()
    restart_text.display_text()
    return_text.display_text()
    draw_player(mouse_x, mouse_y)

    if restart_text.mouse_over() and mouse_click:
        t1.reset()
        t2.reset()
        game_state = "play"

    if return_text.mouse_over() and mouse_click:
        t1.reset()
        t2.reset()
        game_state = "start"


def options_screen():
    global res_x
    global res_y
    global screen
    global game_state

    screen_res_text = Text(screen, f"Screen Resolution: {res_x} x {res_y}",
                           score_font, center_x, 100, black, gray)
    return_text = Text(screen, "Return", score_font, center_x, y_bottom,
                       black, gray)

    screen.fill(white)
    screen_res_text.display_text()
    return_text.display_text()
    draw_player(mouse_x, mouse_y)

    if return_text.mouse_over() and mouse_click:
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

    # Screen Positions
    center_x = res_x // 2
    center_y = res_y // 2
    y_top = res_y // 4
    y_bottom = res_y // 1.5
    y_very_bottom = res_y // 1.1

    # Clock and Time
    Clock = pygame.time.Clock()
    CLOCK_TICK = pygame.USEREVENT + 1
    pygame.time.set_timer(CLOCK_TICK, 1000)
    reset_time = 20
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
    t3 = Target("t3", screen, "Images\\bullseye.png")
    t4 = Target("t4", screen, "Images\\bullseye.png")

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

        if game_state == "start":
            start_screen()
        if game_state == "play":
            play_screen()
        if game_state == "score":
            score_screen()
        if game_state == "options":
            options_screen()

        pygame.display.update()

        Clock.tick(120)

    pygame.quit()
