import pygame
from os.path import abspath, dirname
import sys

pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))

# Caption
pygame.display.set_caption("Space Invaders")

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

IMG_NAMES = ["ship", "enemy1"]
IMAGES = {name: pygame.image.load(IMAGE_PATH + "{}.png".format(name)) for name in IMG_NAMES}


def main_menu():
    
    BACKGROUND = pygame.image.load(IMAGE_PATH + "background.jpeg")
    titletext = TITLE_FONT.render("Space Invaders", True, WHITE)
    titletext2 = SUB_TITLE_FONT.render("Press any key to continue", True, WHITE)

    screen.blit(BACKGROUND, (0, 0))
    screen.blit(titletext, (164, 155))
    screen.blit(titletext2, (201, 225))


def main():
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        main_menu()


if __name__ == "__main__":
    main()
