from abc import ABC, abstractmethod

from maze.core.utils import MazeSettings
from maze.core.utils.navigation import Coord


class AbstractMap(ABC):

    def __init__(self, settings: MazeSettings):
        self.dims = settings.dims
        self.pos = Coord(self.dims[1]//2, self.dims[2]//2)
        self.matrix = settings.matrix(settings)

    def update(self, x, y, walls, **kwargs):
        self.pos.update(x, y)
        self.matrix.get(x, y).learn(walls, **kwargs)
