from .Layer import Layer

from sprites import Cloud


class HorizonLayer(Layer):
    def __init__(self, imageFile, gameState, clouds):
        super().__init__(imageFile)
        self.gameState = gameState
        self.clouds = clouds

    def update(self):
        self.clouds.update()

    def render(self, surface):
        self.clouds.draw(surface)
