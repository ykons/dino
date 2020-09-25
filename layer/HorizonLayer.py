import random

import pygame

from .Layer import Layer

from sprites import *
import utils.values as vl


class HorizonLayer(Layer):
    BG_CLOUD_SPEED = 0.2
    BUMPY_THRESHOLD = .3
    CLOUD_FREQUENCY = .5
    HORIZON_HEIGHT = 16
    MAX_CLOUDS = 6

    def __init__(self, gameState):
        self.gameState = gameState

        self.clouds = self.gameState.clouds
        self.ground = Ground()
        self.scoreboard = Scoreboard()

        self.cloudFrequency = self.CLOUD_FREQUENCY
        self.cloudSpeed = self.BG_CLOUD_SPEED
        self.time = pygame.time.get_ticks()

    def addCloud(self):
        self.clouds.add(Cloud(vl.WORLD_WIDTH, random.randrange(Cloud.MAX_SKY_LEVEL, Cloud.MIN_SKY_LEVEL)))

    def updateClouds(self, deltaTime, speed):
        cloudSpeed = self.cloudSpeed / 1000 * deltaTime * speed
        numClouds = len(self.clouds)

        if numClouds:
            self.clouds.update(cloudSpeed)

            lastCloud = self.clouds.sprites()[-1]

            # Check for adding a new cloud.
            if (numClouds < self.MAX_CLOUDS and \
                (vl.WORLD_WIDTH - lastCloud.rect.left) > lastCloud.cloudGap and \
                self.cloudFrequency > random.random()):
                self.addCloud()
        else:
            self.addCloud()

    def update(self, runningTime, currentSpeed):
        deltaTime = runningTime - (self.time);
        self.time = runningTime;
        
        self.updateClouds(deltaTime, currentSpeed)
        self.ground.update(deltaTime, currentSpeed)
        self.scoreboard.update(self.gameState.score)

    def render(self, surface):
        self.clouds.draw(surface)
        self.ground.draw(surface)
        self.scoreboard.draw(surface)
