"""All the imports use in game"""
import sys
from os.path import abspath, dirname
import pygame

pygame.init()

# Create screen
SCREEN = pygame.display.set_mode((800, 600))

# Caption
pygame.display.set_caption("Space Invaders")

# Path
BASE_PATH = abspath(dirname(__file__))

# Font
FONT_PATH = BASE_PATH + "/fonts/"
FONT = FONT_PATH + "space_invaders.ttf"
TITLE_FONT = pygame.font.Font(FONT, 50)
SUB_TITLE_FONT = pygame.font.Font(FONT, 25)
MAIN_FONT = pygame.font.Font(FONT, 20)

# Image and sound
IMAGE_PATH = BASE_PATH + "/images/"
SOUND_PATH = BASE_PATH + "/sounds/"

# Icon
ICON = pygame.image.load(IMAGE_PATH + "ufo.png")
pygame.display.set_icon(ICON)

# Background image
BACKGROUND = pygame.image.load(IMAGE_PATH + "background.jpeg")

# Ship
SHIP = pygame.image.load(IMAGE_PATH + "ship.png")
SHIP_RECT = SHIP.get_rect(topleft=(375, 540))
SHIP_SPEED = 5

# Enemy1
NUM_OF_ENEMIES = 10
ENEMY1_IMG = []
ENEMY1_RECT = []
ENEMY2_RECT = []
ENEMY_SPEED = []
ENEMY_PUSH_DOWN = []
X = 115

for enemies in range(NUM_OF_ENEMIES):
    X += 50
    ENEMY1 = (pygame.image.load(IMAGE_PATH + "enemy3_1.png"))
    # Resize enemy1
    ENEMY1_IMG.append(pygame.transform.scale(ENEMY1, (40, 40)))
    ENEMY1_RECT.append(ENEMY1_IMG[enemies].get_rect(topleft=(X, 200)))
    ENEMY2_RECT.append(ENEMY1_IMG[enemies].get_rect(topleft=(X, 300)))
    ENEMY_SPEED.append(2)
    ENEMY_PUSH_DOWN.append(40)

# Bullet
BULLET = pygame.image.load(IMAGE_PATH + "laser.png")

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (78, 255, 87)

# Game variables
CLOCK = pygame.time.Clock()
FPS = 60


def main_menu():
    """Main Menu for Space Invaders"""
    while True:
        CLOCK.tick(FPS)

        title_text = TITLE_FONT.render("Space Invaders", True, WHITE)
        title_text2 = SUB_TITLE_FONT.render("Press enter to continue", True, WHITE)

        # Enemy points
        point_text = SUB_TITLE_FONT.render("   =   10 pts", True, GREEN)

        # Drawing with positions
        SCREEN.blit(BACKGROUND, (0, 0))

        SCREEN.blit(title_text, (164, 155))
        SCREEN.blit(title_text2, (201, 225))

        SCREEN.blit(ENEMY1_IMG[0], (318, 270))
        SCREEN.blit(point_text, (368, 270))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()

        pygame.display.update()


def draw_enemies():
    """Display the enemies"""
    # Enemy movement
    for i in range(NUM_OF_ENEMIES):
        ENEMY1_RECT[i].x += ENEMY_SPEED[i]
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
            ENEMY2_RECT[i].y += ENEMY_PUSH_DOWN[i]

        SCREEN.blit(ENEMY1_IMG[i], ENEMY1_RECT[i])
        SCREEN.blit(ENEMY1_IMG[i], ENEMY2_RECT[i])


def bullet(spaceship_x, spaceship_y):
    """bullet state"""
    bullet_y = 540
    bullet_y -= 15
    SCREEN.blit(BULLET, (spaceship_x + 23, spaceship_y))


def main():
    """Game loop"""
    pygame.key.set_repeat(1, 10)

    while True:
        CLOCK.tick(FPS)

        SCREEN.fill(BLACK)

        # Drawing with positions
        SCREEN.blit(BACKGROUND, (0, 0))

        # Lives
        lives_text = MAIN_FONT.render("Lives", True, WHITE)
        # Resize enemy1 next to lives
        tiny_enemy1 = pygame.transform.scale(ENEMY1, (25, 25))

        score_text = MAIN_FONT.render("Score", True, WHITE)
        score_text_num = MAIN_FONT.render("0", True, GREEN)

        # Drawing with positions
        SCREEN.blit(lives_text, (640, 5))
        SCREEN.blit(tiny_enemy1, (715, 3))
        SCREEN.blit(tiny_enemy1, (742, 3))
        SCREEN.blit(tiny_enemy1, (769, 3))

        SCREEN.blit(score_text, (5, 5))
        SCREEN.blit(score_text_num, (85, 5))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and SHIP_RECT.x > 10:
            SHIP_RECT.x -= SHIP_SPEED
        if keys[pygame.K_RIGHT] and SHIP_RECT.x < 740:
            SHIP_RECT.x += SHIP_SPEED
        if keys[pygame.K_SPACE]:
            bullet(SHIP_RECT.x, SHIP_RECT.y)

        SCREEN.blit(SHIP, SHIP_RECT)

        draw_enemies()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
