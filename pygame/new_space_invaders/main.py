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
IMAGE_PATH = BASE_PATH + "/images/"
SOUND_PATH = BASE_PATH + "/sounds/"

ICON = pygame.image.load(IMAGE_PATH + "ufo.png")
pygame.display.set_icon(ICON)

FONT = FONT_PATH + "space_invaders.ttf"
TITLE_FONT = pygame.font.Font(FONT, 50)
SUB_TITLE_FONT = pygame.font.Font(FONT, 25)
MAIN_FONT = pygame.font.Font(FONT, 20)

BACKGROUND = pygame.image.load(IMAGE_PATH + "background.jpeg")
SHIP = pygame.image.load(IMAGE_PATH + "ship.png")
BULLET = pygame.image.load(IMAGE_PATH + "laser.png")
EXPLOSION_PURPLE = pygame.image.load(IMAGE_PATH + "explosionpurple.png")
EXPLOSION_CYAN = pygame.image.load(IMAGE_PATH + "explosioncyan.png")
EXPLOSION_GREEN = pygame.image.load(IMAGE_PATH + "explosiongreen.png")
MYSTERY_IMG = pygame.image.load(IMAGE_PATH + "mystery.png")

BACKGROUND_SOUND = mixer.Sound(SOUND_PATH + "background.wav")
BULLET_SOUND = mixer.Sound(SOUND_PATH + "shoot.wav")
EXPLOSION_SOUND = mixer.Sound(SOUND_PATH + "invaderkilled.wav")
MYSTERY_SOUND = mixer.Sound(SOUND_PATH + "mysteryentered.wav")

EXPLOSION_PURPLE = pygame.transform.scale(EXPLOSION_PURPLE, (50, 40))
EXPLOSION_CYAN = pygame.transform.scale(EXPLOSION_CYAN, (50, 40))
EXPLOSION_GREEN = pygame.transform.scale(EXPLOSION_GREEN, (50, 40))
MYSTERY_IMG = pygame.transform.scale(MYSTERY_IMG, (90, 40))

ship_rect = SHIP.get_rect(topleft=(375, 540))
SHIP_SPEED = 5

NUM_OF_ENEMIES = 10
total_num_of_enemies = 50
ENEMY_PURPLE_IMG = []
ENEMY_CYAN_IMG = []
ENEMY_GREEN_IMG = []
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
x = 105

for enemy in range(NUM_OF_ENEMIES):
    x += 50
    ENEMY_PURPLE = pygame.image.load(IMAGE_PATH + "enemy1_2.png")
    ENEMY_CYAN = pygame.image.load(IMAGE_PATH + "enemy2_1.png")
    ENEMY_GREEN = pygame.image.load(IMAGE_PATH + "enemy3_1.png")

    ENEMY_PURPLE_IMG.append(pygame.transform.scale(ENEMY_PURPLE, (40, 40)))
    ENEMY_CYAN_IMG.append(pygame.transform.scale(ENEMY_CYAN, (40, 40)))
    ENEMY_GREEN_IMG.append(pygame.transform.scale(ENEMY_GREEN, (40, 40)))

    enemy_purple_rect.append(ENEMY_PURPLE_IMG[enemy].get_rect(topleft=(x, 80)))
    enemy1_cyan_rect.append(ENEMY_CYAN_IMG[enemy].get_rect(topleft=(x, 120)))
    enemy2_cyan_rect.append(ENEMY_CYAN_IMG[enemy].get_rect(topleft=(x, 160)))
    enemy1_green_rect.append(ENEMY_GREEN_IMG[enemy].get_rect(topleft=(x, 200)))
    enemy2_green_rect.append(ENEMY_GREEN_IMG[enemy].get_rect(topleft=(x, 240)))

    enemy_purple_hit.append(False)
    enemy1_cyan_hit.append(False)
    enemy2_cyan_hit.append(False)
    enemy1_green_hit.append(False)
    enemy2_green_hit.append(False)

bullet_y = 540
bullet_x = 0
bullet_rect = BULLET.get_rect(topleft=(bullet_x + 23, bullet_y))
bullet_state = "Ready"
BULLET_SPEED = 18

BUNKERS = []

MYSTERY_SPEED = 2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (210, 0, 255)
CYAN = (0, 255, 255)
GREEN = (78, 255, 87)

CLOCK = pygame.time.Clock()
FPS = 60
score = 0


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
                MYSTERY_SOUND.set_volume(0.03)
                MYSTERY_SOUND.play()
                self.mystery_entered_played = False
            if self.mystery_rect.x >= 800:
                self.mystery_rect.x = 900
            else:
                self.mystery_rect.x += MYSTERY_SPEED
                SCREEN.blit(MYSTERY_IMG, self.mystery_rect)
        if self.mystery_is_visible1:
            if self.mystery_entered_played1:
                MYSTERY_SOUND.set_volume(0.03)
                MYSTERY_SOUND.play()
                self.mystery_entered_played1 = False
            if self.mystery_rect1.x >= 800:
                self.mystery_rect1.x = 900
            else:
                self.mystery_rect1.x += MYSTERY_SPEED
                SCREEN.blit(MYSTERY_IMG, self.mystery_rect1)

    def draw_mystery(self):
        self.mystery_is_visible = False
        self.mystery_is_visible1 = False
        for v in range(NUM_OF_ENEMIES):
            if 110 <= enemy_purple_rect[v].y <= 300:
                self.mystery_is_visible = True
            if 150 <= enemy_purple_rect[v].y <= 300:
                self.mystery_is_visible1 = True

        state.show_mystery()

        if rect_intersect(bullet_rect, self.mystery_rect):
            random_point_mystery(self.mystery_rect)
        if rect_intersect(bullet_rect, self.mystery_rect1):
            random_point_mystery(self.mystery_rect1)


state = MysteryState(MYSTERY_IMG.get_rect(topleft=(-100, 40)),
                     MYSTERY_IMG.get_rect(topleft=(-100, 40)), True, True)


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
        SCREEN.blit(ENEMY_GREEN_IMG[0], (300, 265))
        SCREEN.blit(point_text_green, (350, 270))
        SCREEN.blit(ENEMY_CYAN_IMG[0], (300, 315))
        SCREEN.blit(point_text_cyan, (350, 320))
        SCREEN.blit(ENEMY_PURPLE_IMG[0], (300, 365))
        SCREEN.blit(point_text_purple, (350, 370))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()

        pygame.display.update()


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

        SCREEN.blit(ENEMY_PURPLE_IMG[i], enemy_purple_rect[i])
        SCREEN.blit(ENEMY_CYAN_IMG[i], enemy1_cyan_rect[i])
        SCREEN.blit(ENEMY_CYAN_IMG[i], enemy2_cyan_rect[i])
        SCREEN.blit(ENEMY_GREEN_IMG[i], enemy1_green_rect[i])
        SCREEN.blit(ENEMY_GREEN_IMG[i], enemy2_green_rect[i])


def enemies_collision():
    global total_num_of_enemies, bullet_state, score
    global enemy_purple_rect, enemy1_cyan_rect, \
        enemy2_cyan_rect, enemy1_green_rect, enemy2_green_rect
    global enemy_purple_hit, enemy1_cyan_hit, enemy2_cyan_hit, \
        enemy1_green_hit, enemy2_green_hit
    if bullet_state == "Fire":
        for j in range(NUM_OF_ENEMIES):
            if rect_intersect(bullet_rect, enemy_purple_rect[j]):
                SCREEN.blit(EXPLOSION_PURPLE, enemy_purple_rect[j])
                pygame.time.wait(20)
                EXPLOSION_SOUND.set_volume(0.05)
                EXPLOSION_SOUND.play()
                enemy_purple_rect[j].y = 600
                bullet_state = "Ready"
                enemy_purple_hit[j] = True
                score += 30
                total_num_of_enemies -= 1
            elif rect_intersect(bullet_rect, enemy1_cyan_rect[j]):
                SCREEN.blit(EXPLOSION_CYAN, enemy1_cyan_rect[j])
                pygame.time.wait(20)
                EXPLOSION_SOUND.set_volume(0.05)
                EXPLOSION_SOUND.play()
                enemy1_cyan_rect[j].y = 600
                bullet_state = "Ready"
                enemy1_cyan_hit[j] = True
                score += 20
                total_num_of_enemies -= 1
            elif rect_intersect(bullet_rect, enemy2_cyan_rect[j]):
                SCREEN.blit(EXPLOSION_CYAN, enemy2_cyan_rect[j])
                pygame.time.wait(20)
                EXPLOSION_SOUND.set_volume(0.05)
                EXPLOSION_SOUND.play()
                enemy2_cyan_rect[j].y = 600
                bullet_state = "Ready"
                enemy2_cyan_hit[j] = True
                score += 20
                total_num_of_enemies -= 1
            elif rect_intersect(bullet_rect, enemy1_green_rect[j]):
                SCREEN.blit(EXPLOSION_GREEN, enemy1_green_rect[j])
                pygame.time.wait(20)
                EXPLOSION_SOUND.set_volume(0.05)
                EXPLOSION_SOUND.play()
                enemy1_green_rect[j].y = 600
                bullet_state = "Ready"
                enemy1_green_hit[j] = True
                score += 10
                total_num_of_enemies -= 1
            elif rect_intersect(bullet_rect, enemy2_green_rect[j]):
                SCREEN.blit(EXPLOSION_GREEN, enemy2_green_rect[j])
                pygame.time.wait(20)
                EXPLOSION_SOUND.set_volume(0.05)
                EXPLOSION_SOUND.play()
                enemy2_green_rect[j].y = 600
                bullet_state = "Ready"
                enemy2_green_hit[j] = True
                score += 10
                total_num_of_enemies -= 1


first_bunker = []
second_bunker = []
third_bunker = []


def bunker():
    first_x = 70
    first_y = 450
    first_c = 70
    first_v = 70
    second_x = 350
    second_c = 350
    second_v = 350
    third_x = 650
    third_c = 650
    third_v = 650
    # first bunker
    # SORRY FOR THE DUPLICATE CODE, MY MODLY BRAIN WORK LINE THIS
    # TODO(jan): NEED TO FIX THIS ASAP
    for row in range(9):
        first_x += 10
        first_bunker.append(pygame.draw.rect(SCREEN, GREEN,
                            (first_x, first_y, 10, 10)))
    for column in range(4):
        first_y += 10
        first_bunker.append(pygame.draw.rect(SCREEN, GREEN,
                            (first_x, first_y, 10, 10)))
    for row in range(9):
        first_x -= 10
        first_bunker.append(pygame.draw.rect(SCREEN, GREEN,
                            (first_x, first_y, 10, 10)))
    for column in range(4):
        first_y -= 10
        first_bunker.append(pygame.draw.rect(SCREEN, GREEN,
                            (first_x, first_y, 10, 10)))
    for row in range(8):
        first_x += 10
        first_bunker.append(pygame.draw.rect(SCREEN, GREEN,
                            (first_x, 460, 10, 10)))
    for row in range(8):
        first_c += 10
        first_bunker.append(pygame.draw.rect(SCREEN, GREEN,
                            (first_c, 470, 10, 10)))
    for row in range(8):
        first_v += 10
        first_bunker.append(pygame.draw.rect(SCREEN, GREEN,
                            (first_v, 480, 10, 10)))

    # second bunker
    for row in range(9):
        second_x += 10
        second_bunker.append(pygame.draw.rect(SCREEN, GREEN,
                             (second_x, first_y, 10, 10)))
    for column in range(4):
        first_y += 10
        second_bunker.append(pygame.draw.rect(SCREEN, GREEN,
                             (second_x, first_y, 10, 10)))
    for row in range(9):
        second_x -= 10
        second_bunker.append(pygame.draw.rect(SCREEN, GREEN,
                             (second_x, first_y, 10, 10)))
    for column in range(4):
        first_y -= 10
        second_bunker.append(pygame.draw.rect(SCREEN, GREEN,
                             (second_x, first_y, 10, 10)))
    for row in range(8):
        second_x += 10
        second_bunker.append(pygame.draw.rect(SCREEN, GREEN,
                             (second_x, 460, 10, 10)))
    for row in range(8):
        second_c += 10
        second_bunker.append(pygame.draw.rect(SCREEN, GREEN,
                             (second_c, 470, 10, 10)))
    for row in range(8):
        second_v += 10
        second_bunker.append(pygame.draw.rect(SCREEN, GREEN,
                             (second_v, 480, 10, 10)))

    # third bunker
    for row in range(9):
        third_x += 10
        third_bunker.append(pygame.draw.rect(SCREEN, GREEN,
                            (third_x, first_y, 10, 10)))
    for column in range(4):
        first_y += 10
        third_bunker.append(pygame.draw.rect(SCREEN, GREEN,
                            (third_x, first_y, 10, 10)))
    for row in range(9):
        third_x -= 10
        third_bunker.append(pygame.draw.rect(SCREEN, GREEN,
                            (third_x, first_y, 10, 10)))
    for column in range(4):
        first_y -= 10
        third_bunker.append(pygame.draw.rect(SCREEN, GREEN,
                            (third_x, first_y, 10, 10)))
    for row in range(8):
        third_x += 10
        third_bunker.append(pygame.draw.rect(SCREEN, GREEN,
                            (third_x, 460, 10, 10)))
    for row in range(8):
        third_c += 10
        third_bunker.append(pygame.draw.rect(SCREEN, GREEN,
                            (third_c, 470, 10, 10)))
    for row in range(8):
        third_v += 10
        third_bunker.append(pygame.draw.rect(SCREEN, GREEN,
                            (third_v, 480, 10, 10)))


def bunker_collision():
    global bullet_state
    if bullet_state == "Fire":
        for k in range(9):
            if rect_intersect(bullet_rect, first_bunker[k]):
                bullet_state = "Ready"
                first_bunker[k].y = 600
                first_bunker[k].x = 600
                print("Collide")
        for k in range(9):
            if rect_intersect(bullet_rect, second_bunker[k]):
                bullet_state = "Ready"
                second_bunker[k].y = 600
                second_bunker[k].x = 600
                print("Collide")
        for k in range(9):
            if rect_intersect(bullet_rect, third_bunker[k]):
                bullet_state = "Ready"
                third_bunker[k].y = 600
                third_bunker[k].x = 600
                print("Collide")


def bullet(spaceship_x, spaceship_y):
    global bullet_state
    bullet_state = "Fire"
    SCREEN.blit(BULLET, (spaceship_x + 23, spaceship_y))


def rect_intersect(rect_zero, rect_one):
    return rect_zero.colliderect(rect_one)


def draw_gameover():
    SCREEN.blit(BACKGROUND, (0, 0))
    gameover_text = TITLE_FONT.render("Game Over", True, WHITE)
    SCREEN.blit(gameover_text, (250, 250))
    BACKGROUND_SOUND.stop()
    BULLET_SOUND.stop()


def is_gameover():
    global total_num_of_enemies
    if total_num_of_enemies == 0:
        return True
    return False


def is_enemy_hit_ship():
    global enemy_purple_hit, enemy1_cyan_hit, enemy2_cyan_hit, \
        enemy1_green_hit, enemy2_green_rect
    for i in range(NUM_OF_ENEMIES):
        if (enemy_purple_rect[i].y >= 410 and enemy_purple_hit[i] is not True
            or enemy1_cyan_rect[i].y >= 410 and enemy1_cyan_hit[i] is not True
            or enemy2_cyan_rect[i].y >= 410 and enemy2_cyan_hit[i] is not True
            or enemy1_green_rect[i].y >= 410 and enemy1_green_hit[i] is not
            True or enemy2_green_rect[i].y >= 410 and enemy2_green_hit[i] is
                not True):
            return True
    return False


def random_point_mystery(m_rect):
    global score
    random_point = random.randint(1, 6) * 50
    point_text = MAIN_FONT.render(str(random_point), True, WHITE)
    m_rect.x += 23
    pygame.time.wait(20)
    SCREEN.blit(point_text, m_rect)
    m_rect.x = 900
    score += random_point


def main():
    global bullet_y, bullet_state, bullet_rect, bullet_x
    pygame.key.set_repeat(1, 10)
    BACKGROUND_SOUND.set_volume(0.5)
    BACKGROUND_SOUND.play(-1)

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

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and ship_rect.x > 10:
            ship_rect.x -= SHIP_SPEED
        if keys[pygame.K_RIGHT] and ship_rect.x < 740:
            ship_rect.x += SHIP_SPEED
        if keys[pygame.K_SPACE]:
            if bullet_state == "Ready":
                bullet_y = 540
                BULLET_SOUND.set_volume(0.05)
                BULLET_SOUND.play()
                bullet_x = ship_rect.x
                bullet(bullet_x, bullet_y)
        SCREEN.blit(SHIP, ship_rect)

        if bullet_y <= 0:
            bullet_y = 540
            bullet_state = "Ready"
        if bullet_state == "Fire":
            bullet(bullet_x, bullet_y)
            bullet_y -= BULLET_SPEED
        bullet_rect = BULLET.get_rect(topleft=(bullet_x + 23, bullet_y))

        draw_enemies()
        bunker()
        enemies_collision()
        bunker_collision()
        state.draw_mystery()

        if is_gameover():
            draw_gameover()
        elif is_enemy_hit_ship():
            draw_gameover()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
