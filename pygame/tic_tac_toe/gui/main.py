import os.path
import sys
import random
import pygame

pygame.init()

# Screen
WIDTH, HEIGHT = 550, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))

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

# Loading images
project_directory = os.path.dirname(__file__)
x_img = pygame.image.load(os.path.join(project_directory, "img/x.png"))
o_img = pygame.image.load(os.path.join(project_directory, "img/o.png"))

# Resizing images
WIDTH_RESIZE, HEIGHT_RESIZE = 110, 110
x_img = pygame.transform.scale(x_img, (WIDTH_RESIZE, HEIGHT_RESIZE))
o_img = pygame.transform.scale(o_img, (WIDTH_RESIZE, HEIGHT_RESIZE))

# Game variables
current_player = "X"
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
won = False
won_x = False
won_o = False
x_score = 0
o_score = 0
is_click = "not click"
is_game_end = False
current_player_turn = "X"

# Fonts
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
    for row in board:
        for tile in row:
            if tile == number:
                continue
            else:
                break
        else:
            return True

    for column in range(3):
        for row in board:
            if row[column] == number:
                continue
            else:
                break
        else:
            return True

    for tile in range(3):
        if board[tile][tile] == number:
            continue
        else:
            break
    else:
        return True

    for tile in range(3):
        if board[tile][2 - tile] == number:
            continue
        else:
            break
    else:
        return True


def num():
    global won_x, won_o

    if check_win(1):
        won_x = True
    elif check_win(2):
        won_o = True


def x_turn():
    if current_player == "X":
        x_turn_text = FONT.render("X turn", True, WHITE)
        screen.blit(x_turn_text, (130, 550))
        pygame.draw.rect(screen, BLACK, (120, 600, 110, 30))


def o_turn():
    if current_player == "O":
        o_turn_text = FONT.render("O turn", True, WHITE)
        screen.blit(o_turn_text, (130, 600))
        pygame.draw.rect(screen, BLACK, (130, 550, 110, 30))


def score_x():
    score_value = FONT.render("X " + str(x_score), True, WHITE)
    screen.blit(score_value, (50, 550))


def score_o():
    score_value = FONT.render("O " + str(o_score), True, WHITE)
    screen.blit(score_value, (50, 600))


def draw_text_won():
    global OVER_FONT

    if won_x:
        over_text = OVER_FONT.render("X won", True, LIGHT_BLUE)
        space_text = OVER_FONT.render("Space bar for clear", True, LIGHT_BLUE)
        screen.blit(over_text, (220, 200))
        screen.blit(space_text, (50, 300))

    elif won_o:
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
    global current_player_turn

    while current_player_turn == "Computer":
        row = random.randint(0, 2)
        column = random.randint(0, 2)

        x = [50, 225, 400][column]
        y = [50, 225, 400][row]

        if board[row][column] == 0:
            screen.blit(o_img, (x, y))
            board[row][column] = 2
            current_player_turn = "X"

def best_ai():
    bestscore = float('-inf')
    for row, column in range(3):
        if board[row][column] == 0:
            board[row][column] = ai
            score = minimax(board)
            board[row][column] = 0
            if score > bestscore:
                bestscore = score
                bestmove = board[row][column]

def minimax(board):
    return 1

def flip_ai_player():
    global current_player_turn

    if current_player_turn == "X":
        current_player_turn = "Computer"
    elif current_player_turn == "Computer":
        current_player_turn = "X"


def is_board_fill():
    return board[0][0] != 0 and board[0][1] != 0 and \
           board[0][2] != 0 and board[1][0] != 0 and \
           board[1][1] != 0 and board[1][2] != 0 and \
           board[2][0] != 0 and board[2][1] != 0 and \
           board[2][2] != 0


def game_intro():
    global x_score, o_score, won_x, won_o, won, board, click, current_player_turn

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    mode_computer = pygame.draw.rect(screen, GREY, (250, 560, 160, 50))

    if mode_computer.collidepoint(mouse):
        pygame.draw.rect(screen, BRIGHT_GREY, (250, 560, 160, 50))
        if click[0] == 1:
            won_x = False
            won_o = False
            won = False
            x_score = 0
            o_score = 0
            current_player_turn = "Computer"
            board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            screen.fill((0, 0, 0))
            draw_rectangle()

    computer = FONT.render("Computer", True, (255, 255, 255))
    screen.blit(computer, (260, 570))


def is_button_click():
    global is_click

    if not click[0] == 1 and is_click == "not click":
        click_on_button = FONT.render("Click   on   the   button   to   play", True, (255, 255, 255))
        screen.blit(click_on_button, (55, 200))
        is_click = "click"


def mode_ai():
    pos = pygame.mouse.get_pos()
    game_intro()

    if won is not True:
        if first.collidepoint(pos) and board[0][0] == 0:
            if current_player == "X":
                screen.blit(x_img, (50, 50))
                board[0][0] = 1
                if not is_board_fill():
                    ai()
                    flip_ai_player()

        if second.collidepoint(pos) and board[0][1] == 0:
            if current_player == "X":
                screen.blit(x_img, (225, 50))
                board[0][1] = 1
                if not is_board_fill():
                    ai()
                    flip_ai_player()

        if third.collidepoint(pos) and board[0][2] == 0:
            if current_player == "X":
                screen.blit(x_img, (400, 50))
                board[0][2] = 1
                if not is_board_fill():
                    ai()
                    flip_ai_player()

        if fourth.collidepoint(pos) and board[1][0] == 0:
            if current_player == "X":
                screen.blit(x_img, (50, 225))
                board[1][0] = 1
                if not is_board_fill():
                    ai()
                    flip_ai_player()

        if fifth.collidepoint(pos) and board[1][1] == 0:
            if current_player == "X":
                screen.blit(x_img, (225, 225))
                board[1][1] = 1
                if not is_board_fill():
                    ai()
                    flip_ai_player()

        if sixth.collidepoint(pos) and board[1][2] == 0:
            if current_player == "X":
                screen.blit(x_img, (400, 225))
                board[1][2] = 1
                if not is_board_fill():
                    ai()
                    flip_ai_player()

        if seventh.collidepoint(pos) and board[2][0] == 0:
            if current_player == "X":
                screen.blit(x_img, (50, 400))
                board[2][0] = 1
                if not is_board_fill():
                    ai()
                    flip_ai_player()

        if eighth.collidepoint(pos) and board[2][1] == 0:
            if current_player == "X":
                screen.blit(x_img, (225, 400))
                board[2][1] = 1
                if not is_board_fill():
                    ai()
                    flip_ai_player()

        if ninth.collidepoint(pos) and board[2][2] == 0:
            if current_player == "X":
                screen.blit(x_img, (400, 400))
                board[2][2] = 1
                if not is_board_fill():
                    ai()
                    flip_ai_player()


while True:
    click = pygame.mouse.get_pressed()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                won_x = False
                won_o = False
                won = False
                is_game_end = False
                board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                screen.fill((0, 0, 0))
                draw_rectangle()
                ai()
                flip_ai_player()

        if event.type == pygame.MOUSEBUTTONDOWN:
            try:
                mode_ai()
            except:
                pass

            check_win(num)
            num()
            if won_x is False and won_o is False and is_board_fill():
                tie()
            if is_game_end is False:
                if check_win(1):
                    is_game_end = True
                    won = True
                    x_score += 1
                if check_win(2):
                    is_game_end = True
                    won = True
                    o_score += 1
            draw_text_won()

        is_button_click()
        game_intro()
        x_turn()
        o_turn()
        score_x()
        score_o()

    pygame.display.update()
