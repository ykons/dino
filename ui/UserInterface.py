import pygame

from mode import GameModeObserver
import utils.values as vl


class UserInterface(GameModeObserver):

    def __init__(self):
        from mode import PlayGameMode
        # Window
        pygame.init()
        self.window = pygame.display.set_mode((vl.WORLD_WIDTH, vl.WORLD_HEIGHT))
        pygame.display.set_caption(vl.CAPTION)
        pygame.display.set_icon(pygame.image.load("assets/ui/dino.png"))

        # Load Game
        self.playGameMode = PlayGameMode()
        self.playGameMode.addObserver(self)
        self.playGameMode.update()

        # Loop properties
        self.clock = pygame.time.Clock()
        self.running = True

    def quitRequested(self):
        self.running = False

    def run(self):
        while self.running:
            self.window.fill(vl.WHITE)

            # Inputs and updates are exclusives
            if self.playGameMode is not None:
                self.playGameMode.processInput()
                self.playGameMode.update()
                self.playGameMode.render(self.window)

            # Update display
            pygame.display.update()
            # pygame.display.flip()
            self.clock.tick(60)
