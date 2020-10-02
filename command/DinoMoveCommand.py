from .Command import Command


class DinoMoveCommand(Command):
    """
    This command moves a unit in a given direction
    """

    def __init__(self, state, moveVector):
        self.state = state
        self.moveVector = moveVector

    def run(self):
        dino = self.state.dinos.sprites()[0]

        if (self.moveVector.y == 1):
            dino.startJump(self.state.currentSpeed)