import math

from utils import load_image
from utils.values import FPS, WORLD_HEIGHT


class Ground():
    SPRITE_X = 2
    SPRITE_Y = 104
    WIDTH = 2400
    HEIGHT = 26

    def __init__(self):
        self.image, self.rect = load_image('dino_sprites.png', self.SPRITE_X, self.SPRITE_Y, self.WIDTH, self.HEIGHT, -1, -1, -1)
        self.image1, self.rect1 = load_image('dino_sprites.png', self.SPRITE_X, self.SPRITE_Y, self.WIDTH, self.HEIGHT, -1, -1, -1)
        self.rect.bottom = WORLD_HEIGHT
        self.rect1.bottom = WORLD_HEIGHT
        self.rect1.left = self.rect.right

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.image1, self.rect1)

    def update(self, deltaTime, speed):
        increment = math.floor(-1 * speed * (FPS / 1000) * deltaTime)

        #print("Ground.rect(%s, %s, %s, %s)", self.rect.top, self.rect.left, self.rect.bottom, self.rect.right)

        self.rect.left += increment
        self.rect1.left += increment

        if self.rect.right < 0:
            self.rect.left = self.rect1.right

        if self.rect1.right < 0:
            self.rect1.left = self.rect.right
