import math
import os.path
import random
import sys
from os.path import abspath, dirname

import pygame
from pygame import mixer

pygame.init()

# Create the screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Path
project_directory = os.path.dirname(__file__)
BASE_PATH = abspath(dirname(__file__))

# Background
back_image = pygame.image.load(os.path.join(project_directory, "img/background.jpeg"))

# Resize
back_image = pygame.transform.scale(back_image, (WIDTH, HEIGHT))

# Background sound
pygame.mixer.music.load(os.path.join(project_directory, "sound/back.wav"))
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption('Space Invaders')
ICON = pygame.image.load(os.path.join(project_directory, "img/vr-gaming.png"))
pygame.display.set_icon(ICON)

# Player
player_img = pygame.image.load(os.path.join(project_directory, "img/space-invaders.png"))
player_x = 370
player_y = 480
player_x_change = 5

# Enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 7

for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load(os.path.join(project_directory, "img/enemy.png")))
    enemy_x.append(random.randint(0, 735))
    enemy_y.append(random.randint(50, 150))
    # Speed
    enemy_x_change.append(3.5)
    # Push down
    enemy_y_change.append(40)

# Bullet
bullet_img = pygame.image.load(os.path.join(project_directory, "img/bullet.png"))
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 15
bullet_state = 'Ready'

# Score
score = 0
font = BASE_PATH + "/font/arcadeclassic.ttf"
score_font = pygame.font.Font(font, 32)
text_x = 10
text_y = 10

# Game over
over_font = pygame.font.Font(font, 70)

# Global
CLOCK = pygame.time.Clock()
FPS = 60
pygame.key.set_repeat(1, 10)

def game_over_text():
    over_text = over_font.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(over_text, (250, 250))


def show_score(x, y):
    score_value = score_font.render("Score " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (x, y))


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


def fire_bullet(x, y):
    global bullet_state

    bullet_state = 'Fire'
    screen.blit(bullet_img, (x + 16, y + 10))


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))

    if distance < 27:
        return True
    else:
        return False

while True:
    CLOCK.tick(FPS)
    screen.fill((0, 0, 0))
    screen.blit(back_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # If keystroke is pressed check whether it's right or left
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_x_change
        if keys[pygame.K_RIGHT]:
            player_x += player_x_change
        if keys[pygame.K_SPACE]:
            if bullet_state == 'Ready':
                bullet_sound = mixer.Sound(os.path.join(project_directory, "sound/laser.wav"))
                bullet_sound.set_volume(0.05)
                bullet_sound.play()
                bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)

    # Checking the boundaries
    if player_x < 0:
        player_x = 0
    elif player_x > 736:
        player_x = 736

    # Enemy movement
    for i in range(num_of_enemies):
        # Game over
        if enemy_y[i] > 440:
            for j in range(num_of_enemies):
                enemy_y[j] = 2000
            game_over_text()
            break
        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0:
            enemy_x_change[i] = 3.5
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 736:
            enemy_x_change[i] = -3.5
            enemy_y[i] += enemy_y_change[i]

        # Collision
        collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            bullet_sound = mixer.Sound(os.path.join(project_directory, "sound/explosion.wav"))
            bullet_sound.set_volume(0.05)
            bullet_sound.play()
            bullet_y = 480
            bullet_state = 'Ready'
            score += 1
            enemy_x[i] = random.randint(0, 735)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)

    # Bullet movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = 'Ready'
    if bullet_state == 'Fire':
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)
    show_score(text_x, text_y)

    pygame.display.update()
