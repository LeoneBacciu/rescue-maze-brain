from maze.contrib.robocup.map import Map
from maze.contrib.robocup.map.matrix import Matrix, Cell, Walls
from maze.contrib.robocup.communication.flags import Flags
from maze.core.utils.settings import *
from maze.bridge import Bridge
from maze.robot.robot.robot import Robot

if __name__ == '__main__':

    maze_settings = MazeSettings(
        map=Map,
        matrix=Matrix,
        cell=Cell,
        walls=Walls,
        dims=(1, 30, 30)
    )

    serial_settings = SerialSettings(
        bridge=Bridge,
        port='/dev/pts/3',
        baud_rate=9600,
        flag=Flags
    )

    robot = Robot(
        maze_settings=maze_settings,
        serial_settings=serial_settings
    )

    robot.run()
