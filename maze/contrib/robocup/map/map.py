from maze.modules.map import AbstractMap


class Map(AbstractMap):

    def build(self):
        self.matrix.get(0, 0).learn(
            walls=[1, 0, 1, 1]
        )

        self.matrix.get(0, 1).learn(
            walls=[0, 1, 1, 0]
        )

        self.matrix.get(1, 0).learn(
            walls=[1, 0, 0, 1]
        )

        self.matrix.get(1, 1).learn(
            walls=[1, 1, 0, 1]
        )

    def search(self):
        print(self.matrix.get(0, 0).getNeighbours())
