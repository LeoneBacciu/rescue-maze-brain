from abc import ABC, abstractmethod

from maze.core.utils import MazeSettings
from maze.core.utils.constants import *
from maze.core.utils.navigation.coord import Coord


class AbstractCell(ABC):

    def __init__(self, x, y, matrix, settings: MazeSettings):
        self.COORD = Coord(x, y)
        self.explored = False
        self.walls = settings.walls()
        self.matrix = matrix

    def learn(self, walls, **kwargs):
        self.walls.setWalls(walls)
        self.explored = True

    @abstractmethod
    def canGo(self, cell):
        pass

    def isAdjacent(self, cell):
        return (cell.COORD.x-self.COORD.x, cell.COORD.y-self.COORD.y) in NEIGHBOURS

    def getNeighbours(self):
        neighbours = []
        for i, d in enumerate(NEIGHBOURS):
            if self.walls.isFree(i):
                cell = self.matrix.get(self.COORD + d)
                if self.isAdjacent(cell) and self.canGo(cell):
                    neighbours.append(d)
        return neighbours
