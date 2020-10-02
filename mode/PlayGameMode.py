import pygame
from pygame.math import Vector2

from state import GameState
from layer import HorizonLayer, DinoLayer
from command import DinoMoveCommand
from utils.values import ACCELERATION, MAX_SPEED

from .GameMode import GameMode


class PlayGameMode(GameMode):
    def __init__(self):
        super().__init__()
        # Game state
        self.gameState = GameState()

        # Layers
        self.layers = [
            HorizonLayer(self.gameState),
            DinoLayer(self.gameState)
        ]

        # All layers listen to game state events
        for layer in self.layers:
            self.gameState.addObserver(layer)

        # Controls
        self.gameOver = False
        self.commands = []

    def processInput(self):
        # Pygame events (close, keyboard and mouse click)
        moveVector = Vector2()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    self.notifyQuitRequested()
                    break
                elif event.key == pygame.K_ESCAPE or \
                    event.key == pygame.K_q:
                    self.notifyQuitRequested()
                    break
                elif event.key == pygame.K_w:
                    moveVector.y = 1
                elif event.key == pygame.K_s:
                    moveVector.y = -1

        # If the game is over, all commands creations are disabled
        if self.gameOver:
            return
        
        # Keyboard controls the moves of the player's unit
        if moveVector.x != 0 or moveVector.y != 0:
            self.commands.append(
                DinoMoveCommand(self.gameState, moveVector)
            )

    def update(self, runningTime):
        for command in self.commands:
            command.run()
        self.commands.clear()

        for layer in self.layers:
            layer.update(runningTime, self.gameState.currentSpeed)

        # Check game over
        # if self.playerDino.status != "alive":
        #    self.gameOver = True
        #    self.notifyGameLost()

        if self.gameState.epoch%7 == 6:
            self.gameState.score += 1

        if self.gameState.currentSpeed < MAX_SPEED:
            self.gameState.currentSpeed += ACCELERATION
        
        self.gameState.epoch += 1

    def render(self, window):
        for layer in self.layers:
            layer.render(window)
