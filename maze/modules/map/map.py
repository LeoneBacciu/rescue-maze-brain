import pickle
from abc import ABC
import numpy as np

from maze.core.utils.settings import MazeSettings
from maze.core.navigation import Coord


class AbstractMap(ABC):

    def __init__(self, settings: MazeSettings):
        self.dims = settings.dims
        self.backup_dir = settings.backup_dir
        self.pos: Coord = None
        self.matrix = settings.matrix(settings)
        self.center()
        self.ramps = []
        self.pending = []

    def update(self, coord: Coord, walls, **kwargs):
        cell = self.matrix.get(coord)
        cell.learn(walls, **kwargs)

    def bfs(self, check):
        queue = [[self.pos]]
        history = np.full(shape=self.dims[1:], fill_value=False, dtype=bool)
        while queue:
            element = queue.pop(0)
            if check(self.matrix.get(element[-1])):
                return element
            if history[element[-1].y][element[-1].x]:
                continue
            history[element[-1].y][element[-1].x] = True
            for neighbour in self.matrix.get(element[-1]).getNeighbours():
                queue.append(element + [neighbour])
        return False

    def goto(self, coord: Coord):
        self.pos.update(coord.x, coord.y)

    def center(self):
        self.pos = Coord(self.dims[1] // 2, self.dims[2] // 2)

    def save(self):
        with open(f'{self.backup_dir}/backup.bk', 'w+') as f:
            pickle.dump(self, f)

    @staticmethod
    def load(settings: MazeSettings):
        with open(f'{settings.backup_dir}/backup.bk', 'w+') as f:
            return pickle.load(f)
