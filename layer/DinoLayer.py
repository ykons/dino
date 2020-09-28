import random

import pygame

from .Layer import Layer

from sprites import *
import utils.values as vl


class DinoLayer(Layer):
    def __init__(self, gameState):
        self.gameState = gameState

        self.dinos = self.gameState.dinos
        self.dinos.add(Dino())

        self.time = pygame.time.get_ticks()

    def update(self, runningTime, currentSpeed):        
        self.dinos.update()

    def render(self, surface):
        self.dinos.draw(surface)
