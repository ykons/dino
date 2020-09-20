from pygame.math import Vector2

from .GameItem import GameItem


class Cloud(GameItem):
    SPRITE_X = 166
    SPRITE_Y = 2
    WIDTH = 92
    HEIGHT = 27
    MAX_CLOUD_GAP = 800
    MAX_SKY_LEVEL = 60
    MIN_CLOUD_GAP = 200
    MIN_SKY_LEVEL = 142

    def __init__(self, state, position, tile=Vector2(SPRITE_X, SPRITE_Y), width=WIDTH, height=HEIGHT):
        super().__init__(state, position, tile, width, height)
