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

        directions = [Direction.top, Direction.top, Direction.left, Direction.top, Direction.top, Direction.right]

        for d in directions:
            ie = OutputEnvelope(d, True, 0x10)
            self.bridge.send_envelope(ie)
            e = self.bridge.read_envelope()
            print(str(e))

        return
        # while True:
        #     data, flags = self.bridge.read()
        #     print(data, flags)
        #     data, flags = self.brain.act(data, flags)
        #     self.bridge.write(data, flags)
