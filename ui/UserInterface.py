import pygame

from mode import GameModeObserver

WORLD_WIDTH = 1200
WORLD_HEIGHT = 300

class UserInterface(GameModeObserver):

    def __init__(self):
        from mode import PlayGameMode
        # Window
        pygame.init()
        self.window = pygame.display.set_mode((WORLD_WIDTH, WORLD_HEIGHT))
        pygame.display.set_caption("Dino")
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
            self.window.fill((255,255,255))

            # Inputs and updates are exclusives
            if self.playGameMode is not None:
                self.playGameMode.processInput()
                self.playGameMode.update()
                self.playGameMode.render(self.window)

            # Update display
            pygame.display.update()
            #pygame.display.flip()
            self.clock.tick(60)
