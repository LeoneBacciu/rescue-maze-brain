import numpy as np


class Matrix:

    def __init__(self, width):
        self._dims = (width, width)
        self._matrix = np.ndarray(shape=self._dims, dtype=object)  # TODO: change to Cell

    def __getitem__(self, item):
        return self._matrix[item]

    def __setitem__(self, key, value):  # TODO: add type check
        self._matrix[key] = value
