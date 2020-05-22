from maze.contrib.robocup.map.matrix import Matrix, Cell, Walls
from maze.contrib.robocup.map import Map
from maze.core.utils import MazeSettings

if __name__ == '__main__':

    settings = MazeSettings(
        matrix=Matrix,
        cell=Cell,
        walls=Walls,
        dims=(1, 30, 30)
    )

    maze = Map(settings)
    maze.build()
    maze.update(0, 0, [0, 0, 1, 1])
    maze.update(1, 0, [1, 1, 0, 0], black=True)
    maze.search()
