import pygame
from pygame import Rect

from state import GameStateObserver


class Layer(GameStateObserver):
    def __init__(self, imageFile):
        self.texture = pygame.image.load(imageFile)

    def setTileset(self, imageFile):
        self.texture = pygame.image.load(imageFile)

    def renderTile(self, surface, position, tile, width, height):
        # Texture
        textureRect = Rect(int(tile.x), int(tile.y), width, height)

        # Draw
        surface.blit(self.texture, position, textureRect)

    def render(self, surface):
        raise NotImplementedError()
