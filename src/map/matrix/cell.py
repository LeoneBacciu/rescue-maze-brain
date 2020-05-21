from src.map.matrix.matrix import Matrix


class Cell:

    def __init__(self, x, y, matrix: Matrix):
        self._coord = (x, y)
        self._explored = False
        self._walls = [False] * 4
        self._black = False
        self._silver = False
        self._victim = False
        self._matrix = matrix

    def learn(self, walls, black, silver):
        self._walls = walls
        self._black = black
        self._silver = silver
        self._victim = False
        self._explored = True
