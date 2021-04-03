import pickle
from abc import ABC

import numpy as np

from maze.core.communication.directions import Direction
from maze.core.navigation import Coord
from maze.core.navigation.coord import direction_to_coord
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

    def goto(self, direction: Direction):
        self.pos += direction_to_coord[direction.value]

    def bfs(self, check):
        queue = [[self.pos]]
        history = np.full(shape=self.dims[1:], fill_value=False, dtype=bool)
        while queue:
            element = queue.pop(0)
            if check(self.get(element[-1])):
                return element
            if history[element[-1].y][element[-1].x]:
                continue
            history[element[-1].y][element[-1].x] = True
            for neighbour in self.get(element[-1]).get_neighbours(self.matrix):
                queue.append(element + [neighbour])
        return False

    def get(self, *args):
        return self.matrix.get(*args)

    @property
    def current_cell(self) -> AbstractCell:
        return self.get(self.pos)

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
