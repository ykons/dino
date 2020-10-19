import random, math

import pygame
from utils import load_image
from utils.values import WORLD_WIDTH, WORLD_HEIGHT


class Cactus(pygame.sprite.Sprite):
    SPRITE_X = 446
    SPRITE_Y = 2
    WIDTH = 204
    HEIGHT = 70

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('dino_sprites.png', self.SPRITE_X, self.SPRITE_Y, self.WIDTH, self.HEIGHT, -1, -1, -1)
        self.rect.x = WORLD_WIDTH
        self.rect.y = WORLD_HEIGHT*0.98

    def update(self, speed):
        self.rect.x -= math.ceil(speed)
        if self.rect.right < 0:
            pass #self.kill()
