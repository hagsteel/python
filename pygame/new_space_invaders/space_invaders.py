import pygame
from os.path import abspath, dirname
import sys

pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))

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
clock = pygame.time.Clock()
fps = 60


def main_menu():
    while True:
        clock.tick(fps)

        TITLETEXT = TITLE_FONT.render("Space Invaders", True, WHITE)
        TITLETEXT2 = SUB_TITLE_FONT.render("Press enter to continue", True, WHITE)

        # Enemy1 image
        enemy1 = pygame.image.load(IMAGE_PATH + "enemy1.png")
        # Resize enemy1
        enemy1 = pygame.transform.scale(enemy1, (40, 40))
        # Enemy points
        pointtext = SUB_TITLE_FONT.render("   =   10 pts", True, GREEN)

        # Drawing with positions
        screen.blit(BACKGROUND, (0, 0))
        screen.blit(TITLETEXT, (164, 155))
        screen.blit(TITLETEXT2, (201, 225))
        screen.blit(enemy1, (318, 270))
        screen.blit(pointtext, (368, 270))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()

        pygame.display.update()


def main():
    global ship_rect, ship_speed

    while True:
        clock.tick(fps)

        screen.fill(BLACK)

        # Drawing with positions
        screen.blit(BACKGROUND, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ship_rect.x -= ship_speed
                if event.key == pygame.K_RIGHT:
                    ship_rect.x += ship_speed

        screen.blit(SHIP, ship_rect)
        print(ship_rect.x)

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
