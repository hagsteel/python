import os.path
import sys
import random

import pygame

pygame.init()

# Screen
WIDTH, HEIGHT = 550, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Caption
pygame.display.set_caption("Tic Tac Toe")

# Colors
WHITE = (255, 255, 255)
GREY = (72, 72, 72)
BRIGHT_GREY = (60, 60, 90)
BLACK = (0, 0, 0)
DARK_BLUE = (9, 109, 209)
PINK = (255, 0, 255)
LIGHT_BLUE = (108, 176, 243)

# FPS
clock = pygame.time.Clock()
FPS = 60

# Images
project_directory = os.path.dirname(__file__)
x_img = pygame.image.load(os.path.join(project_directory, "img/x.png"))
o_img = pygame.image.load(os.path.join(project_directory, "img/o.png"))

# Resize images
WIDTH_RESIZE, HEIGHT_RESIZE = 110, 110
x_img = pygame.transform.scale(x_img, (WIDTH_RESIZE, HEIGHT_RESIZE))
o_img = pygame.transform.scale(o_img, (WIDTH_RESIZE, HEIGHT_RESIZE))

# Game variables
CURRENT_PLAYER = "X"
BOARD = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
WON = False
WON_X = False
WON_O = False
X_SCORE = 0
O_SCORE = 0
IS_CLICK = "not click"
IS_GAME_END = False
CURRENT_PLAYER_TURN = "X"

# Font
ARCADECLASSIC = os.path.join(project_directory, "font/arcadeclassic.regular.ttf")
FONT = pygame.font.Font(ARCADECLASSIC, 32)
OVER_FONT = pygame.font.Font(ARCADECLASSIC, 50)


def draw_rectangle():
    global first, second, third, fourth, fifth, sixth, seventh, eighth, ninth

    first = pygame.draw.rect(screen, WHITE, (25, 25, 150, 150))
    second = pygame.draw.rect(screen, WHITE, (200, 25, 150, 150))
    third = pygame.draw.rect(screen, WHITE, (375, 25, 150, 150))
    fourth = pygame.draw.rect(screen, WHITE, (25, 200, 150, 150))
    fifth = pygame.draw.rect(screen, WHITE, (200, 200, 150, 150))
    sixth = pygame.draw.rect(screen, WHITE, (375, 200, 150, 150))
    seventh = pygame.draw.rect(screen, WHITE, (25, 375, 150, 150))
    eighth = pygame.draw.rect(screen, WHITE, (200, 375, 150, 150))
    ninth = pygame.draw.rect(screen, WHITE, (375, 375, 150, 150))


def check_win(number):
    for row in BOARD:
        for tile in row:
            if tile == number:
                continue
            break
        else:
            return True

    for column in range(3):
        for row in BOARD:
            if row[column] == number:
                continue
            break
        else:
            return True

    for tile in range(3):
        if BOARD[tile][tile] == number:
            continue
        break
    else:
        return True

    for tile in range(3):
        if BOARD[tile][2 - tile] == number:
            continue
        break
    else:
        return True


def num():
    global WON_X, WON_O

    if check_win(1):
        WON_X = True
    elif check_win(2):
        WON_O = True


def x_turn():
    if CURRENT_PLAYER == "X":
        x_turn_text = FONT.render("X turn", True, WHITE)
        screen.blit(x_turn_text, (130, 550))
        pygame.draw.rect(screen, BLACK, (120, 600, 110, 30))


def o_turn():
    if CURRENT_PLAYER == "O":
        o_turn_text = FONT.render("O turn", True, WHITE)
        screen.blit(o_turn_text, (130, 600))
        pygame.draw.rect(screen, BLACK, (130, 550, 110, 30))


def score_x():
    score_value = FONT.render("X " + str(X_SCORE), True, WHITE)
    screen.blit(score_value, (50, 550))


def score_o():
    score_value = FONT.render("O " + str(O_SCORE), True, WHITE)
    screen.blit(score_value, (50, 600))


def draw_text_won():
    global OVER_FONT

    if WON_X:
        over_text = OVER_FONT.render("X won", True, LIGHT_BLUE)
        space_text = OVER_FONT.render("Space bar for clear", True, LIGHT_BLUE)
        screen.blit(over_text, (220, 200))
        screen.blit(space_text, (50, 300))

    elif WON_O:
        over_text = OVER_FONT.render("Computer won", True, PINK)
        space_text = OVER_FONT.render("Space bar for clear", True, PINK)
        screen.blit(over_text, (140, 200))
        screen.blit(space_text, (50, 300))


def tie():
    global OVER_FONT

    tie_text = OVER_FONT.render("Tie", True, DARK_BLUE)
    space_text = OVER_FONT.render("Space bar for clear", True, DARK_BLUE)
    screen.blit(tie_text, (220, 200))
    screen.blit(space_text, (50, 300))


# Computer(AI)
def ai():
    global CURRENT_PLAYER_TURN

    while CURRENT_PLAYER_TURN == "Computer":
        row = random.randint(0, 2)
        column = random.randint(0, 2)

        x = [50, 225, 400][column]
        y = [50, 225, 400][row]

        if BOARD[row][column] == 0:
            screen.blit(o_img, (x, y))
            BOARD[row][column] = 2
            CURRENT_PLAYER_TURN = "X"


def best_ai():
    global CURRENT_PLAYER_TURN, BOARD

    first_time = True

    if first_time:
        ai()
        first_time = False

    if BOARD[0][1] == 1 and BOARD[0][2] == 1:
        if BOARD[0][0] == 0:
            x = [50, 225, 400][0]
            y = [50, 225, 400][0]
            BOARD[0][0] = 2
            screen.blit(o_img, (x, y))
        else:
            ai()

    if BOARD[1][1] == 1 and BOARD[1][2] == 1:
        if BOARD[0][1] == 0:
            x = [50, 225, 400][0]
            y = [50, 225, 400][1]
            BOARD[0][1] = 2
            screen.blit(o_img, (x, y))

        else:
            ai()


def flip_ai_player():
    global CURRENT_PLAYER_TURN

    if CURRENT_PLAYER_TURN == "X":
        CURRENT_PLAYER_TURN = "Computer"
    elif CURRENT_PLAYER_TURN == "Computer":
        CURRENT_PLAYER_TURN = "X"


def is_board_fill():
    return BOARD[0][0] != 0 and BOARD[0][1] != 0 and \
           BOARD[0][2] != 0 and BOARD[1][0] != 0 and \
           BOARD[1][1] != 0 and BOARD[1][2] != 0 and \
           BOARD[2][0] != 0 and BOARD[2][1] != 0 and \
           BOARD[2][2] != 0


def game_intro():
    global X_SCORE, O_SCORE, WON_X, WON_O, WON, BOARD, CLICK, CURRENT_PLAYER_TURN

    mouse = pygame.mouse.get_pos()
    CLICK = pygame.mouse.get_pressed()
    mode_computer = pygame.draw.rect(screen, GREY, (250, 560, 160, 50))

    if mode_computer.collidepoint(mouse):
        pygame.draw.rect(screen, BRIGHT_GREY, (250, 560, 160, 50))
        if CLICK[0] == 1:
            WON_X = False
            WON_O = False
            WON = False
            X_SCORE = 0
            O_SCORE = 0
            CURRENT_PLAYER_TURN = "Computer"
            BOARD = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            screen.fill((0, 0, 0))
            draw_rectangle()

    computer = FONT.render("Computer", True, (255, 255, 255))
    screen.blit(computer, (260, 570))


def is_button_click():
    global IS_CLICK

    if not CLICK[0] == 1 and IS_CLICK == "not click":
        click_on_button = FONT.render("Click   on   the   button   to   play",
                                      True, (255, 255, 255))
        screen.blit(click_on_button, (55, 200))
        IS_CLICK = "click"


def mode_ai():
    pos = pygame.mouse.get_pos()
    game_intro()

    if WON is not True:
        if first.collidepoint(pos) and BOARD[0][0] == 0:
            if CURRENT_PLAYER == "X":
                screen.blit(x_img, (50, 50))
                BOARD[0][0] = 1
                if not is_board_fill():
                    # ai()
                    best_ai()
                    flip_ai_player()

        if second.collidepoint(pos) and BOARD[0][1] == 0:
            if CURRENT_PLAYER == "X":
                screen.blit(x_img, (225, 50))
                BOARD[0][1] = 1
                if not is_board_fill():
                    # ai()
                    best_ai()
                    flip_ai_player()

        if third.collidepoint(pos) and BOARD[0][2] == 0:
            if CURRENT_PLAYER == "X":
                screen.blit(x_img, (400, 50))
                BOARD[0][2] = 1
                if not is_board_fill():
                    # ai()
                    best_ai()
                    flip_ai_player()

        if fourth.collidepoint(pos) and BOARD[1][0] == 0:
            if CURRENT_PLAYER == "X":
                screen.blit(x_img, (50, 225))
                BOARD[1][0] = 1
                if not is_board_fill():
                    # ai()
                    best_ai()
                    flip_ai_player()

        if fifth.collidepoint(pos) and BOARD[1][1] == 0:
            if CURRENT_PLAYER == "X":
                screen.blit(x_img, (225, 225))
                BOARD[1][1] = 1
                if not is_board_fill():
                    # ai()
                    best_ai()
                    flip_ai_player()

        if sixth.collidepoint(pos) and BOARD[1][2] == 0:
            if CURRENT_PLAYER == "X":
                screen.blit(x_img, (400, 225))
                BOARD[1][2] = 1
                if not is_board_fill():
                    # ai()
                    best_ai()
                    flip_ai_player()

        if seventh.collidepoint(pos) and BOARD[2][0] == 0:
            if CURRENT_PLAYER == "X":
                screen.blit(x_img, (50, 400))
                BOARD[2][0] = 1
                if not is_board_fill():
                    # ai()
                    best_ai()
                    flip_ai_player()

        if eighth.collidepoint(pos) and BOARD[2][1] == 0:
            if CURRENT_PLAYER == "X":
                screen.blit(x_img, (225, 400))
                BOARD[2][1] = 1
                if not is_board_fill():
                    # ai()
                    best_ai()
                    flip_ai_player()

        if ninth.collidepoint(pos) and BOARD[2][2] == 0:
            if CURRENT_PLAYER == "X":
                screen.blit(x_img, (400, 400))
                BOARD[2][2] = 1
                if not is_board_fill():
                    # ai()
                    best_ai()
                    flip_ai_player()


while True:
    CLICK = pygame.mouse.get_pressed()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                WON_X = False
                WON_O = False
                WON = False
                IS_GAME_END = False
                BOARD = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                screen.fill((0, 0, 0))
                draw_rectangle()
                # ai()
                best_ai()
                flip_ai_player()

        if event.type == pygame.MOUSEBUTTONDOWN:
            try:
                mode_ai()
            except:
                pass

            check_win(num)
            num()

            if WON_X is False and WON_O is False and is_board_fill():
                tie()

            if IS_GAME_END is False:
                if check_win(1):
                    IS_GAME_END = True
                    WON = True
                    X_SCORE += 1
                if check_win(2):
                    IS_GAME_END = True
                    WON = True
                    O_SCORE += 1

            draw_text_won()

        is_button_click()
        game_intro()
        x_turn()
        o_turn()
        score_x()
        score_o()

    pygame.display.update()
