import pygame
from pygame import Vector2

import utils.values as vl

from sprites import Cloud


class GameState():

    def __init__(self):
        self.epoch = 0
        self.score = 0
        self.high_score = 0
        self.worldSize = Vector2(vl.WORLD_WIDTH, vl.WORLD_HEIGHT)
        self.currentSpeed = vl.SPEED

        self.dinos  = pygame.sprite.Group()
        self.clouds = pygame.sprite.Group()
        self.ground = pygame.sprite.Group()

        self.observers = []

    @property
    def worldWidth(self):
        """
        Returns the world width as an integer
        """
        return int(self.worldSize.x)

    @property
    def worldHeight(self):
        """
        Returns the world height as an integer
        """
        return int(self.worldSize.y)

    def isInside(self, position):
        """
        Returns true is position is inside the world
        """
        return position.x >= 0 and position.x < self.worldWidth \
            and position.y >= 0 and position.y < self.worldHeight

    def addObserver(self, observer):
        """
        Add a game state observer. 
        All observer is notified when something happens (see GameStateObserver class)
        """
        self.observers.append(observer)
