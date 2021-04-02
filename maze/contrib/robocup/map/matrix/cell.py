from maze.modules.map.matrix.cell import AbstractCell


class Cell(AbstractCell):

    def __init__(self, walls, black, checkpoint, victim, *args, **kwargs):
        super().__init__(walls, *args, **kwargs)
        self.black = black
        self.checkpoint = checkpoint
        self.victim = victim

    def can_go(self, cell):
        return not cell.black

    @property
    def explored(self):
        return True
