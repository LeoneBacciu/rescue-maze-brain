from abc import ABC, abstractmethod
import numpy as np

from maze.core.utils import MazeSettings
from maze.core.utils.navigation import Coord


class AbstractMatrix(ABC):

    def __init__(self, settings: MazeSettings):
        self._dims = settings.dims
        self._cell = settings.cell
        self._level = 0
        self._matrix = np.ndarray(shape=self._dims, dtype=settings.cell)
        for h in range(self._dims[0]):
            for y in range(self._dims[1]):
                for x in range(self._dims[2]):
                    self._matrix[h][x][y] = settings.cell(x, y, self, settings)

    def climb(self):
        self._level += 1

    def descend(self):
        self._level -= 1 if self._level >= 1 else 0

    def get(self, *args):
        if len(args) == 1 and type(args[0]) == Coord:
            return self._matrix[self._level][args[0].y][args[0].x]
        else:
            return self._matrix[self._level][args[1]][args[0]]
