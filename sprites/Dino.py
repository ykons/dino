import pygame
from utils import load_sprite_sheet
from utils.values import WORLD_WIDTH, WORLD_HEIGHT, GRAVITY


class Dino(pygame.sprite.Sprite):
    SPRITE_X = 1680
    SPRITE_Y = 2
    WIDTH = 440
    HEIGHT = 94

    def __init__(self, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self)
        self.images, self.rect = load_sprite_sheet('dino_sprites.png', self.SPRITE_X, self.SPRITE_Y, self.WIDTH, self.HEIGHT, 5, 1, sizex, sizey, -1)
        self.images1, self.rect1 = load_sprite_sheet('dino_sprites.png', 2207, 39, 118, 59, 2, 1, sizex, sizey, -1)
        self.rect.bottom = int(0.98*WORLD_HEIGHT)
        self.rect.left = WORLD_WIDTH/15
        self.image = self.images[0]
        self.index = 0
        self.counter = 0
        self.score = 0
        self.isJumping = False
        self.isDead = False
        self.isDucking = False
        self.isBlinking = False
        self.movement = [0,0]
        self.jumpSpeed = 11.5

        self.stand_pos_width = self.rect.width
        self.duck_pos_width = self.rect1.width

    def update(self):
        if self.isJumping:
            self.movement[1] = self.movement[1] + GRAVITY

        if self.isJumping:
            self.index = 0
        elif self.isBlinking:
            if self.index == 0:
                if self.counter % 400 == 399:
                    self.index = (self.index + 1)%2
            else:
                if self.counter % 20 == 19:
                    self.index = (self.index + 1)%2

        elif self.isDucking:
            if self.counter % 5 == 0:
                self.index = (self.index + 1)%2
        else:
            if self.counter % 5 == 0:
                self.index = (self.index + 1)%2 + 2

        if self.isDead:
           self.index = 4

        if not self.isDucking:
            self.image = self.images[self.index]
            self.rect.width = self.stand_pos_width
        else:
            self.image = self.images1[(self.index)%2]
            self.rect.width = self.duck_pos_width

        self.rect = self.rect.move(self.movement)

        if not self.isDead and self.counter % 7 == 6 and self.isBlinking == False:
            self.score += 1

        self.counter = (self.counter + 1)
