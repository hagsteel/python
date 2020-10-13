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

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (78, 255, 87)

def main_menu():
    
    # Background image
    BACKGROUND = pygame.image.load(IMAGE_PATH + "background.jpeg")

    titletext = TITLE_FONT.render("Space Invaders", True, WHITE)
    titletext2 = SUB_TITLE_FONT.render("Press any key to continue", True, WHITE)

    # Enemy1 image
    enemy1 = pygame.image.load(IMAGE_PATH + "enemy1.png")
    # Resize enemy1
    enemy1 = pygame.transform.scale(enemy1, (40, 40))

    # Points
    pointtext = SUB_TITLE_FONT.render("   =   10 pts", True, GREEN)

    screen.blit(BACKGROUND, (0, 0))
    screen.blit(titletext, (164, 155))
    screen.blit(titletext2, (201, 225))
    screen.blit(enemy1, (318, 270))
    screen.blit(pointtext, (368, 270))


def main():
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        main_menu()

        pygame.display.update()


if __name__ == "__main__":
    main()
