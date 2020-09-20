class GameItem():
    def __init__(self, state, position, tile, width, height):
        self.state = state
        self.status = "alive"
        self.position = position
        self.tile = tile
        self.width = width
        self.height = height
