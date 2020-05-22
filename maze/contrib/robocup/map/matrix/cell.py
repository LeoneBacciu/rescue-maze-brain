from maze.modules.map.matrix.cell import AbstractCell


class Cell(AbstractCell):

    def __init__(self, x, y, matrix, settings):
        super().__init__(x, y, matrix, settings)
        self.black = False
        self.checkpoint = False
        self.victim = False
        self.ramp = False

    def learn(self, walls, **kwargs):
        super().learn(walls, **kwargs)
        self.black = kwargs.get('black', False)
        self.checkpoint = kwargs.get('checkpoint', False)
        self.victim = kwargs.get('victim', False)
        self.ramp = kwargs.get('ramp', False)

    def canGo(self, cell):
        return not cell.black
