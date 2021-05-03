# set PYTHONPATH=%PYTHONPATH%;C:\Users\sonoa\PyCharmProjects\rescue-maze-brain\
# export PYTHONPATH="${PYTHONPATH}:/home/pi/robot/rescue-maze-brain/"

from maze.contrib.robocup.communication.envelope import InputEnvelope, OutputEnvelope
from maze.contrib.robocup.map import Map
from maze.core.utils.settings import *
from maze.bridge import Bridge
from maze.robot.robot.robot import Robot
from maze.contrib.robocup.robot.brain import Brain

if __name__ == '__main__':

    maze_settings = MazeSettings(
        map=Map,
        matrix=Matrix,
        cell=Cell,
        dims=(1, 30, 30)
    )

    serial_settings = SerialSettings(
        bridge=Bridge,
        port='COM3',
        baud_rate=9600,
        input_envelope=InputEnvelope,
        output_envelope=OutputEnvelope
    )

    robot = Robot(
        brain=Brain,
        maze_settings=maze_settings,
        serial_settings=serial_settings
    )

    robot.run()
