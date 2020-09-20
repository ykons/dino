from .Layer import Layer

class HorizonLayer(Layer):
    def __init__(self, imageFile, gameState, clouds):
        super().__init__(imageFile)
        self.gameState = gameState
        self.clouds = clouds

    def render(self, surface):
        for cloud in self.clouds:
            if cloud.status == "alive":
                self.renderTile(surface, cloud.position,
                                cloud.tile, cloud.width, cloud.height)
