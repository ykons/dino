import pygame
from utils import load_image


class Cloud(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('dino_sprites.png', 166, 2, 92, 28, -1, -1, -1)
        self.speed = 3
        self.rect.left = x
        self.rect.top = y
        self.movement = [-1*self.speed, 0]

    def update(self):
        self.rect = self.rect.move(self.movement)
        if self.rect.right < 0:
            self.kill()
