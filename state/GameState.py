from pygame import Vector2

from .Cloud import Cloud


class GameState():
    ACCELERATION = 0.001
    BG_CLOUD_SPEED = 0.2
    CLEAR_TIME = 3000
    CLOUD_FREQUENCY = 0.5
    GAMEOVER_CLEAR_TIME = 750
    GAP_COEFFICIENT = 0.6
    GRAVITY = 0.6
    INITIAL_JUMP_VELOCITY = 12
    INVERT_FADE_DURATION = 12000
    INVERT_DISTANCE = 700
    MAX_BLINK_COUNT = 3
    MAX_CLOUDS = 6
    MAX_OBSTACLE_LENGTH = 3
    MAX_OBSTACLE_DUPLICATION = 2
    MAX_SPEED = 13
    MIN_JUMP_HEIGHT = 35
    SPEED = 6
    SPEED_DROP_COEFFICIENT = 3

    def __init__(self):
        from ui.UserInterface import WORLD_WIDTH
        from ui.UserInterface import WORLD_HEIGHT
        self.epoch = 0
        self.worldSize = Vector2(WORLD_WIDTH, WORLD_HEIGHT)
        self.worldVelocity = GameState.SPEED
        self.clouds = [Cloud(self, Vector2(1100, 10))]
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
