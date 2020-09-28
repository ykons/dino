from .Command import Command


class MoveCommand(Command):
    """
    This command moves a unit in a given direction
    """

    def __init__(self, state, item, moveVector):
        self.state = state
        self.item = item
        self.moveVector = moveVector

    def run(self):
        # Destroyed units can't move
        if self.item.status != "alive":
            return

        newPos = self.item.position + self.moveVector

        # If the bullet goes outside the world, destroy it
        if not self.state.isInside(newPos):
            self.item.status = "destroyed"
            return

        self.item.position = newPos
