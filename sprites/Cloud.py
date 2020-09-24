import random, math

import pygame
from utils import load_image


class Cloud(pygame.sprite.Sprite):
    SPRITE_X = 166
    SPRITE_Y = 2
    WIDTH = 92
    HEIGHT = 27
    MAX_CLOUD_GAP = 800
    MAX_SKY_LEVEL = 60
    MIN_CLOUD_GAP = 200
    MIN_SKY_LEVEL = 142

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('dino_sprites.png', self.SPRITE_X, self.SPRITE_Y, self.WIDTH, self.HEIGHT, -1, -1, -1)
        self.rect.left = x
        self.rect.top = y
        self.cloudGap = random.randint(self.MIN_CLOUD_GAP, self.MAX_CLOUD_GAP)

    def update(self, speed):
        self.rect = self.rect.move(-1*math.ceil(speed), 0)
        if self.rect.right < 0:
            self.kill()
