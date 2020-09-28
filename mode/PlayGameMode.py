import pygame
from pygame.math import Vector2

from state import GameState
from layer import HorizonLayer, DinoLayer
from command import MoveCommand, DeleteDestroyedCommand

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
        self.dino = self.gameState.dinos.sprites()[0]
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
                elif event.key == pygame.K_ESCAPE:
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
                MoveCommand(self.gameState, self.dino, moveVector)
            )

    def update(self, runningTime):
        for layer in self.layers:
            layer.update(runningTime, self.gameState.currentSpeed)

        for command in self.commands:
            command.run()
        self.commands.clear()

        # Check game over
        # if self.playerDino.status != "alive":
        #    self.gameOver = True
        #    self.notifyGameLost()

        if self.gameState.epoch%7 == 6:
            self.gameState.score += 1

        if self.gameState.epoch%700 == 699:
            self.gameState.currentSpeed += 1
        
        self.gameState.epoch += 1

    def render(self, window):
        for layer in self.layers:
            layer.render(window)
