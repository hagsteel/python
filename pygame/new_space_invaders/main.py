import sys
from os.path import abspath, dirname

import pygame

pygame.init()

SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

BASE_PATH = abspath(dirname(__file__))

FONT_PATH = BASE_PATH + "/fonts/"
FONT = FONT_PATH + "space_invaders.ttf"
TITLE_FONT = pygame.font.Font(FONT, 50)
SUB_TITLE_FONT = pygame.font.Font(FONT, 25)
MAIN_FONT = pygame.font.Font(FONT, 20)

IMAGE_PATH = BASE_PATH + "/images/"
SOUND_PATH = BASE_PATH + "/sounds/"

ICON = pygame.image.load(IMAGE_PATH + "ufo.png")
pygame.display.set_icon(ICON)

BACKGROUND = pygame.image.load(IMAGE_PATH + "background.jpeg")

SHIP = pygame.image.load(IMAGE_PATH + "ship.png")
SHIP_RECT = SHIP.get_rect(topleft=(375, 540))
SHIP_SPEED = 5

NUM_OF_ENEMIES = 10
ENEMY_IMG = []
ENEMY1_RECT = []
ENEMY2_RECT = []
ENEMY_SPEED = 2
ENEMY_PUSH_DOWN = 40
X = 105
group_enemies = []

for enemies in range(NUM_OF_ENEMIES):
    X += 50
    ENEMY = pygame.image.load(IMAGE_PATH + "enemy3_1.png")
    ENEMY_IMG.append(pygame.transform.scale(ENEMY, (40, 40)))
    ENEMY1_RECT.append(ENEMY_IMG[enemies].get_rect(topleft=(X, 60)))
    ENEMY2_RECT.append(ENEMY_IMG[enemies].get_rect(topleft=(X, 100)))

BULLET = pygame.image.load(IMAGE_PATH + "laser.png")
BULLET_STATE = "Ready"
BULLET_Y = 540
BULLET_SPEED = 18

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (78, 255, 87)

# Game variables
CLOCK = pygame.time.Clock()
FPS = 60


def main_menu():
    while True:
        CLOCK.tick(FPS)

        title_text = TITLE_FONT.render("Space Invaders", True, WHITE)
        title_text2 = SUB_TITLE_FONT.render("Press enter to continue", True, WHITE)
        point_text = SUB_TITLE_FONT.render("   =   10 pts", True, GREEN)

        SCREEN.blit(BACKGROUND, (0, 0))
        SCREEN.blit(title_text, (164, 155))
        SCREEN.blit(title_text2, (201, 225))
        SCREEN.blit(ENEMY_IMG[0], (318, 270))
        SCREEN.blit(point_text, (368, 270))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()

        pygame.display.update()


def bunker():
    width = 100
    height = 50
    y_axis = 450
    pygame.draw.rect(SCREEN, GREEN, (70, y_axis, width, height))
    pygame.draw.rect(SCREEN, GREEN, (350, y_axis, width, height))
    pygame.draw.rect(SCREEN, GREEN, (650, y_axis, width, height))


def draw_enemies():
    global ENEMY_SPEED

    for i in range(NUM_OF_ENEMIES):
        # TODO: Treat them as a group instead of moving them one by one
        # TODO: Have one position for all of the enemies, instead of giving
        # each enemy its own position
        group_enemies.append(ENEMY1_RECT[i].x)

        for num in ENEMY1_RECT:
            num.x += ENEMY_SPEED
            if num.x <= 1:
                ENEMY_SPEED = 2
            elif num.x >= 755:
                ENEMY_SPEED = -2

        SCREEN.blit(ENEMY_IMG[i], ENEMY1_RECT[i])
        SCREEN.blit(ENEMY_IMG[i], ENEMY2_RECT[i])

        """ENEMY1_RECT[i].x += ENEMY_SPEED[i]
        if ENEMY1_RECT[i].x <= 1:
            ENEMY_SPEED[i] = 2
        elif ENEMY1_RECT[i].x >= 755:
            ENEMY_SPEED[i] = -2"""

        """ENEMY1_RECT[i].x += ENEMY_SPEED[i]
        if ENEMY1_RECT[i].x <= 1:
            ENEMY_SPEED[i] = 2
            ENEMY1_RECT[i].y += ENEMY_PUSH_DOWN[i]
        elif ENEMY1_RECT[i].x >= 755:
            ENEMY_SPEED[i] = -2
            ENEMY1_RECT[i].y += ENEMY_PUSH_DOWN[i]

        ENEMY2_RECT[i].x += ENEMY_SPEED[i]
        if ENEMY2_RECT[i].x <= 1:
            ENEMY_SPEED[i] = 2
            ENEMY2_RECT[i].y += ENEMY_PUSH_DOWN[i]
        elif ENEMY2_RECT[i].x >= 755:
            ENEMY_SPEED[i] = -2
            ENEMY2_RECT[i].y += ENEMY_PUSH_DOWN[i]"""


def bullet(spaceship_x, spaceship_y):
    global BULLET_STATE

    BULLET_STATE = "Fire"
    SCREEN.blit(BULLET, (spaceship_x + 23, spaceship_y))


def main():
    global BULLET_Y, BULLET_STATE

    pygame.key.set_repeat(1, 10)

    while True:
        CLOCK.tick(FPS)

        SCREEN.fill(BLACK)
        SCREEN.blit(BACKGROUND, (0, 0))

        lives_text = MAIN_FONT.render("Lives", True, WHITE)
        tiny_enemy = pygame.transform.scale(ENEMY, (25, 25))
        score_text = MAIN_FONT.render("Score", True, WHITE)
        score_text_num = MAIN_FONT.render("0", True, GREEN)

        SCREEN.blit(lives_text, (640, 5))
        SCREEN.blit(tiny_enemy, (715, 3))
        SCREEN.blit(tiny_enemy, (742, 3))
        SCREEN.blit(tiny_enemy, (769, 3))
        SCREEN.blit(score_text, (5, 5))
        SCREEN.blit(score_text_num, (85, 5))

        draw_enemies()
        bunker()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and SHIP_RECT.x > 10:
            SHIP_RECT.x -= SHIP_SPEED
        if keys[pygame.K_RIGHT] and SHIP_RECT.x < 740:
            SHIP_RECT.x += SHIP_SPEED
        if keys[pygame.K_SPACE]:
            if BULLET_STATE == "Ready":
                bullet_x = SHIP_RECT.x
                bullet(bullet_x, BULLET_Y)
        SCREEN.blit(SHIP, SHIP_RECT)

        # Bullet movement
        if BULLET_Y <= 0:
            BULLET_Y = 540
            BULLET_STATE = "Ready"
        if BULLET_STATE == "Fire":
            bullet(bullet_x, BULLET_Y)
            BULLET_Y -= BULLET_SPEED

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
