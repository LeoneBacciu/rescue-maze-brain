from abc import ABC, abstractmethod

from maze.core.navigation import Coord
from maze.core.utils.constants import *


class AbstractCell(ABC):

    @abstractmethod
    def __init__(self, walls, *args, **kwargs):
        self.coord = Coord(0, 0)
        self.walls = walls

    @abstractmethod
    def can_go(self, cell):
        pass

    def isAdjacent(self, cell):
        return (cell.pos.x - self.coord.x, cell.pos.y - self.coord.y) in NEIGHBOURS

    def getNeighbours(self, matrix):
        neighbours = []
        for i, d in enumerate(NEIGHBOURS):
            if self.walls[i] == 0:
                cell = matrix.get(self.coord + d)
                if self.isAdjacent(cell) and self.can_go(cell):
                    neighbours.append(self.coord + d)
        return neighbours

    def set_coord(self, coord: Coord):
        self.coord = coord

    @property
    @abstractmethod
    def explored(self):
        pass


class AnonymousCell(AbstractCell):
    def __init__(self, *args, **kwargs):
        super().__init__(None, *args, **kwargs)

    def can_go(self, cell):
        return False

    @property
    def explored(self):
        return False
