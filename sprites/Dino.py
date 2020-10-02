import pygame

from utils import load_sprite_sheet
from utils.values import WORLD_WIDTH, WORLD_HEIGHT, GRAVITY, BOTTOM_PAD


class Dino(pygame.sprite.Sprite):
    SPRITE_X = 1680
    SPRITE_Y = 2
    WIDTH = 440
    HEIGHT = 94
    INIITAL_JUMP_VELOCITY = -18
    MIN_JUMP_HEIGHT = 60
    MAX_JUMP_HEIGHT = 120
    DROP_VELOCITY = -9
    SPEED_DROP_COEFFICIENT = 3

    def __init__(self, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self)
        self.images, self.rect = load_sprite_sheet(
            'dino_sprites.png', self.SPRITE_X, self.SPRITE_Y, self.WIDTH, self.HEIGHT, 5, 1, sizex, sizey, -1)
        self.images1, self.rect1 = load_sprite_sheet(
            'dino_sprites.png', 2207, 39, 118, 59, 2, 1, sizex, sizey, -1)
        self.groundYPos = int(WORLD_HEIGHT - self.HEIGHT - BOTTOM_PAD)
        self.rect.y = self.groundYPos
        self.rect.x = WORLD_WIDTH/30
        self.image = self.images[0]
        self.index = 0
        self.counter = 0
        self.score = 0
        self.isJumping = False
        self.isDead = False
        self.isDucking = False
        self.reachedMinHeight = False
        self.speedDrop = False
        self.minJumpHeight = self.groundYPos - self.MIN_JUMP_HEIGHT
        self.jumpVelocity = 0

        self.stand_pos_width = self.rect.width
        self.duck_pos_width = self.rect1.width

    def startJump(self, speed):
        if (not self.isJumping):
            # self.update(0, Trex.status.JUMPING)
            # Tweak the jump velocity based on the speed.
            self.jumpVelocity = self.INIITAL_JUMP_VELOCITY - (speed / 10)
            self.isJumping = True
            self.reachedMinHeight = False
            self.speedDrop = False

    def endJump(self):
        if (self.reachedMinHeight and
            self.jumpVelocity < self.DROP_VELOCITY):
            self.jumpVelocity = self.DROP_VELOCITY

    def updateJump(self, deltaTime):
        msPerFrame = 1000 / 60 #Trex.animFrames[this.status].msPerFrame
        framesElapsed = deltaTime / msPerFrame

        # Speed drop makes Trex fall faster.
        if (self.speedDrop):
            self.rect.y += round(self.jumpVelocity *
            self.SPEED_DROP_COEFFICIENT * framesElapsed)
        else:
            self.rect.y += round(self.jumpVelocity * framesElapsed)

        self.jumpVelocity += GRAVITY * framesElapsed

        # Minimum height has been reached.
        if (self.rect.y < self.minJumpHeight or self.speedDrop):
            self.reachedMinHeight = True

        # Reached max height
        if (self.rect.y < self.MAX_JUMP_HEIGHT or self.speedDrop):
            self.endJump()

        # Back down at ground level. Jump completed.
        if (self.rect.y > self.groundYPos):
            self.reset()

    def setSpeedDrop(self):
        self.speedDrop = True
        self.jumpVelocity = 1

    def setDuck(self, isDucking):
        if (isDucking):# and self.status != Trex.status.DUCKING):
            # self.update(0, Trex.status.DUCKING)
            self.isDucking = True
        elif False:#(self.status == Trex.status.DUCKING):
            # self.update(0, Trex.status.RUNNING)
            self.isDucking = False

    def reset(self):
        self.rect.x = WORLD_WIDTH/30
        self.rect.y = self.groundYPos
        self.jumpVelocity = 0
        self.isJumping = False
        self.isDucking = False
        #self.update(0, Trex.status.RUNNING)
        self.speedDrop = False

    def update(self, deltaTime):
        if self.isJumping:
            self.updateJump(deltaTime)
            self.index = 0

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

        if not self.isDead and self.counter % 7 == 6:
            self.score += 1

        self.counter = (self.counter + 1)
