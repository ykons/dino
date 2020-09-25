import pygame
from utils import load_image, load_sprite_sheet, extractDigits
from utils.values import WORLD_WIDTH, WORLD_HEIGHT


class Scoreboard():
    SPRITE_X = 1294
    SPRITE_Y = 2
    WIDTH = 240
    HEIGHT = 26

    def __init__(self, x=-1, y=-1):
        self.score = 0
        self.tempimages, self.temprect = load_sprite_sheet('dino_sprites.png', self.SPRITE_X, self.SPRITE_Y, self.WIDTH, self.HEIGHT, 12, 1, -1, -1, -1)
        self.image = pygame.Surface((int(self.WIDTH*5/12), int(self.HEIGHT)))
        self.rect = self.image.get_rect()
        if x == -1:
            self.rect.left = WORLD_WIDTH*0.89
        else:
            self.rect.left = x
        if y == -1:
            self.rect.top = WORLD_HEIGHT*0.1
        else:
            self.rect.top = y

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, score):
        score_digits = extractDigits(score)
        self.image.fill((255,255,255))
        for s in score_digits:
            self.image.blit(self.tempimages[s],self.temprect)
            self.temprect.left += self.temprect.width
        self.temprect.left = 0
