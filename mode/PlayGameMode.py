from .GameMode import GameMode

from state import GameState
from layer import HorizonLayer
from command import MoveCommand, DeleteDestroyedCommand

import pygame
from pygame.math import Vector2


class PlayGameMode(GameMode):
    def __init__(self):
        super().__init__()
        # Game state
        self.gameState = GameState()

        # Layers
        self.layers = [
            HorizonLayer("assets/level/dino_sprites.png", self.gameState, self.gameState.clouds)
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

        # Move the world's itens
        for cloud in self.gameState.clouds:
            self.commands.append(
                MoveCommand(self.gameState, cloud, Vector2(-1*self.gameState.worldVelocity, 0))
            )

        # Delete any destroyed item
        self.commands.append(
            DeleteDestroyedCommand(self.gameState.clouds)
        )

    def update(self):
        for command in self.commands:
            command.run()
        self.commands.clear()
        self.gameState.epoch += 1

        # Check game over
        #if self.playerDino.status != "alive":
        #    self.gameOver = True
        #    self.notifyGameLost()

    def render(self, window):
        for layer in self.layers:
            layer.render(window)
