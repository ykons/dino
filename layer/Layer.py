import pygame
from pygame import Rect

from state import GameStateObserver


class Layer(GameStateObserver):
    def __init__(self):
        pass

    def update(self):
        raise NotImplementedError()

    def render(self, surface):
        raise NotImplementedError()
