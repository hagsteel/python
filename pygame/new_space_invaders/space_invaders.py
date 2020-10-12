import pygame
from os.path import abspath, dirname
import sys

pygame.init()

BASE_PATH = abspath(dirname(__file__))
FONT_PATH = BASE_PATH + "/fonts/"
IMAGE_PATH = BASE_PATH + "/images/"
SOUND_PATH = BASE_PATH + "/sounds/"
FONT = FONT_PATH + "space_invaders.ttf"

TITLE_FONT = pygame.font.Font(FONT, 50)
SUB_TITLE_FONT = pygame.font.Font(FONT, 25)

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((800, 600))
IMG_NAMES = ["ship", "enemy1"]
IMAGES = {name: pygame.image.load(IMAGE_PATH + "{}.png".format(name)) for name in IMG_NAMES}

def main_menu():
    screen.fill(BLACK)
    
    BACKGROUND = pygame.image.load(IMAGE_PATH + "background.jpeg")
    titletext = TITLE_FONT.render("Space Invaders", True, WHITE)
    titletext2 = SUB_TITLE_FONT.render("Press any key to continue", True, WHITE)

    screen.blit(BACKGROUND, (0, 0))
    screen.blit(titletext, (164, 155))
    screen.blit(titletext2, (201, 225))


def text():
    Text(FONT, 50)

def main():
    clock = pygame.time.Clock()
    clock.tick(60)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        main_menu()


if __name__ == "__main__":
    main()
