from pygame import *
from os.path import abspath, dirname
import sys

BASE_PATH = abspath(dirname(__file__))
FONT_PATH = BASE_PATH + "/fonts/"
IMAGE_PATH = BASE_PATH + "/images/"
SOUND_PATH = BASE_PATH + "/sounds/"

SCREEN = display.set_mode((800, 600))
IMG_NAMES = ["ship", "enemy1"]
IMAGES = {name: image.load(IMAGE_PATH + "{}.png".format(name)) for name in IMG_NAMES}

class Ship:
    def __init__(self):
        self.image = IMAGES['ship']
        self.rect = self.image.get_rect(topleft=(375, 540))

class SpaceInvaders:
    def __init__(self):
        init()
        self.clock = time.Clock()
        self.caption = display.set_caption("Space Invaders")
        self.screen = SCREEN
        self.background = image.load(IMAGE_PATH + "background.jpeg")

    def should_exit(evt):
        return evt.type == QUIT

    def check_input(self):
        for event in event.get():
            if self.should_exit(event):
                sys.exit()

if __name__ == "__main__":
    while True:
        SpaceInvaders()
