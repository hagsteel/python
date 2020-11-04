import sys
from os.path import abspath, dirname

import pygame
from pygame import mixer

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
enemy_pink_img = []
enemy_cyan_img = []
enemy_green_img = []
enemy_pink_rect = []
enemy1_cyan_rect = []
enemy2_cyan_rect = []
enemy1_green_rect = []
enemy2_green_rect = []
ENEMY_SPEED = 1
ENEMY_PUSH_DOWN = 10
X = 105

for enemies in range(NUM_OF_ENEMIES):
    X += 50
    ENEMY_PINK = pygame.image.load(IMAGE_PATH + "enemy1_2.png")
    ENEMY_GREEN = pygame.image.load(IMAGE_PATH + "enemy3_1.png")
    ENEMY_CYAN = pygame.image.load(IMAGE_PATH + "enemy2_1.png")

    enemy_green_img.append(pygame.transform.scale(ENEMY_GREEN, (40, 40)))
    enemy_pink_img.append(pygame.transform.scale(ENEMY_PINK, (40, 40)))
    enemy_cyan_img.append(pygame.transform.scale(ENEMY_CYAN, (40, 40)))

    enemy_pink_rect.append(enemy_pink_img[enemies].get_rect(topleft=(X, 60)))
    enemy1_cyan_rect.append(enemy_cyan_img[enemies].get_rect(topleft=(X, 100)))
    enemy2_cyan_rect.append(enemy_cyan_img[enemies].get_rect(topleft=(X, 140)))
    enemy1_green_rect.append(enemy_green_img[enemies].get_rect(topleft=(X, 180)))
    enemy2_green_rect.append(enemy_green_img[enemies].get_rect(topleft=(X, 220)))

BULLET = pygame.image.load(IMAGE_PATH + "laser.png")
BULLET_STATE = "Ready"
BULLET_Y = 540
BULLET_SPEED = 18
BULLET = BULLET.get_rect(topleft=(23, BULLET_Y))

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (78, 255, 87)

background_sound = mixer.Sound(SOUND_PATH + "background.wav")
background_sound.set_volume(0.2)
background_sound.play(-1)

# Game variables
CLOCK = pygame.time.Clock()
FPS = 60

print(f"Bullet {BULLET}")
for i in range(7):
    print(enemy1_green_rect[i])


def main_menu():
    while True:
        CLOCK.tick(FPS)

        title_text = TITLE_FONT.render("Space Invaders", True, WHITE)
        title_text2 = SUB_TITLE_FONT.render("Press enter to continue", True, WHITE)
        point_text = SUB_TITLE_FONT.render("   =   10 pts", True, GREEN)

        SCREEN.blit(BACKGROUND, (0, 0))
        SCREEN.blit(title_text, (164, 155))
        SCREEN.blit(title_text2, (201, 225))
        SCREEN.blit(enemy_green_img[0], (318, 270))
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

    for num in enemy_pink_rect:
        num.x += ENEMY_SPEED
    for num in enemy1_cyan_rect:
        num.x += ENEMY_SPEED
    for num in enemy2_cyan_rect:
        num.x += ENEMY_SPEED
    for num in enemy1_green_rect:
        num.x += ENEMY_SPEED
    for num in enemy2_green_rect:
        num.x += ENEMY_SPEED

    for i in range(NUM_OF_ENEMIES):
        for num in enemy_pink_rect:
            if num.x <= 1:
                ENEMY_SPEED = 1
                enemy_pink_rect[i].y += ENEMY_PUSH_DOWN
            elif num.x >= 755:
                ENEMY_SPEED = -0.5
                enemy_pink_rect[i].y += ENEMY_PUSH_DOWN
        for num in enemy1_cyan_rect:
            if num.x <= 1:
                ENEMY_SPEED = 1
                enemy1_cyan_rect[i].y += ENEMY_PUSH_DOWN
            elif num.x >= 755:
                ENEMY_SPEED = -0.5
                enemy1_cyan_rect[i].y += ENEMY_PUSH_DOWN
        for num in enemy2_cyan_rect:
            if num.x <= 1:
                ENEMY_SPEED = 1
                enemy2_cyan_rect[i].y += ENEMY_PUSH_DOWN
            elif num.x >= 755:
                ENEMY_SPEED = -0.5
                enemy2_cyan_rect[i].y += ENEMY_PUSH_DOWN
        for num in enemy1_green_rect:
            if num.x <= 1:
                ENEMY_SPEED = 1
                enemy1_green_rect[i].y += ENEMY_PUSH_DOWN
            elif num.x >= 755:
                ENEMY_SPEED = -0.5
                enemy1_green_rect[i].y += ENEMY_PUSH_DOWN
        for num in enemy2_green_rect:
            if num.x <= 1:
                ENEMY_SPEED = 1
                enemy2_green_rect[i].y += ENEMY_PUSH_DOWN
            elif num.x >= 755:
                ENEMY_SPEED = -0.5
                enemy2_green_rect[i].y += ENEMY_PUSH_DOWN

        SCREEN.blit(enemy_pink_img[i], enemy_pink_rect[i])
        SCREEN.blit(enemy_cyan_img[i], enemy1_cyan_rect[i])
        SCREEN.blit(enemy_cyan_img[i], enemy2_cyan_rect[i])
        SCREEN.blit(enemy_green_img[i], enemy1_green_rect[i])
        SCREEN.blit(enemy_green_img[i], enemy2_green_rect[i])


def bullet(spaceship_x, spaceship_y):
    global BULLET_STATE

    BULLET_STATE = "Fire"
    SCREEN.blit(BULLET, (spaceship_x + 23, spaceship_y))


def rangeintersect(min0, max0, min1, max1):
    return (max(min0, max0) >= min(min1, max1)
            and min(min0, max0) <= max(min1, max1))


def rectintersect(r0, r1):
    return (rangeintersect(r0.x + r0.width, r1.x + r1.width)
            and r0.y + r0.height, r1.y + r1.height)


def collision():
    for i in range(NUM_OF_ENEMIES):
        if rectintersect(BULLET, enemy1_green_rect[i]):
            print("Collide")


def main():
    global BULLET_Y, BULLET_STATE

    pygame.key.set_repeat(1, 10)

    while True:
        CLOCK.tick(FPS)
        SCREEN.fill(BLACK)
        SCREEN.blit(BACKGROUND, (0, 0))

        lives_text = MAIN_FONT.render("Lives", True, WHITE)
        tiny_enemy = pygame.transform.scale(ENEMY_GREEN, (25, 25))
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
                bullet_sound = mixer.Sound(SOUND_PATH + "shoot.wav")
                bullet_sound.set_volume(0.05)
                bullet_sound.play()
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

        collision()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
