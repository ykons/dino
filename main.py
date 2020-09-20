import os
import pygame

from ui import UserInterface

os.environ['SDL_VIDEO_CENTERED'] = '1'

userInterface = UserInterface()
userInterface.run()

pygame.quit()
