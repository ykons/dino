import random

from .Layer import Layer

from sprites import Cloud


class HorizonLayer(Layer):
    def __init__(self, gameState):
        self.gameState = gameState
        self.clouds = self.gameState.clouds
        self.clouds.add(Cloud(1100, 10))

    def update(self):
        if len(self.clouds) < 5 and random.randrange(0, 300) == 10:
            self.clouds.add(Cloud(1100, random.randrange(300/5, 300/2)))

        # Update Sprites
        self.gameState.clouds.update()

    def render(self, surface):
        self.gameState.clouds.draw(surface)
