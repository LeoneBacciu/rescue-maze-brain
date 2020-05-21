import numpy as np

from src.map.matrix.cell import Cell


class Matrix:

    def __init__(self, width):
        self._dims = (width, width)
        self._matrix = np.ndarray(shape=self._dims, dtype=Cell)

    def __getitem__(self, item):
        return self._matrix[item]

    def __setitem__(self, key, value):
        if type(value) == Cell:
            self._matrix[key] = value
