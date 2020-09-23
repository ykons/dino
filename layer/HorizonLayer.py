import random

from .Layer import Layer

from sprites import Cloud
import utils.values as vl


class HorizonLayer(Layer):
    def __init__(self, gameState):
        self.gameState = gameState
        self.clouds = self.gameState.clouds

    def update(self):
        if len(self.clouds) < 5 and random.randrange(0, 300) == 10:
            self.clouds.add(Cloud(vl.WORLD_WIDTH, random.randrange(vl.WORLD_HEIGHT/5, vl.WORLD_HEIGHT/2)))

        # Update Sprites
        self.gameState.clouds.update()

    def render(self, surface):
        self.gameState.clouds.draw(surface)
