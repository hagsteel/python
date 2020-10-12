from pygame import *
from os.path import abspath, dirname

BASE_PATH = abspath(dirname(__file__))
print(abspath(dirname(__file__)))
FONT_PATH = BASE_PATH + "/fonts/"

class SpaceInvaders:
    def __init__(self):
        init()
        pass
