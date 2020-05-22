class AbstractWalls:

    def __init__(self, *args):
        if len(args) == 0:
            self._walls = [False]*4
        else:
            self._walls = args[:4]

    def isFree(self, direction):
        return not self._walls[direction]

    def isWall(self, direction):
        return self._walls[direction]

    def setWalls(self, walls: list):
        self._walls = walls[:4]
