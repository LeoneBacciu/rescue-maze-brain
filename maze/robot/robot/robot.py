from typing import Type

from maze.contrib.robocup.communication.envelope import OutputEnvelope, InputEnvelope
from maze.contrib.robocup.robot.brain import Brain
from maze.core.communication.directions import Direction
from maze.core.utils.settings import MazeSettings, SerialSettings
from maze.robot.brain.brain import AbstractBrain


class Robot:

    def __init__(self, brain: Type[Brain], maze_settings: MazeSettings, serial_settings: SerialSettings):
        self.map = maze_settings.map(maze_settings)
        self.bridge = serial_settings.bridge(serial_settings)
        self.brain = brain(self.map, serial_settings.input_envelope, serial_settings.output_envelope)

    def run(self):

        self.bridge.handshake()
        e = OutputEnvelope(Direction.top, True, False)
        self.bridge.send_envelope(e)
        # print(str(e.walls))
        # print(e.black)
        # print(e.checkpoint)
        #
        # self.bridge.send(BaseDirections(True, False, False, False), InputFlags(was_black=True))

        return
        # while True:
        #     data, flags = self.bridge.read()
        #     print(data, flags)
        #     data, flags = self.brain.act(data, flags)
        #     self.bridge.write(data, flags)
