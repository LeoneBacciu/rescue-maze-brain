import pickle
from abc import ABC

import numpy as np

from maze.core.communication.directions import Direction
from maze.core.navigation import Coord
from maze.core.utils.constants import NEIGHBOURS
from maze.modules.map.matrix import AbstractCell


class AbstractMap(ABC):

    def __init__(self, settings):
        self.dims = settings.dims
        self.backup_dir = settings.backup_dir
        self.pos = Coord(self.dims[1] // 2, self.dims[2] // 2)
        self.matrix = settings.matrix(settings)

    def update(self, cell: AbstractCell):
        self.current_cell = cell
        self.current_cell.set_coord(self.pos)

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

    def goto(self, direction: Direction):
        self.pos += NEIGHBOURS[direction.value]

    @property
    def current_cell(self) -> AbstractCell:
        return self.matrix.get(self.pos)

    @current_cell.setter
    def current_cell(self, value):
        self.matrix.set(self.pos, value)

    def save(self):
        with open(f'{self.backup_dir}/backup.bk', 'w+') as f:
            pickle.dump(self, f)

    @staticmethod
    def load(settings):
        with open(f'{settings.backup_dir}/backup.bk', 'w+') as f:
            return pickle.load(f)
