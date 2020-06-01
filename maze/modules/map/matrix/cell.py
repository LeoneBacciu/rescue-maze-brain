from abc import ABC, abstractmethod

from maze.core.utils.settings import MazeSettings
from maze.core.utils.constants import *
from maze.core.navigation import Coord


class AbstractCell(ABC):

    def __init__(self, x, y, matrix, settings: MazeSettings):
        self.pos = Coord(x, y)
        self.explored = False
        self.walls = settings.walls()
        self.matrix = matrix
        self.ramp = []
        self.ramp_id = None

    def learn(self, walls, **kwargs):
        self.walls.setWalls(walls)
        self.explored = True
        self.ramp = kwargs.get('ramp', [])
        self.ramp_id = kwargs.get('ramp_id', None)

    @abstractmethod
    def canGo(self, cell):
        pass

    def isAdjacent(self, cell):
        return (cell.pos.x - self.pos.x, cell.pos.y - self.pos.y) in NEIGHBOURS

    def getNeighbours(self):
        neighbours = []
        for i, d in enumerate(NEIGHBOURS):
            if self.walls.isFree(i):
                cell = self.matrix.get(self.pos + d)
                if self.isAdjacent(cell) and self.canGo(cell):
                    neighbours.append(self.pos + d)
        return neighbours
