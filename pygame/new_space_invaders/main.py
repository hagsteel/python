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

explosion_sound = mixer.Sound(SOUND_PATH + "invaderkilled.wav")
explosion_purple = pygame.image.load(IMAGE_PATH + "explosionpurple.png")
explosion_cyan = pygame.image.load(IMAGE_PATH + "explosioncyan.png")
explosion_green = pygame.image.load(IMAGE_PATH + "explosiongreen.png")
explosion_purple = pygame.transform.scale(explosion_purple, (50, 40))
explosion_cyan = pygame.transform.scale(explosion_cyan, (50, 40))
explosion_green = pygame.transform.scale(explosion_green, (50, 40))

NUM_OF_ENEMIES = 10
enemy_purple_img = []
enemy_cyan_img = []
enemy_green_img = []
enemy_purple_rect = []
enemy1_cyan_rect = []
enemy2_cyan_rect = []
enemy1_green_rect = []
enemy2_green_rect = []
ENEMY_SPEED = 1
ENEMY_PUSH_DOWN = 10
X = 105

for enemy in range(NUM_OF_ENEMIES):
    X += 50
    ENEMY_PURPLE = pygame.image.load(IMAGE_PATH + "enemy1_2.png")
    ENEMY_CYAN = pygame.image.load(IMAGE_PATH + "enemy2_1.png")
    ENEMY_GREEN = pygame.image.load(IMAGE_PATH + "enemy3_1.png")

    enemy_purple_img.append(pygame.transform.scale(ENEMY_PURPLE, (40, 40)))
    enemy_cyan_img.append(pygame.transform.scale(ENEMY_CYAN, (40, 40)))
    enemy_green_img.append(pygame.transform.scale(ENEMY_GREEN, (40, 40)))

    enemy_purple_rect.append(enemy_purple_img[enemy].get_rect(topleft=(X, 60)))
    enemy1_cyan_rect.append(enemy_cyan_img[enemy].get_rect(topleft=(X, 100)))
    enemy2_cyan_rect.append(enemy_cyan_img[enemy].get_rect(topleft=(X, 140)))
    enemy1_green_rect.append(enemy_green_img[enemy].get_rect(topleft=(X, 180)))
    enemy2_green_rect.append(enemy_green_img[enemy].get_rect(topleft=(X, 220)))

BULLET = pygame.image.load(IMAGE_PATH + "laser.png")
BULLET_STATE = "Ready"
BULLET_Y = 540
BULLET_X = 0
BULLET_SPEED = 18
BULLET_RECT = BULLET.get_rect(topleft=(BULLET_X + 23, BULLET_Y))

bunkers = []

mystery = pygame.image.load(IMAGE_PATH + "mystery.png")
mystery = pygame.transform.scale(mystery, (90, 40))
mystery_rect = mystery.get_rect(topleft=(0, 40))
mystery_speed = 2
mystery_entered_played = True

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (210, 0, 255)
CYAN = (0, 255, 255)
GREEN = (78, 255, 87)

# Game variables
CLOCK = pygame.time.Clock()
FPS = 60


def main_menu():
    while True:
        CLOCK.tick(FPS)

        title_text = TITLE_FONT.render("Space Invaders", True, WHITE)
        title_text2 = SUB_TITLE_FONT.render("Press enter to continue", True, WHITE)
        point_text_green = SUB_TITLE_FONT.render("   =   10 pts", True, GREEN)
        point_text_cyan = SUB_TITLE_FONT.render("   =   10 pts", True, CYAN)
        point_text_purple = SUB_TITLE_FONT.render("   =   10 pts", True, PURPLE)

        SCREEN.blit(BACKGROUND, (0, 0))
        SCREEN.blit(title_text, (164, 155))
        SCREEN.blit(title_text2, (201, 225))
        SCREEN.blit(enemy_green_img[0], (300, 265))
        SCREEN.blit(point_text_green, (350, 270))
        SCREEN.blit(enemy_cyan_img[0], (300, 315))
        SCREEN.blit(point_text_cyan, (350, 320))
        SCREEN.blit(enemy_purple_img[0], (300, 365))
        SCREEN.blit(point_text_purple, (350, 370))

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
    bunkers.append(pygame.draw.rect(SCREEN, GREEN, (70, y_axis, width, height)))
    bunkers.append(pygame.draw.rect(SCREEN, GREEN, (350, y_axis, width, height)))
    bunkers.append(pygame.draw.rect(SCREEN, GREEN, (650, y_axis, width, height)))


def draw_enemies():
    global ENEMY_SPEED

    for num in enemy_purple_rect:
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
        for num in enemy_purple_rect:
            if num.x <= 1:
                ENEMY_SPEED = 1
                enemy_purple_rect[i].y += ENEMY_PUSH_DOWN
            elif num.x >= 755:
                ENEMY_SPEED = -0.5
                enemy_purple_rect[i].y += ENEMY_PUSH_DOWN
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

        SCREEN.blit(enemy_purple_img[i], enemy_purple_rect[i])
        SCREEN.blit(enemy_cyan_img[i], enemy1_cyan_rect[i])
        SCREEN.blit(enemy_cyan_img[i], enemy2_cyan_rect[i])
        SCREEN.blit(enemy_green_img[i], enemy1_green_rect[i])
        SCREEN.blit(enemy_green_img[i], enemy2_green_rect[i])


def bullet(spaceship_x, spaceship_y):
    global BULLET_STATE

    BULLET_STATE = "Fire"
    SCREEN.blit(BULLET, (spaceship_x + 23, spaceship_y))


def rect_intersect(rect_zero, rect_one):
    return rect_zero.colliderect(rect_one)


def enemies_collision():
    global BULLET_STATE

    if BULLET_STATE == "Fire":
        for j in range(NUM_OF_ENEMIES):
            if rect_intersect(BULLET_RECT, enemy_purple_rect[j]):
                SCREEN.blit(explosion_purple, enemy_purple_rect[j])
                pygame.time.wait(20)
                explosion_sound.set_volume(0.05)
                explosion_sound.play()
                enemy_purple_rect[j].y = 600
                BULLET_STATE = "Ready"
            elif rect_intersect(BULLET_RECT, enemy1_cyan_rect[j]):
                SCREEN.blit(explosion_cyan, enemy1_cyan_rect[j])
                pygame.time.wait(20)
                explosion_sound.set_volume(0.05)
                explosion_sound.play()
                enemy1_cyan_rect[j].y = 600
                BULLET_STATE = "Ready"
            elif rect_intersect(BULLET_RECT, enemy2_cyan_rect[j]):
                SCREEN.blit(explosion_cyan, enemy2_cyan_rect[j])
                pygame.time.wait(20)
                explosion_sound.set_volume(0.05)
                explosion_sound.play()
                enemy2_cyan_rect[j].y = 600
                BULLET_STATE = "Ready"
            elif rect_intersect(BULLET_RECT, enemy1_green_rect[j]):
                SCREEN.blit(explosion_green, enemy1_green_rect[j])
                pygame.time.wait(20)
                explosion_sound.set_volume(0.05)
                explosion_sound.play()
                enemy1_green_rect[j].y = 600
                BULLET_STATE = "Ready"
            elif rect_intersect(BULLET_RECT, enemy2_green_rect[j]):
                SCREEN.blit(explosion_green, enemy2_green_rect[j])
                pygame.time.wait(20)
                explosion_sound.set_volume(0.05)
                explosion_sound.play()
                enemy2_green_rect[j].y = 600
                BULLET_STATE = "Ready"


def bunker_collision():
    for k in range(3):
        if rect_intersect(BULLET_RECT, bunkers[k]):
            print("Collide")


def draw_mystery():
    global mystery_entered_played

    mystery_is_visible = False
    for v in range(NUM_OF_ENEMIES):
        if enemy_purple_rect[v].y >= 90:
            mystery_is_visible = True
    if mystery_is_visible:
        mystery_entered = mixer.Sound(SOUND_PATH + "mysteryentered.wav")
        if mystery_entered_played:
            mystery_entered.set_volume(0.03)
            mystery_entered.play()
            mystery_entered_played = False
        mystery_rect.x += mystery_speed
        SCREEN.blit(mystery, mystery_rect)


def main():
    global BULLET_Y, BULLET_STATE, BULLET_RECT, BULLET_X

    pygame.key.set_repeat(1, 10)

    background_sound = mixer.Sound(SOUND_PATH + "background.wav")
    background_sound.set_volume(0.5)
    background_sound.play(-1)

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
                BULLET_Y = 540
                bullet_sound = mixer.Sound(SOUND_PATH + "shoot.wav")
                bullet_sound.set_volume(0.05)
                bullet_sound.play()
                BULLET_X = SHIP_RECT.x
                bullet(BULLET_X, BULLET_Y)
        SCREEN.blit(SHIP, SHIP_RECT)

        # Bullet movement
        if BULLET_Y <= 0:
            BULLET_Y = 540
            BULLET_STATE = "Ready"
        if BULLET_STATE == "Fire":
            bullet(BULLET_X, BULLET_Y)
            BULLET_Y -= BULLET_SPEED

        BULLET_RECT = BULLET.get_rect(topleft=(BULLET_X + 23, BULLET_Y))
        enemies_collision()
        bunker_collision()

        draw_mystery()

        # print(enemy_purple_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
