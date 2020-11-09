import random
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
enemy_purple_hit = []
enemy1_cyan_hit = []
enemy2_cyan_hit = []
enemy1_green_hit = []
enemy2_green_hit = []
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

    enemy_purple_rect.append(enemy_purple_img[enemy].get_rect(topleft=(X, 80)))
    enemy1_cyan_rect.append(enemy_cyan_img[enemy].get_rect(topleft=(X, 120)))
    enemy2_cyan_rect.append(enemy_cyan_img[enemy].get_rect(topleft=(X, 160)))
    enemy1_green_rect.append(enemy_green_img[enemy].get_rect(topleft=(X, 200)))
    enemy2_green_rect.append(enemy_green_img[enemy].get_rect(topleft=(X, 240)))

    enemy_purple_hit.append(False)
    enemy1_cyan_hit.append(False)
    enemy2_cyan_hit.append(False)
    enemy1_green_hit.append(False)
    enemy2_green_hit.append(False)

BULLET = pygame.image.load(IMAGE_PATH + "laser.png")
BULLET_STATE = "Ready"
BULLET_Y = 540
BULLET_X = 0
BULLET_SPEED = 18
BULLET_RECT = BULLET.get_rect(topleft=(BULLET_X + 23, BULLET_Y))

bunkers = []

score = 0

mystery = pygame.image.load(IMAGE_PATH + "mystery.png")
mystery_entered = mixer.Sound(SOUND_PATH + "mysteryentered.wav")
mystery = pygame.transform.scale(mystery, (90, 40))
MYSTERY_SPEED = 2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (210, 0, 255)
CYAN = (0, 255, 255)
GREEN = (78, 255, 87)

CLOCK = pygame.time.Clock()
FPS = 60


class MysteryState:
    def __init__(self, mystery_rect, mystery_rect1, mystery_entered_played,
                 mystery_entered_played1):
        self.mystery_rect = mystery_rect
        self.mystery_rect1 = mystery_rect1
        self.mystery_entered_played = mystery_entered_played
        self.mystery_entered_played1 = mystery_entered_played1

    def show_mystery(self):
        if self.mystery_is_visible:
            if self.mystery_entered_played:
                mystery_entered.set_volume(0.03)
                mystery_entered.play()
                self.mystery_entered_played = False
            if self.mystery_rect.x >= 800:
                self.mystery_rect.x = 900
            else:
                self.mystery_rect.x += MYSTERY_SPEED
                SCREEN.blit(mystery, self.mystery_rect)
        if self.mystery_is_visible1:
            if self.mystery_entered_played1:
                mystery_entered.set_volume(0.03)
                mystery_entered.play()
                self.mystery_entered_played1 = False
            if self.mystery_rect1.x >= 800:
                self.mystery_rect1.x = 900
            else:
                self.mystery_rect1.x += MYSTERY_SPEED
                SCREEN.blit(mystery, self.mystery_rect1)

    def draw_mystery(self):
        self.mystery_is_visible = False
        self.mystery_is_visible1 = False
        for v in range(NUM_OF_ENEMIES):
            if enemy_purple_rect[v].y >= 110 and enemy_purple_rect[v].y <= 300:
                self.mystery_is_visible = True
            if enemy_purple_rect[v].y >= 150 and enemy_purple_rect[v].y <= 300:
                self.mystery_is_visible1 = True

        state.show_mystery()

        if rect_intersect(BULLET_RECT, self.mystery_rect):
            random_point_mystery(self.mystery_rect)
        if rect_intersect(BULLET_RECT, self.mystery_rect1):
            random_point_mystery(self.mystery_rect1)


state = MysteryState(mystery.get_rect(topleft=(-100, 40)),
                     mystery.get_rect(topleft=(-100, 40)), True, True)


def main_menu():
    while True:
        CLOCK.tick(FPS)

        title_text = TITLE_FONT.render("Space Invaders", True, WHITE)
        title_text2 = SUB_TITLE_FONT.render("Press enter to continue", True,
                                            WHITE)
        point_text_green = SUB_TITLE_FONT.render("   =   10 pts", True, GREEN)
        point_text_cyan = SUB_TITLE_FONT.render("   =   20 pts", True, CYAN)
        point_text_purple = SUB_TITLE_FONT.render("   =   30 pts", True,
                                                  PURPLE)

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
    bunkers.append(
        pygame.draw.rect(SCREEN, GREEN, (70, y_axis, width, height)))
    bunkers.append(
        pygame.draw.rect(SCREEN, GREEN, (350, y_axis, width, height)))
    bunkers.append(
        pygame.draw.rect(SCREEN, GREEN, (650, y_axis, width, height)))


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
    global BULLET_STATE, score, enemy_purple_rect, enemy1_cyan_rect
    global enemy2_cyan_rect, enemy1_green_rect, enemy2_green_rect
    global enemy_purple_hit, enemy1_cyan_hit, enemy2_cyan_hit, enemy1_green_hit, enemy2_green_hit
    if BULLET_STATE == "Fire":
        for j in range(NUM_OF_ENEMIES):
            if rect_intersect(BULLET_RECT, enemy_purple_rect[j]):
                SCREEN.blit(explosion_purple, enemy_purple_rect[j])
                pygame.time.wait(20)
                explosion_sound.set_volume(0.05)
                explosion_sound.play()
                enemy_purple_rect[j].y = 600
                BULLET_STATE = "Ready"
                enemy_purple_hit[j] = True
                score += 30
            elif rect_intersect(BULLET_RECT, enemy1_cyan_rect[j]):
                SCREEN.blit(explosion_cyan, enemy1_cyan_rect[j])
                pygame.time.wait(20)
                explosion_sound.set_volume(0.05)
                explosion_sound.play()
                enemy1_cyan_rect[j].y = 600
                BULLET_STATE = "Ready"
                enemy1_cyan_hit[j] = True
                score += 20
            elif rect_intersect(BULLET_RECT, enemy2_cyan_rect[j]):
                SCREEN.blit(explosion_cyan, enemy2_cyan_rect[j])
                pygame.time.wait(20)
                explosion_sound.set_volume(0.05)
                explosion_sound.play()
                enemy2_cyan_rect[j].y = 600
                BULLET_STATE = "Ready"
                enemy2_cyan_hit[j] = True
                score += 20
            elif rect_intersect(BULLET_RECT, enemy1_green_rect[j]):
                SCREEN.blit(explosion_green, enemy1_green_rect[j])
                pygame.time.wait(20)
                explosion_sound.set_volume(0.05)
                explosion_sound.play()
                enemy1_green_rect[j].y = 600
                BULLET_STATE = "Ready"
                enemy1_green_hit[j] = True
                score += 10
            elif rect_intersect(BULLET_RECT, enemy2_green_rect[j]):
                SCREEN.blit(explosion_green, enemy2_green_rect[j])
                pygame.time.wait(20)
                explosion_sound.set_volume(0.05)
                explosion_sound.play()
                enemy2_green_rect[j].y = 600
                BULLET_STATE = "Ready"
                enemy2_green_hit[j] = True
                score += 10


def is_gameover():
    global enemy_purple_hit, enemy1_cyan_hit, enemy2_cyan_hit, enemy1_green_hit
    global enemy2_green_hit
    for i in range(NUM_OF_ENEMIES):
        if (enemy_purple_hit[i] is not True
           or enemy1_cyan_hit[i] is not True
           or enemy2_cyan_hit[i] is not True
           or enemy1_green_hit[i] is not True
           or enemy2_green_hit[i] is not True):
            return False
        else:
            return True
    # global score
    # if score >= 900:
    #     return True
    # return False


def is_enemy_hit_ship():
    global enemy_purple_hit, enemy1_cyan_hit, enemy2_cyan_hit, enemy1_green_hit
    global enemy2_green_rect
    for i in range(NUM_OF_ENEMIES):
        if (enemy_purple_rect[i].y >= 410 and enemy_purple_hit[i] is not True
           or enemy1_cyan_rect[i].y >= 410 and enemy1_cyan_hit[i] is not True
           or enemy2_cyan_rect[i].y >= 410 and enemy2_cyan_hit[i] is not True
           or enemy1_green_rect[i].y >= 410 and enemy1_green_hit[i] is not True
           or enemy2_green_rect[i].y >= 410 and enemy2_green_hit[i] is not True):
            return True
    return False


def bunker_collision():
    for k in range(3):
        if rect_intersect(BULLET_RECT, bunkers[k]):
            pass
            # print("Collide")


def random_point_mystery(m_rect):
    global score
    random_point = random.randint(1, 6) * 50
    point_text = MAIN_FONT.render(str(random_point), True, WHITE)
    m_rect.x += 23
    SCREEN.blit(point_text, m_rect)
    m_rect.x = 900
    score += random_point


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
        score_text_num = MAIN_FONT.render(str(score), True, GREEN)

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
        state.draw_mystery()

        if is_gameover():
            SCREEN.blit(BACKGROUND, (0, 0))
            gameover_text = TITLE_FONT.render("Game Over", True, WHITE)
            SCREEN.blit(gameover_text, (250, 250))
            background_sound.stop()
            break

        if is_enemy_hit_ship():
            SCREEN.blit(BACKGROUND, (0, 0))
            gameover_text = TITLE_FONT.render("Game Over", True, WHITE)
            SCREEN.blit(gameover_text, (250, 250))
            background_sound.stop()
            break

        print(is_gameover())
        print(enemy_purple_hit)
        print(enemy1_cyan_hit)
        print(enemy2_cyan_hit)
        print(enemy1_green_hit)
        print(enemy2_green_hit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
