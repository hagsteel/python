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
ship_rect = SHIP.get_rect(topleft=(375, 540))
ship_speed = 5

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

        # Enemy1 image
        enemy1 = pygame.image.load(IMAGE_PATH + "enemy1.png")
        # Resize enemy1
        enemy1 = pygame.transform.scale(enemy1, (40, 40))
        # Enemy points
        point_text = SUB_TITLE_FONT.render("   =   10 pts", True, GREEN)

        # Drawing with positions
        SCREEN.blit(BACKGROUND, (0, 0))
        SCREEN.blit(title_text, (164, 155))
        SCREEN.blit(title_text2, (201, 225))
        SCREEN.blit(enemy1, (318, 270))
        SCREEN.blit(point_text, (368, 270))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()

        pygame.display.update()


left_down = False
right_down = False
pygame.key.set_repeat(1, 10)


def main():
    global ship_rect, ship_speed, left_down, right_down

    while True:
        CLOCK.tick(FPS)

        SCREEN.fill(BLACK)

        # Drawing with positions
        SCREEN.blit(BACKGROUND, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                ship_rect.x -= ship_speed
            if keys[pygame.K_RIGHT]:
                ship_rect.x += ship_speed

        SCREEN.blit(SHIP, ship_rect)

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
