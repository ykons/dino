import random

import pygame

from .Layer import Layer

from sprites import *
from utils.values import WORLD_WIDTH, WORLD_HEIGHT


class HorizonLayer(Layer):
    BG_CLOUD_SPEED = 0.2
    BUMPY_THRESHOLD = .3
    CLOUD_FREQUENCY = .5
    OBSTACLE_FREQUENCY = .5
    HORIZON_HEIGHT = 16
    MAX_CLOUDS = 6
    MAX_OBSTACLES = 2

    def __init__(self, gameState):
        self.gameState = gameState

        self.clouds = self.gameState.clouds
        self.obstacles = self.gameState.obstacles
        self.ground = Ground()
        self.scoreboard = Scoreboard()

        self.cloudSpeed = self.BG_CLOUD_SPEED
        self.time = pygame.time.get_ticks()

    def addObstacle(self, speed):
        self.obstacles.add(Cactus())

    def updateObstacles(self, deltaTime, speed):
        obstacleSpeed = deltaTime * speed
        numObstacles = len(self.obstacles)

        if numObstacles > 0:
            self.obstacles.update(obstacleSpeed)

            lastObstacle = self.obstacles.sprites()[-1]

            # Check for adding a new obstacle.
            if (numObstacles < self.MAX_OBSTACLES and \
                (WORLD_WIDTH - lastObstacle.rect.left) > WORLD_WIDTH*0.7 and \
                self.OBSTACLE_FREQUENCY > random.random()):
                self.addObstacle(obstacleSpeed)
        else:
            self.addObstacle(obstacleSpeed)

    def addCloud(self):
        self.clouds.add(Cloud(WORLD_WIDTH, random.randrange(Cloud.MAX_SKY_LEVEL, Cloud.MIN_SKY_LEVEL)))

    def updateClouds(self, deltaTime, speed):
        cloudSpeed = self.cloudSpeed / 1000 * deltaTime * speed
        numClouds = len(self.clouds)

        if numClouds:
            self.clouds.update(cloudSpeed)

            lastCloud = self.clouds.sprites()[-1]

            # Check for adding a new cloud.
            if (numClouds < self.MAX_CLOUDS and \
                (WORLD_WIDTH - lastCloud.rect.left) > lastCloud.cloudGap and \
                self.CLOUD_FREQUENCY > random.random()):
                self.addCloud()
        else:
            self.addCloud()

    def update(self, runningTime, currentSpeed):
        deltaTime = runningTime - (self.time);
        self.time = runningTime;
        
        self.updateClouds(deltaTime, currentSpeed)
        self.updateObstacles(deltaTime, currentSpeed)
        self.ground.update(deltaTime, currentSpeed)
        self.scoreboard.update(self.gameState.score)

    def render(self, surface):
        self.clouds.draw(surface)
        self.ground.draw(surface)
        self.scoreboard.draw(surface)
